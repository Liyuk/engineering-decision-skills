# Historical records index

This index is for maintainers. It explains what each archive group means and where to find the current source of truth. Historical wording and counts are preserved when they describe an earlier repository state.

## Current source of truth

- User-facing catalog and installation: [`README.md`](../../README.md)
- Current release notes: [`CHANGELOG.md`](../../CHANGELOG.md)
- Shared rules: [`agent/`](../../agent/README.md)
- Installable packages: [`skills/`](../../skills)
- Public examples: [`examples/reports/`](../../examples/reports)

## Archive groups

| Group | Type | Status | Current entry when applicable |
| --- | --- | --- | --- |
| [`research/`](research) | External research, public cases, and method sources | Historical research; source claims are time-bounded | Relevant current method reference under `skills/*/references/` |
| [`evaluations/`](evaluations) | Eval runs, acceptance records, and regression notes | Historical evidence; not a general efficacy claim | Current cases under `skills/*/evals/` and rubric in [`agent/eval-rubric.md`](../../agent/eval-rubric.md) |
| [`decisions/`](decisions) | Historical designs and source-to-skill mappings | Design history; later decisions may supersede it | Current structure in [`agent/README.md`](../../agent/README.md) and package entrypoints |
| [`plans/`](plans) | Implementation plans and execution records | Completed process history | Current files named by the plan |
| [`publication/`](publication) | Blog and project-description drafts | Draft material, not the repository catalog | [`README.md`](../../README.md) |

## Important snapshots

| Record | Date/state | Why it remains useful |
| --- | --- | --- |
| [`2026-09-25-portfolio-acceptance.md`](evaluations/2026-09-25-portfolio-acceptance.md) | Five-skill acceptance snapshot | Records the release boundary and known evidence limits |
| [`skills-portfolio-review.md`](evaluations/skills-portfolio-review.md) | Early portfolio review | Preserves the original positioning and regression observations |
| [`management-retro-evaluation.md`](evaluations/management-retro-evaluation.md) | `management-retro` introduction | Preserves source mapping and matched behavior observations |
| [`writing-to-skills-map.md`](decisions/writing-to-skills-map.md) | Method extraction map | Explains how source writing became package behavior |
| [`2026-09-25-history-and-consistency-design.md`](decisions/2026-09-25-history-and-consistency-design.md) | Current archive reorganization design | Defines the archive taxonomy and consistency checks |
| [`2026-09-25-history-and-consistency.md`](plans/2026-09-25-history-and-consistency.md) | Current archive reorganization plan | Records the implementation and verification steps |

When a historical file mentions four skills or 38 eval prompts, that is an earlier snapshot rather than a current repository count. The current repository inventory is five skills and 39 eval cases.
