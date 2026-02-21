# Document Creation

## Workflow

1. **Clarify** — type (letter, report, invoice, CV...), content, style, language.
2. **Choose format** — see decision tree below.
3. **Write source** — `.typ` for native PDF, `.md` for Pandoc-based conversion.
4. **Compile** — `typst compile`, `pandoc`, or `uv run examples/scripts/md2pdf.py`.
5. **Return** — `read_workspace_file` (PDF preview) or `create_download_link`.

---

## Decision Tree

| User wants | Source format | Use | Prompt |
|------------|----------------|-----|--------|
| PDF, full control | Typst (`.typ`) | `typst compile` | [instructions-typst.md](instructions-typst.md) |
| PDF from Markdown | Markdown (`.md`) | `pandoc --pdf-engine=typst` | [instructions-pandoc-typst.md](instructions-pandoc-typst.md) |
| Editable (ODT, DOCX, HTML, EPUB) | Markdown (`.md`) | `pandoc` | [instructions-pandoc.md](instructions-pandoc.md) |
| Python automation | Any | `uv run` + pypandoc/subprocess | [instructions-python.md](instructions-python.md) |

---

## uv — Python Scripts

**All Python scripts MUST use uv** to avoid dependency conflicts across projects. See [instructions-uv.md](instructions-uv.md).

```bash
# Run script (deps from inline metadata)
uv run examples/scripts/md2pdf.py input.md output.pdf

# Never: pip install + python script.py
```

---

## Constraints

- **PDF** — use Typst (`typst compile`) or Pandoc+Typst. Do not use LaTeX or wkhtmltopdf.
- **Editable** — use Pandoc for ODT/DOCX/HTML/EPUB.
- **Fonts** — DejaVu Sans, DejaVu Serif, DejaVu Sans Mono. Check with `typst fonts`.
- **Images** — save in workspace first; reference by relative path.
- **Output** — save in workspace; return via `read_workspace_file` or `create_download_link`.
- **Language** — match user's language in content; keep code/comments in English.
- **Documentation** — https://typst.app/docs/ when Typst syntax is unclear.

---

## Prompt Index

| File | Use case |
|------|----------|
| [instructions-typst.md](instructions-typst.md) | Native Typst PDF (letter, report, invoice) |
| [instructions-pandoc.md](instructions-pandoc.md) | Pandoc → ODT, DOCX, HTML, EPUB |
| [instructions-pandoc-typst.md](instructions-pandoc-typst.md) | Pandoc + Typst → PDF from Markdown |
| [instructions-python.md](instructions-python.md) | Python automation (pypandoc, subprocess) |
| [instructions-uv.md](instructions-uv.md) | uv usage for dependency isolation |

## External References

- [Typst docs](https://typst.app/docs/) — syntax, functions, reference
- [Pandoc User's Guide](https://pandoc.org/MANUAL.html)
- [Pandoc + Typst (Imaginary Text)](https://imaginarytext.ca/posts/2025/typst-templates-for-pandoc/)
- [Customizing Pandoc (learnbyexample)](https://learnbyexample.github.io/customizing-pandoc/)
- [Pandoc Python Library](https://boisgera.github.io/pandoc/examples/) — AST manipulation
- [uv docs](https://docs.astral.sh/uv/)
