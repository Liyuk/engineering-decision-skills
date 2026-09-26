# `tech-review` method-source retrieval check

- **Date:** 2026-09-25
- **Type:** One-run documentation retrieval check, not a general efficacy study.

## Prompt

The evaluator asked for sources behind item-by-item coverage, evidence-bounded conclusions, allowing a pass when no blockers are supported, and findings that include basis, impact, and action. It explicitly restricted citations to sources present in the skill package and required the answer to state what those sources cannot establish.

## Baseline without the source reference

The agent found only examples and eval expectations inside the skill package. It correctly declined to invent citations, but could not retrieve external method sources because none were present in the package.

## Guided run with the source reference

With [`method-sources.md`](../../../skills/tech-review/references/method-sources.md) available, the agent retrieved NASA NPR 7150.2D, Google code-review guidance, Fagan's inspection paper, and Gerrit's design-doc guidance. It described bounded support and noted that the sources do not define this skill's exact fields, universal pass rules, status/severity scales, or effectiveness.

## Result and limit

The guided run met the retrieval case's criteria: sources were present in the package, claims were qualified by context, and it did not claim the sources prove skill efficacy. The observed difference is source discoverability for this one prompt; it is not evidence that the skill improves technical-review quality across users or models.
