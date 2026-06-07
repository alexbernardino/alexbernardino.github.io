# Modular LaTeX CV

This folder contains a modular LaTeX version of `CurriculumVitae34.docx`.

## Structure

- `main.tex` — master file; compiles the full CV.
- `sections/` — one `.tex` file per major CV section or appendix.
- `media/` — images extracted from the Word document.
- `scripts/build_pdf.sh` — compiles the CV PDF with `xelatex`.
- `scripts/build_site_pages.sh` — optional Pandoc helper to convert sections to Markdown.

## Compile the CV

```bash
cd cv_modular_latex
./scripts/build_pdf.sh
```

or manually:

```bash
xelatex main.tex
xelatex main.tex
```

## Reuse sections for the website

You can convert individual section files to Markdown with Pandoc:

```bash
pandoc sections/09-project-grants.tex -f latex -t gfm -o ../projects.md
pandoc sections/08-publications.tex -f latex -t gfm -o ../publications_from_cv.md
```

The generated Markdown should usually be reviewed manually before publishing.

## Section files

- `sections/01-summary.tex` — Summary
- `sections/02-highlights.tex` — Highlights
- `sections/03-presentation.tex` — Presentation
- `sections/04-pedagogical-activity.tex` — Pedagogical Activity
- `sections/05-scientific-activity.tex` — Scientific Activity
- `sections/06-external-engagement.tex` — External Engagement
- `sections/07-academic-and-research-service.tex` — Academic and Research Service
- `sections/08-teaching-activities.tex` — Teaching Activities
- `sections/09-supervision-activities.tex` — Supervision Activities
- `sections/10-publications.tex` — Publications
- `sections/11-impact-factors.tex` — Impact Factors
- `sections/12-project-grants.tex` — Project Grants
- `sections/13-recognition-and-visibility.tex` — Recognition And Visibility
- `sections/14-external-engagement.tex` — External Engagement
- `sections/15-academic-and-research-service.tex` — Academic and Research Service
