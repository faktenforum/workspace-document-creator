# Pandoc — Editable Formats

**Use when:** User wants an **editable** document (ODT, DOCX, HTML, EPUB), not PDF. Write Markdown and convert with Pandoc.

## Commands

```bash
# Markdown → ODT (recommended open format)
pandoc document.md -o document.odt

# Markdown → DOCX
pandoc document.md -o document.docx

# Markdown → HTML (standalone)
pandoc document.md -s -o document.html

# Markdown → EPUB
pandoc document.md -o document.epub

# With custom styling (reference document)
pandoc document.md --reference-doc=template.odt -o document.odt
```

**Format preference:** Prefer ODT as the recommended open editable format. Offer DOCX for Microsoft Office users.

## Useful Options

```bash
# Table of contents
pandoc document.md --toc -o document.odt

# TOC depth (default 3)
pandoc document.md --toc --toc-depth=2 -o document.odt

# Metadata
pandoc document.md -o document.pdf --metadata title="My Document" --metadata author="Name"

# GitHub Flavored Markdown input
pandoc document.md -f gfm -o document.odt
```

## Customizing Output

- **ODT/DOCX:** Use `--reference-doc=template.odt` to apply styles from an existing document
- **HTML:** Use `--css=style.css` for custom styling
- **EPUB:** Use `--css=epub.css` and `--metadata cover-image:cover.png`

## Advanced Customization

- **ODT/DOCX:** `--reference-doc` for styles
- **EPUB:** Custom `--css`, `--metadata cover-image`, `--top-level-division=chapter`
- **PDF (LaTeX):** Chapter breaks, syntax highlighting, bullet styling — [learnbyexample](https://learnbyexample.github.io/customizing-pandoc/)

## References

- [Pandoc User's Guide](https://pandoc.org/MANUAL.html)
- [Customizing Pandoc (learnbyexample)](https://learnbyexample.github.io/customizing-pandoc/)
