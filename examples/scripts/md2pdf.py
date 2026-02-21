#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pypandoc"]
# ///

"""
Convert Markdown to PDF using Pandoc with Typst as PDF engine.
Usage: uv run md2pdf.py input.md [output.pdf]
"""

import sys
from pathlib import Path

import pypandoc


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run md2pdf.py input.md [output.pdf]", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Error: {input_path} not found", file=sys.stderr)
        sys.exit(1)

    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix(".pdf")

    pypandoc.convert_file(
        str(input_path),
        "pdf",
        outputfile=str(output_path),
        extra_args=["--pdf-engine=typst"],
    )
    print(f"Created {output_path}")


if __name__ == "__main__":
    main()
