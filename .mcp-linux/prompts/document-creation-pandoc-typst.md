# Pandoc + Typst — PDF from Markdown

**Use when:** User provides or prefers Markdown; output should be PDF. Pandoc converts Markdown to Typst, then Typst compiles to PDF.

## Basic Command

```bash
pandoc document.md --pdf-engine=typst -o document.pdf
```

## With Custom Typst Template

Pandoc can use a custom Typst template. Export the default, then customize:

```bash
# Export default Typst template
pandoc -D typst > default.typ

# Use custom template
pandoc document.md --pdf-engine=typst --template=article.typ -o document.pdf
```

**Newer Pandoc (2025):** Pass template via variable:

```bash
pandoc document.md -f markdown --wrap=none -t pdf --pdf-engine=typst \
  -V template=article.typ -o document.pdf
```

## Markdown Metadata

Typst expects title, author, date. Add YAML frontmatter:

```yaml
---
title: "Document Title"
author: "Author Name"
date: 2026-02-21
---
```

## References

- [Imaginary Text: Pandoc + Typst Tutorial](https://imaginarytext.ca/posts/2024/pandoc-typst-tutorial/)
- [Imaginary Text: New Typst Template for Pandoc (2025)](https://imaginarytext.ca/posts/2025/typst-templates-for-pandoc/)
- [Quarto Typst Format](https://quarto.org/docs/output-formats/typst.html) — options for papersize, margin, columns, toc, section-numbering
