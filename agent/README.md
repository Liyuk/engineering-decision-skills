# Shared skill standards

This directory is the canonical home for rules used by more than one skill. Skill-specific workflow details stay next to their `SKILL.md`.

The evidence contract is the shared document that must also live inside every skill package. A copied skill cannot follow a link outside its own directory, so [`scripts/sync_skill_contract.py`](../scripts/sync_skill_contract.py) writes an identical copy to `skills/<skill>/references/decision-and-review-contract.md`. Edit the canonical file here, then run that script. Do not edit the package copies by hand. The evaluation rubric stays only in this directory; skills do not need it at runtime.

The current collection is five independently installable skills: `tech-planning`, `tech-review`, `metric-decision`, `management-retro`, and `eng-reporting`. [ADR 0001](adr/0001-collection-layout.md) and [ADR 0002](adr/0002-short-invocations-and-metric-decision-skill.md) record earlier boundaries. ADR 0002 kept a retrospective skill as a candidate; [ADR 0004](adr/0004-management-retro-fifth-skill.md) accepted `management-retro` as the fifth skill. [ADR 0003](adr/0003-repository-wide-mit-license.md) applies the MIT License to the repository and every skill. Use the skill entrypoints and [`README.md`](../README.md) for the current catalog.

| Document | Owns |
| --- | --- |
| `decision-and-review-contract.md` | Canonical evidence states, bounded conclusions, review findings, and shared handoff fields. Identical copies are synced into each skill package. |
| `eval-rubric.md` | Shared behavioral evaluation dimensions and pass thresholds for every skill |
| [`adr/0001-collection-layout.md`](adr/0001-collection-layout.md) | Skill collection layout and independent install paths |
| [`adr/0002-short-invocations-and-metric-decision-skill.md`](adr/0002-short-invocations-and-metric-decision-skill.md) | Short invocation names and `metric-decision`; retrospective skill was still a candidate |
| [`adr/0003-repository-wide-mit-license.md`](adr/0003-repository-wide-mit-license.md) | MIT License for the repository and every skill |
| [`adr/0004-management-retro-fifth-skill.md`](adr/0004-management-retro-fifth-skill.md) | `management-retro` accepted as the fifth skill |

If a rule is needed by only one skill, keep it in that skill's references. Add a shared document only when more than one skill needs the same contract.
