# Python + Pandoc — Document Automation

**Use when:** Automating document conversion (batch, CI, dynamic content). **Always use uv** — see [document-creation-uv.md](document-creation-uv.md).

## subprocess (no extra deps)

```python
import subprocess

def convert_md_to_pdf(input_file: str, output_file: str) -> None:
    subprocess.run(["pandoc", input_file, "-o", output_file], check=True)

convert_md_to_pdf("input.md", "output.pdf")
```

Run with: `uv run script.py` (no deps needed).

## pypandoc (Python wrapper)

```python
# /// script
# dependencies = ["pypandoc"]
# ///

import pypandoc

output = pypandoc.convert_file("input.md", "pdf", outputfile="output.pdf")
assert output == ""
```

Run with: `uv run script.py` or `uv add --script script.py pypandoc` first.

## Common Patterns

```python
# Metadata
pypandoc.convert_file(
    "input.md", "pdf",
    outputfile="output.pdf",
    extra_args=["--metadata", "title=My Document", "--metadata", "author=Name"]
)

# Table of contents
pypandoc.convert_file(
    "input.md", "pdf",
    outputfile="output.pdf",
    extra_args=["--toc"]
)

# Typst as PDF engine
pypandoc.convert_file(
    "input.md", "pdf",
    outputfile="output.pdf",
    extra_args=["--pdf-engine=typst"]
)
```

## Pandoc Python Library (AST manipulation)

For transforming document structure (not just conversion), use the `pandoc` library:

```python
# /// script
# dependencies = ["pandoc"]
# ///

import pandoc
from pandoc.types import *

doc = pandoc.read("Hello **world**!")
# Transform AST, then:
pandoc.write(doc, format="markdown")
```

**Reference:** [Pandoc Python Library Examples](https://boisgera.github.io/pandoc/examples/)

## Example Scripts

See `examples/scripts/` for ready-to-use uv-based scripts:
- `md2pdf.py` — Markdown → PDF (Pandoc + Typst)
- `md2odt.py` — Markdown → ODT
