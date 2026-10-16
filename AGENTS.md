# Repository guidance

This repository is a collection of independently installable skills for frontline engineering analysis and decision support: technical planning, technical review, metric decisions, project retrospectives, and evidence-based reporting. Keep it focused on bounded engineering work; it is not a general people-management or team-health assistant.

## Source of truth

- `README.md` (English) and `README.zh-CN.md` (Chinese) are the user-facing catalogs and installation guides. Keep the same section structure in both, and update them in the same change. `README.md` is the default GitHub landing page. Keep internal research and process history out of these files.
- `agent/` owns rules shared across multiple skills. Keep each shared rule in one canonical document. Skills operationalize those rules. A skill package must not link outside its own directory.
- The evidence contract's canonical file is `agent/decision-and-review-contract.md`. Because a copied skill cannot read that path, `python3 scripts/sync_skill_contract.py` writes an identical copy to `skills/<skill-name>/references/decision-and-review-contract.md`. Edit the canonical file and run the script in the same change. Do not edit the copies by hand.
- `skills/<skill-name>/SKILL.md` is the standalone entrypoint. Keep skill-specific references, templates, eval cases, scripts, and the synced contract copy with that skill so it can be installed independently.
- `docs/archive/` stores internal research, evaluations, blog drafts, and design/implementation history. Preserve Git history; do not expose these records as the main user entry point.

## Change rules

- Preserve independent skill boundaries; do not create a root router skill unless it adds a distinct, useful invocation path.
- When a shared rule changes, update its canonical `agent/` document and every affected skill in the same change. For the evidence contract, update the canonical file and run `python3 scripts/sync_skill_contract.py` instead of editing five copies.
- When skill behavior changes, update or add eval cases that exercise the behavior and its boundary conditions.
- Distinguish user-provided facts, sourced facts, measurements, estimates, inferences, assumptions, and unknowns. Never invent metrics, citations, or review findings to satisfy an output template.
- Keep review and revision as separate actions unless the user explicitly requests both.
- The root `LICENSE` is the canonical repository license. Each independently installable skill declares the same SPDX identifier in its frontmatter so the license remains visible when copied alone. Document any explicitly approved exception in both the skill and README.
- Run `python3 scripts/validate_repo.py` after moving skill files or changing local references.
