#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LECTURES_FILE = PROJECT_ROOT / "lectures.yaml"
GENERATED_MARKER = "<!-- generated-by: scripts/extract_slides.py -->"
SLIDES_PLACEHOLDERS = (
    "[сюда будут добавлены слайды]",
    "[слайды не найдены",
    "[текст слайда не извлечён автоматически]",
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


def quote_metadata(value: object) -> str:
    text = str(value or "").replace('"', '\\"')
    return f'"{text}"'


def project_path(path_value: object) -> Path:
    path = Path(str(path_value or ""))
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def can_replace_slides(path: Path, overwrite: bool) -> bool:
    if overwrite or not path.exists():
        return True
    text = path.read_text(encoding="utf-8", errors="replace")
    return GENERATED_MARKER in text or any(marker in text for marker in SLIDES_PLACEHOLDERS)


def render_with_fitz(
    pdf_path: Path, asset_dir: Path
) -> tuple[list[dict[str, object]], list[Path], str]:
    import fitz  # type: ignore

    doc = fitz.open(pdf_path)
    pages: list[dict[str, object]] = []
    figures: list[Path] = []
    figure_number = 1

    for page_index, page in enumerate(doc, start=1):
        slide_path = asset_dir / f"slide-{page_index:03d}.png"
        matrix = fitz.Matrix(2, 2)
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        pixmap.save(slide_path)

        for image in page.get_images(full=True):
            xref = image[0]
            try:
                image_pixmap = fitz.Pixmap(doc, xref)
                if image_pixmap.width < 24 or image_pixmap.height < 24:
                    continue
                if image_pixmap.n - image_pixmap.alpha > 3:
                    image_pixmap = fitz.Pixmap(fitz.csRGB, image_pixmap)
                figure_path = asset_dir / f"figure-{figure_number:03d}.png"
                image_pixmap.save(figure_path)
                figures.append(figure_path)
                figure_number += 1
            except Exception:  # noqa: BLE001 - фигуры необязательны
                continue

        pages.append(
            {
                "number": page_index,
                "text": page.get_text("text").strip(),
                "image": slide_path,
            }
        )

    return pages, figures, "PyMuPDF"


def extract_text_with_pypdf(pdf_path: Path) -> list[str]:
    try:
        from pypdf import PdfReader  # type: ignore
    except ModuleNotFoundError:
        return []

    reader = PdfReader(str(pdf_path))
    texts: list[str] = []
    for page in reader.pages:
        texts.append((page.extract_text() or "").strip())
    return texts


def render_with_pdftoppm(pdf_path: Path, asset_dir: Path) -> list[Path]:
    if not shutil.which("pdftoppm"):
        return []

    prefix = asset_dir / "_slide"
    command = ["pdftoppm", "-png", "-r", "180", str(pdf_path), str(prefix)]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    rendered = sorted(asset_dir.glob("_slide-*.png"))
    output: list[Path] = []
    for index, path in enumerate(rendered, start=1):
        target = asset_dir / f"slide-{index:03d}.png"
        if target.exists():
            target.unlink()
        path.replace(target)
        output.append(target)
    return output


def extract_pdf_fallback(pdf_path: Path, asset_dir: Path) -> tuple[list[dict[str, object]], list[Path], str]:
    texts = extract_text_with_pypdf(pdf_path)
    images = render_with_pdftoppm(pdf_path, asset_dir)
    page_count = max(len(texts), len(images))
    pages: list[dict[str, object]] = []

    for index in range(1, page_count + 1):
        pages.append(
            {
                "number": index,
                "text": texts[index - 1] if index <= len(texts) else "",
                "image": images[index - 1] if index <= len(images) else None,
            }
        )

    method_parts = []
    if texts:
        method_parts.append("pypdf")
    if images:
        method_parts.append("pdftoppm")
    return pages, [], "+".join(method_parts) if method_parts else "unavailable"


def extract_pdf(pdf_path: Path, asset_dir: Path) -> tuple[list[dict[str, object]], list[Path], str]:
    asset_dir.mkdir(parents=True, exist_ok=True)
    try:
        return render_with_fitz(pdf_path, asset_dir)
    except ModuleNotFoundError:
        return extract_pdf_fallback(pdf_path, asset_dir)
    except Exception:
        fallback_pages, fallback_figures, fallback_method = extract_pdf_fallback(
            pdf_path, asset_dir
        )
        if fallback_pages:
            return fallback_pages, fallback_figures, fallback_method
        raise


def build_missing_slides_markdown(lecture: dict[str, object], reason: str) -> str:
    lecture_id = str(lecture.get("id") or "lecture-XX")
    return "\n".join(
        [
            GENERATED_MARKER,
            "---",
            f"lecture_id: {quote_metadata(lecture_id)}",
            f"title: {quote_metadata(lecture.get('title'))}",
            f"slides_path: {quote_metadata(lecture.get('slides_path'))}",
            f"extracted_at: {quote_metadata(timestamp())}",
            'method: "not-extracted"',
            "---",
            "",
            "# Slides",
            "",
            f"[слайды не найдены или не извлечены автоматически: {reason}]",
            "",
        ]
    )


def build_slides_markdown(
    lecture: dict[str, object],
    pages: list[dict[str, object]],
    figures: list[Path],
    method: str,
) -> str:
    lecture_id = str(lecture.get("id") or "lecture-XX")
    lines = [
        GENERATED_MARKER,
        "---",
        f"lecture_id: {quote_metadata(lecture_id)}",
        f"title: {quote_metadata(lecture.get('title'))}",
        f"slides_path: {quote_metadata(lecture.get('slides_path'))}",
        f"extracted_at: {quote_metadata(timestamp())}",
        f"method: {quote_metadata(method)}",
        "---",
        "",
        f"# Slides — {lecture.get('title') or lecture_id}",
        "",
    ]

    if not pages:
        lines.extend(
            [
                "[текст слайда не извлечён автоматически]",
                "",
                "[страницы слайдов не сохранены как изображения]",
                "",
            ]
        )
        return "\n".join(lines)

    for page in pages:
        number = int(page["number"])
        lines.extend([f"## Слайд {number:03d}", ""])

        image = page.get("image")
        if image:
            lines.extend(
                [
                    f"![Slide {number:03d}](../../assets/{lecture_id}/slide-{number:03d}.png)",
                    "",
                ]
            )
        else:
            lines.extend(["[страница слайда не сохранена как изображение]", ""])

        text = str(page.get("text") or "").strip()
        if text:
            lines.extend([text, ""])
        else:
            lines.extend(["[текст слайда не извлечён автоматически]", ""])

    if figures:
        lines.extend(["## Извлеченные фигуры", ""])
        for index, _figure in enumerate(figures, start=1):
            lines.extend(
                [
                    f"![Figure {index:03d}](../../assets/{lecture_id}/figure-{index:03d}.png)",
                    "",
                ]
            )

    return "\n".join(lines)


def process_lecture(lecture: dict[str, object], overwrite: bool) -> bool:
    lecture_id = str(lecture.get("id") or "").strip()
    if not lecture_id:
        print("[WARN] Пропущена лекция без id")
        return False

    source_dir = PROJECT_ROOT / "sources" / lecture_id
    output_path = source_dir / "slides.md"
    asset_dir = PROJECT_ROOT / "assets" / lecture_id

    if not can_replace_slides(output_path, overwrite):
        append_log(
            lecture_id,
            "SKIP",
            "`slides.md` уже содержит ручной или непустой текст. "
            "Файл не перезаписан. Используй --overwrite, если это нужно.",
        )
        print(f"[SKIP] {lecture_id}: slides.md не перезаписан")
        return True

    slides_path = project_path(lecture.get("slides_path"))
    try:
        if not slides_path.exists():
            raise FileNotFoundError(f"не найден файл слайдов: {slides_path}")
        if slides_path.suffix.lower() != ".pdf":
            raise ValueError("сейчас автоматически поддерживается только PDF")

        pages, figures, method = extract_pdf(slides_path, asset_dir)
        markdown = build_slides_markdown(lecture, pages, figures, method)
        source_dir.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
        append_log(lecture_id, "OK", f"Слайды извлечены методом `{method}`.")
        print(f"[OK] {lecture_id}: слайды извлечены")
        return True
    except Exception as exc:  # noqa: BLE001
        reason = str(exc)
        source_dir.mkdir(parents=True, exist_ok=True)
        output_path.write_text(build_missing_slides_markdown(lecture, reason), encoding="utf-8")
        append_log(lecture_id, "ERROR", reason)
        print(f"[WARN] {lecture_id}: слайды не извлечены, создана пометка")
        return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Извлечь текст и изображения PDF-слайдов из lectures.yaml."
    )
    parser.add_argument(
        "--lecture",
        action="append",
        help="Обработать только указанную лекцию. Можно передать несколько раз.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Перезаписывать существующий sources/lecture-XX/slides.md.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = set(args.lecture or [])

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
        if not process_lecture(lecture, args.overwrite):
            failed += 1

    print(f"[DONE] обработано: {processed}, с ошибками: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
