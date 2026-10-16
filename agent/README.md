# Shared skill standards

This directory is the canonical home for rules used by more than one skill. Skill files should point here instead of copying shared policy. Skill-specific workflow details stay next to their `SKILL.md`.

The current collection is five independently installable skills: `tech-planning`, `tech-review`, `metric-decision`, `management-retro`, and `eng-reporting`. [ADR 0001](adr/0001-collection-layout.md) and [ADR 0002](adr/0002-short-invocations-and-metric-decision-skill.md) record earlier boundaries, including when a retrospective skill was still a candidate. Use the skill entrypoints and [`README.md`](../README.md) for the current catalog.

| Document | Owns |
| --- | --- |
| `decision-and-review-contract.md` | Evidence states, bounded conclusions, review findings, and shared handoff fields |
| `eval-rubric.md` | Shared behavioral evaluation dimensions and pass thresholds for every skill |
| `adr/` | Accepted decisions about the repository's skill architecture and maintenance model |

If a rule is needed by only one skill, keep it in that skill's references. Add a shared document only when more than one skill needs the same contract.
