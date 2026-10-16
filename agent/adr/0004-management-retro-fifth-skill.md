# ADR 0004: Accept management-retro as the fifth skill

- Status: Accepted
- Date: 2026-09-25

## Context

[ADR 0002](0002-short-invocations-and-metric-decision-skill.md) kept a management retrospective as a mode or candidate until it showed a trigger and output distinct from planning, review, metric decisions, and reporting. That ADR also deferred a standalone AI-value skill until there were enough representative cases.

By 2026-09-25 the repository had added `skills/management-retro/` as its own entrypoint, with the eight-judgment reference and evaluation cases. Those cases cover a normal retrospective, missing information, conflicting information, and routing boundaries: compressing an already confirmed summary stays with `eng-reporting`, and checking whether a metric change is real stays with `metric-decision`. The README and the portfolio acceptance already describe five skills. This record was written on 2026-10-16 so the candidate sentence in ADR 0002 is not the latest word.

## Decision

- `management-retro` is an independently installable fifth skill. It is not a mode of `eng-reporting` or `tech-review`, and it is not a required step after the other skills.
- Use it to learn from completed engineering work, a delivery period, or an incident: separate sequence from evidenced cause, and choose what to keep, change, or stop next time.
- Do not use it to reformat an already settled summary (`eng-reporting`), validate a metric (`metric-decision`), review a proposal that has not been carried out (`tech-review`), or choose future capacity (`tech-planning`).
- Do not add a standalone AI-value skill from this decision. ADR 0002 still defers that until there are enough representative cases.
- Keep the skill inside frontline engineering judgment. It does not become a people-management, performance, or team-health assistant.

## Consequences

- Install and invoke `management-retro` on its own. Its package contains the entrypoint, reference, evaluations, license, and the synced evidence-contract copy.
- ADR 0002 remains the record of the earlier candidate boundary. The current catalog is this ADR together with the five skill entrypoints and [`README.md`](../../README.md).
- Using the skill does not require the other four skills to be installed or run in sequence.
