#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LECTURES_FILE = PROJECT_ROOT / "lectures.yaml"
DEFAULT_LANGUAGES = ("ru", "en", "en-US", "en-GB")
RAW_PLACEHOLDERS = (
    "[сюда будет вставлен транскрипт]",
    "[транскрипт не удалось получить автоматически",
    "method: not-fetched",
)


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def clean_scalar(value: str) -> str:
    value = value.strip()
    if value in {"", "''", '""'}:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_minimal_yaml(text: str) -> list[dict[str, str]]:
    lectures: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line == "lectures:":
            continue

        if line.startswith("- "):
            if current:
                lectures.append(current)
            current = {}
            line = line[2:].strip()

        if current is None or ":" not in line:
            continue

        key, value = line.split(":", 1)
        current[key.strip()] = clean_scalar(value)

    if current:
        lectures.append(current)

    return lectures


def load_lectures() -> list[dict[str, str]]:
    if not LECTURES_FILE.exists():
        raise FileNotFoundError(f"Не найден файл {LECTURES_FILE}")

    text = LECTURES_FILE.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        return parse_minimal_yaml(text)

    data = yaml.safe_load(text) or {}
    lectures = data.get("lectures", [])
    if not isinstance(lectures, list):
        raise ValueError("В lectures.yaml поле `lectures` должно быть списком")
    return [lecture for lecture in lectures if isinstance(lecture, dict)]


def append_log(lecture_id: str, level: str, message: str) -> None:
    log_dir = PROJECT_ROOT / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{lecture_id}.log.md"
    with log_path.open("a", encoding="utf-8") as file:
        file.write(f"\n## {timestamp()} — {level}\n\n{message.strip()}\n")


def extract_video_id(url: str) -> str:
    url = url.strip()
    if not url or "PASTE_YOUTUBE_URL_HERE" in url:
        raise ValueError("youtube_url не заполнен")

    parsed = urlparse(url)
    host = parsed.netloc.lower()

    if host.endswith("youtu.be"):
        candidate = parsed.path.strip("/").split("/")[0]
        if candidate:
            return candidate

    if "youtube.com" in host:
        query_id = parse_qs(parsed.query).get("v", [""])[0]
        if query_id:
            return query_id

        parts = [part for part in parsed.path.split("/") if part]
        for marker in ("embed", "shorts", "live"):
            if marker in parts:
                index = parts.index(marker)
                if index + 1 < len(parts):
                    return parts[index + 1]

    match = re.search(r"(?:v=|youtu\.be/|embed/|shorts/|live/)([A-Za-z0-9_-]{11})", url)
    if match:
        return match.group(1)

    raise ValueError("не удалось извлечь video id из youtube_url")


def segment_value(segment: object, key: str, default: object = "") -> object:
    if isinstance(segment, dict):
        return segment.get(key, default)
    return getattr(segment, key, default)


def normalize_segments(transcript: object) -> list[dict[str, object]]:
    normalized: list[dict[str, object]] = []
    for segment in transcript:  # type: ignore[operator]
        text = str(segment_value(segment, "text", "")).replace("\n", " ").strip()
        if not text:
            continue
        normalized.append(
            {
                "text": text,
                "start": float(segment_value(segment, "start", 0.0) or 0.0),
                "duration": float(segment_value(segment, "duration", 0.0) or 0.0),
            }
        )
    return normalized


def fetch_with_youtube_transcript_api(
    video_id: str, languages: tuple[str, ...]
) -> tuple[str, list[dict[str, object]]]:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Библиотека youtube-transcript-api не установлена. "
            "Установи ее командой: python -m pip install youtube-transcript-api"
        ) from exc

    errors: list[str] = []

    if hasattr(YouTubeTranscriptApi, "get_transcript"):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(
                video_id, languages=list(languages)
            )
            return "youtube-transcript-api:get_transcript", normalize_segments(transcript)
        except Exception as exc:  # noqa: BLE001 - выводим понятную ошибку пользователю
            errors.append(f"get_transcript: {exc}")

    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=list(languages))
        return "youtube-transcript-api:fetch", normalize_segments(transcript)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"fetch: {exc}")

    if hasattr(YouTubeTranscriptApi, "list_transcripts"):
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_transcript(list(languages))
            return "youtube-transcript-api:list_transcripts", normalize_segments(
                transcript.fetch()
            )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"list_transcripts: {exc}")

    raise RuntimeError(
        "Не удалось получить транскрипт через youtube-transcript-api. "
        + " | ".join(errors)
    )


def format_time(seconds: float) -> str:
    total = max(0, int(round(seconds)))
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def quote_metadata(value: object) -> str:
    text = str(value or "").replace('"', '\\"')
    return f'"{text}"'


def build_transcript_markdown(
    lecture: dict[str, object], method: str, segments: list[dict[str, object]]
) -> str:
    lines = [
        "---",
        f"lecture_id: {quote_metadata(lecture.get('id'))}",
        f"title: {quote_metadata(lecture.get('title'))}",
        f"youtube_url: {quote_metadata(lecture.get('youtube_url'))}",
        f"fetched_at: {quote_metadata(timestamp())}",
        f"method: {quote_metadata(method)}",
        "---",
        "",
        "# Raw transcript",
        "",
    ]

    for segment in segments:
        start = float(segment.get("start", 0.0) or 0.0)
        text = str(segment.get("text", "")).strip()
        if text:
            lines.append(f"[{format_time(start)}] {text}")

    lines.append("")
    return "\n".join(lines)


def build_unavailable_markdown(lecture: dict[str, object], reason: str) -> str:
    return "\n".join(
        [
            "---",
            f"lecture_id: {quote_metadata(lecture.get('id'))}",
            f"title: {quote_metadata(lecture.get('title'))}",
            f"youtube_url: {quote_metadata(lecture.get('youtube_url'))}",
            f"fetched_at: {quote_metadata(timestamp())}",
            'method: "not-fetched"',
            "---",
            "",
            "# Raw transcript",
            "",
            "[транскрипт не удалось получить автоматически — вставить вручную]",
            "",
            f"Причина: {reason}",
            "",
        ]
    )


def can_replace_raw(path: Path, overwrite: bool) -> bool:
    if overwrite or not path.exists():
        return True
    text = path.read_text(encoding="utf-8", errors="replace")
    return any(marker in text for marker in RAW_PLACEHOLDERS)


def write_raw_transcript(path: Path, content: str, overwrite: bool) -> bool:
    if not can_replace_raw(path, overwrite):
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def process_lecture(
    lecture: dict[str, object], languages: tuple[str, ...], overwrite: bool
) -> bool:
    lecture_id = str(lecture.get("id") or "").strip()
    if not lecture_id:
        print("[WARN] Пропущена лекция без id")
        return False

    output_path = PROJECT_ROOT / "sources" / lecture_id / "transcript.raw.md"
    try:
        video_id = extract_video_id(str(lecture.get("youtube_url") or ""))
        method, segments = fetch_with_youtube_transcript_api(video_id, languages)
        if not segments:
            raise RuntimeError("получен пустой транскрипт")

        content = build_transcript_markdown(lecture, method, segments)
        if write_raw_transcript(output_path, content, overwrite):
            append_log(lecture_id, "OK", f"Транскрипт сохранен в `{output_path}`.")
            print(f"[OK] {lecture_id}: транскрипт сохранен")
        else:
            append_log(
                lecture_id,
                "SKIP",
                "`transcript.raw.md` уже содержит ручной или непустой текст. "
                "Файл не перезаписан. Используй --overwrite, если это нужно.",
            )
            print(f"[SKIP] {lecture_id}: transcript.raw.md не перезаписан")
        return True
    except Exception as exc:  # noqa: BLE001
        reason = str(exc)
        content = build_unavailable_markdown(lecture, reason)
        wrote = write_raw_transcript(output_path, content, overwrite)
        append_log(lecture_id, "ERROR", reason)
        if wrote:
            print(f"[WARN] {lecture_id}: транскрипт не получен, создана пометка")
        else:
            print(f"[WARN] {lecture_id}: транскрипт не получен, существующий файл сохранен")
        return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Получить YouTube-транскрипты для лекций из lectures.yaml."
    )
    parser.add_argument(
        "--lecture",
        action="append",
        help="Обработать только указанную лекцию. Можно передать несколько раз.",
    )
    parser.add_argument(
        "--languages",
        default=",".join(DEFAULT_LANGUAGES),
        help="Список языков субтитров через запятую.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Перезаписывать существующий transcript.raw.md.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.lecture or [])
    languages = tuple(lang.strip() for lang in args.languages.split(",") if lang.strip())

    try:
        lectures = load_lectures()
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] Не удалось прочитать lectures.yaml: {exc}", file=sys.stderr)
        return 2

    if selected:
        known_ids = {str(lecture.get("id") or "") for lecture in lectures}
        missing = sorted(selected - known_ids)
        for lecture_id in missing:
            print(f"[WARN] Лекция `{lecture_id}` не найдена в lectures.yaml")

    processed = 0
    failed = 0
    for lecture in lectures:
        lecture_id = str(lecture.get("id") or "")
        if selected and lecture_id not in selected:
            continue
        processed += 1
        if not process_lecture(lecture, languages, args.overwrite):
            failed += 1

    print(f"[DONE] обработано: {processed}, с ошибками: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
