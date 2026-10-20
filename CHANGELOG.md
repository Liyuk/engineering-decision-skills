# Changelog

## Unreleased

- Added weekly Dependabot checks for GitHub Actions, the only package ecosystem in the repository. Minor and patch updates are grouped, and open pull requests are limited to five.
- Split the user-facing catalog into an English `README.md` and a Chinese `README.zh-CN.md`. Each file is single-language, the section structure matches, and each links to the other at the top.
- Tightened each skill description and in-skill routing so a task that belongs to a neighboring skill is named explicitly.
- Aligned `eng-reporting` rewrite examples and templates with the evidence boundary: clearer wording may restate sourced facts only.
- Linked the `tech-review` decision-structure reference from its entrypoint.
- Copied the evidence contract into every skill package with `scripts/sync_skill_contract.py`. The canonical file stays in `agent/`; validation fails when a copy drifts or a skill links outside its package.
- Recorded [ADR 0004](agent/adr/0004-management-retro-fifth-skill.md): `management-retro` is the fifth skill, superseding the candidate status in ADR 0002.
- Validation now requires `license: MIT`, a non-empty description, and a link from each skill entrypoint to its local references and assets.
- Added three routing-boundary eval prompts (`route-new-roadmap-out`, `route-existing-proposal-review-out`, `route-proposal-review-out`). They are unscored scenario checks. The inventory is 42 prompts.
- Added `management-retro` as a fifth independently installable skill for evidence-bounded learning from completed engineering work.
- Added a concise, scope-qualified methods reference for `tech-review`.
- Added three public-source case reports showing the distinct output of each skill for technical managers and senior Tech Leads.
- Clarified the collection as five task-focused capabilities drawn from frontline technical-manager and senior Tech Lead work.
- The current working tree contains 42 scenario prompts across the five skills; these are exploratory evaluation cases, not a general efficacy claim.
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
