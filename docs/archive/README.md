# Maintainer archive

This directory keeps historical research, evaluation records, project-description drafts, and design/implementation notes for provenance. These files are not part of the installable skill packages and are not the user-facing catalog. Git commit history remains unchanged.

- [`index.md`](index.md) — inventory of archived records, their status, and current replacements.
- `publication/` — project-description and blog drafts.
- `evaluations/` — behavior evaluations, acceptance records, and regression checks.
- `decisions/` — historical design decisions and source-to-skill mappings.
- `plans/` — historical implementation plans and execution records.
- `research/` — competitor, demand, public-case, and method-source research.

Installable user packages live only under `skills/<skill-name>/`. The maintained method references required by an individual skill remain inside that skill's own directory.

Files in this directory are snapshots. When a snapshot disagrees with the current repository, follow its date and status in [`index.md`](index.md), then use the linked current entry for present behavior.
