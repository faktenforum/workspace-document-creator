# Document Conversion Scripts

Python scripts for document conversion. **All scripts use uv** for dependency isolation.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed
- [Pandoc](https://pandoc.org/) and [Typst](https://typst.app/) on PATH (for PDF output)

## Usage

```bash
# From workspace root
uv run examples/scripts/md2pdf.py document.md document.pdf
uv run examples/scripts/md2odt.py document.md document.odt
```

## Scripts

| Script | Purpose |
|--------|---------|
| `md2pdf.py` | Markdown → PDF (Pandoc + Typst) |
| `md2odt.py` | Markdown → ODT |

Dependencies are declared via inline metadata; no `pip install` required.
