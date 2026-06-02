#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+$", "", line) for line in text.split("\n")]
    normalized = "\n".join(lines)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Консервативно нормализовать пробелы и пустые строки в Markdown-тексте."
    )
    parser.add_argument("input", help="Входной файл")
    parser.add_argument("output", help="Выходной файл")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Разрешить запись поверх существующего выходного файла.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"[ERROR] Входной файл не найден: {input_path}", file=sys.stderr)
        return 2
    if output_path.exists() and not args.overwrite:
        print(
            f"[ERROR] Выходной файл уже существует: {output_path}. "
            "Используй --overwrite, если нужно перезаписать.",
            file=sys.stderr,
        )
        return 2

    text = input_path.read_text(encoding="utf-8", errors="replace")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(normalize_text(text), encoding="utf-8")
    print(f"[OK] записано: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
