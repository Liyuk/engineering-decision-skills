# Changelog

## Unreleased

- Added `management-retro` as a fifth independently installable skill for evidence-bounded learning from completed engineering work.
- Added a concise, scope-qualified methods reference for `tech-review`.
- Added three public-source case reports showing the distinct output of each skill for technical managers and senior Tech Leads.
- Clarified the collection as five task-focused capabilities drawn from frontline technical-manager and senior Tech Lead work.
- The current working tree contains 39 scenario prompts across the five skills; these are exploratory evaluation cases, not a general efficacy claim.
- Reworked the README around decision pressure and added a before/after example showing how the skills bound an overconfident metric conclusion.
- Added an English project summary, five-minute quick start, contribution guide, and GitHub Actions repository validation.

## v1.0.0 — 2026-09-24

Initial public release of four independently installable skills:

- `tech-planning` — technical investment choices and roadmaps.
- `tech-review` — evidence-based review of existing proposals.
- `metric-decision` — metric definition, validation, and decision follow-through.
- `eng-reporting` — evidence-preserving engineering management updates.

The collection uses the MIT License. Each skill includes its own entrypoint, focused references, and scenario evaluations where applicable. The planning workflow distinguishes confirmed owners from suggested or unknown responsibility assignments.

### Verification

- `python3 scripts/validate_repo.py` passed.
- Vercel Skills CLI copied all four skills from the public repository into a temporary Codex skills directory.
- The repository contains 29 scenario prompts. A single-run, rubric-scored behavior spot check covered 12 prompts; one planning attribution issue was corrected and two focused reruns scored 10/10. This is exploratory evaluation, not evidence of general improvement across models or tasks.
- Installation and behavior were smoke-tested with Codex. Claude Code and other agent hosts have not been directly validated.

No npm package is published; install from GitHub with the Skills CLI.
