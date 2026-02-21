# Document Creator Workspace

Persistent workspace repository for the **Document Creator** agent in [LibreChat](https://github.com/faktenforum/ai-chat-interface) with the [mcp-linux](https://github.com/faktenforum/ai-chat-interface/tree/main/packages/mcp-linux) server. The agent checks out this repo via MCP and uses it as a workspace with prompts, examples, and scripts for document creation.

## Structure

| Path | Description |
|------|-------------|
| `.mcp-linux/prompts/` | Agent prompts: Typst, Pandoc, Python, uv — split by use case |
| `examples/scripts/` | Python conversion scripts (md2pdf, md2odt) using uv |
| `.mcp-linux/plan.json` | Workspace plan (resets on main branch checkout) |

## Prompts (agent audience)

- **document-creation.md** — Main index, workflow, decision tree
- **document-creation-typst.md** — Native Typst PDF (letter, report, invoice)
- **document-creation-pandoc.md** — Pandoc → ODT, DOCX, HTML, EPUB
- **document-creation-pandoc-typst.md** — Pandoc + Typst → PDF from Markdown
- **document-creation-python.md** — Python automation (pypandoc, uv)
- **document-creation-uv.md** — uv for dependency isolation

## Usage (contributors)

- Agents clone this repo as a workspace and work on task branches. Main branch stays clean.
- Python scripts use [uv](https://docs.astral.sh/uv/) — run with `uv run examples/scripts/md2pdf.py input.md output.pdf`.
