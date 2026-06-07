#!/usr/bin/env bash
# Optional helper: convert selected LaTeX sections to GitHub-flavored Markdown.
# Requires: brew install pandoc
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p generated_markdown
for f in sections/*.tex; do
  base=$(basename "$f" .tex)
  pandoc "$f" -f latex -t gfm -o "generated_markdown/${base}.md"
done
