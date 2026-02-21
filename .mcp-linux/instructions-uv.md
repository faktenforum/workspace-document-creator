# uv — Python Script Dependency Management

**Audience:** Document Creator Agent. **Purpose:** Avoid dependency conflicts when the agent works on multiple projects. All Python scripts in this workspace MUST use uv.

## Why uv

- **Isolated environments per script** — no conflicts between pypandoc, requests, etc. across tasks
- **No manual venv** — `uv run` creates ephemeral envs on demand
- **Inline metadata** — dependencies declared in the script; no global `requirements.txt`
- **Fast** — 10–100x faster than pip

**Reference:** https://docs.astral.sh/uv/

## Running Scripts

```bash
# Script without dependencies
uv run script.py

# Script with inline metadata (preferred)
uv run md2pdf.py input.md output.pdf

# One-off dependency (no inline metadata)
uv run --with pypandoc convert.py input.md output.pdf

# In a project dir: skip project deps for standalone script
uv run --no-project script.py
```

## Creating Scripts with Inline Metadata

Use `uv add --script` to declare dependencies in the script:

```bash
uv add --script md2pdf.py pypandoc
```

This adds a TOML block at the top:

```python
# /// script
# dependencies = [
#   "pypandoc",
# ]
# ///

import pypandoc
# ...
```

**Important:** With inline metadata, the script's dependencies are isolated — even in a project with `pyproject.toml`, the project's deps are ignored. No `--no-project` needed.

## Quick Reference

| Task | Command |
|------|---------|
| Run script | `uv run script.py` |
| Add dep to script | `uv run uv add --script script.py pkg` |
| Lock script deps | `uv lock --script script.py` |
| Run with extra dep (one-off) | `uv run --with pkg script.py` |
| Use specific Python | `uv run --python 3.12 script.py` |

## Agent Rules

1. **Always use `uv run`** for Python scripts — never `python script.py` or `pip install` + run
2. **Prefer inline metadata** — add deps with `uv add --script script.py pkg`
3. **No global installs** — do not `pip install` in the workspace; each script manages its own deps
4. **New scripts** — use `uv add --script <file> <deps>` before first run
