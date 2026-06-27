# cv2

Working area for targeted CV drafts.

## Current draft

The current draft is a Vinted-focused one-page CV for the Senior Business
Process Architect, AI Automation role:

- `index.html`
- `styles.css`
- `scripts/build_pdf.py`
- `output/pdf/kiril-bekulov-vinted-ai-automation-cv.pdf`
- `assets/research/vinted-cv-concept.png`
- `research/vinted-cv-critique.md`

## Research snapshot

The Vinted role is centered on making marketing workflows ready for autonomous
AI agents: process maps, decision trees, data contracts, fallback loops,
technical briefs, n8n-ready low-code automation, and reusable documentation.

The current Kiril profile has strong alignment through FinTech process rigor,
SQL/VBA operations automation, Blue Prism delivery, custom C#/JS/VB helpers,
quality-control standards, team training, and recent LLM integration into RPA
workflows. Additional strong signals: reusable in-house C# automation-platform
work, BA/PO-adjacent business-analysis support during a resourcing gap, and
outside-work AI practice through a shipped platformer prototype built with
LLM-assisted coding and generative-media workflows.
The strongest next proof to add is one concrete C# platform or LLM/RPA example
with measurable scope and outcome.

## Build PDF

Use the bundled Python/reportlab runtime:

```bash
PYTHONPATH=/Users/kirilbekulov/.cache/codex-runtimes/codex-primary-runtime/dependencies/python \
  /Users/kirilbekulov/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_pdf.py
```

The output is written to `output/pdf/kiril-bekulov-vinted-ai-automation-cv.pdf`.

Resume-building guidance used for this draft:

- Target the exact role rather than sending a master CV.
- Place key job-description language in context, not as a keyword dump.
- Keep conventional section names and reverse-chronological experience.
- Use factual outcomes and numbers where the profile supports them.
- Keep the application export readable without photos, complex graphics, or
  content hidden in images.

## Sources

- LinkedIn job posting: https://lt.linkedin.com/jobs/view/senior-business-process-architect-ai-automation-at-vinted-4431739100
- Vinted Careers: https://careers.vinted.com/
- Vinted About: https://www.vinted.com/about
- Current public CV: https://cv.bekulov.com/
- Harvard resume guide: https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/
- MIT resume guide: https://capd.mit.edu/resources/resumes/
- The Muse ATS guide: https://www.themuse.com/advice/beat-the-robots-how-to-get-your-resume-past-the-system-into-human-hands
