# Next skill capability boundary: portfolio gap and adjacent projects

- Research date: 2026-09-24
- Scope: first-party GitHub repository documentation and skill files for `mattpocock/skills` and `testdouble/han`; local portfolio and source-method materials. External claims below describe published repository scope, not independently verified user outcomes.

## Recommendation

**Prioritize a bounded management-retrospective skill, subject to one design gate:** its trigger should be an explicit request to explain recurring execution/system patterns after a period, project, or incident; its output should be an evidence-labeled set of system judgments, bounded explanatory hypotheses, and follow-up experiments/actions. Do not trigger it for an ordinary status update, a new technical investment/roadmap, measurement validity, or review of a proposed solution. This is the clearest named method in the local source map that is not already operationalized end-to-end: the map says the management retrospective's eight judgments are only partially represented in reporting, and the portfolio review explicitly says it is not a complete workflow.

This is a design recommendation, not a finding that another skill is required. Before implementation, establish whether the eight judgments yield a repeatable output and distinct eval cases; if they collapse into existing planning/review/reporting behavior, keep them as references instead.

## First-party capability facts

### `mattpocock/skills`

The repository describes its skills as small, adaptable, composable practices for real software engineering. Its current README catalogs user-invoked skills for shared domain/context setup, specs, issue triage, tracer-bullet ticket decomposition, implementation, and long-horizon engineering work; model-invoked skills include TDD, debugging, domain modeling, codebase design, and code review. The README also lists general productivity skills such as grilling, handoff, questionnaires, and teaching. These are repo-owner descriptions of intended use, not independent efficacy evidence. ([Repository README](https://github.com/mattpocock/skills/blob/main/README.md))

The specific `to-tickets` boundary is converting an already discussed plan/spec/conversation into dependent tracer-bullet tickets, while `implement` executes specifications or tickets. This makes implementation task decomposition a poor next capability for this portfolio: it would overlap an established coding-agent engineering workflow. ([README skill catalog](https://github.com/mattpocock/skills/blob/main/README.md), [`to-tickets`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md))

### `testdouble/han/han-planning`

Han presents itself as a suite for solo product engineers and small teams, covering planning, implementation, review, architecture, documentation, research, and reporting. Its planning skills include feature specification, implementation planning, phased builds/work items, and iterative plan review. ([Han repository README](https://github.com/testdouble/han))

Han's `iterative-plan-review` starts from an existing plan, stress-tests and edits it in place over bounded passes, and records findings and iteration history in companion artifacts. It explicitly excludes writing a new plan, implementing plan steps, code review, and bug investigation; new feature and implementation plans have separate skills. ([`iterative-plan-review` operator docs](https://github.com/testdouble/han/blob/main/han-planning/docs/skills/iterative-plan-review.md), [`plan-a-feature`](https://github.com/testdouble/han/blob/main/han-planning/skills/plan-a-feature/SKILL.md), [`plan-implementation`](https://github.com/testdouble/han/blob/main/han-planning/skills/plan-implementation/SKILL.md))

Han also has `stakeholder-summary`, which turns an existing feature specification into a plain-language pre-kickoff artifact about customer problem, experience, scope boundaries, and stakeholder questions. That overlaps with generic executive or project-summary writing, so a new capability here must focus on diagnosing completed work and changing management decisions—not rephrasing a plan for stakeholders. ([`stakeholder-summary` docs](https://github.com/testdouble/han/blob/main/han-reporting/docs/skills/stakeholder-summary.md), [`stakeholder-summary` skill](https://github.com/testdouble/han/blob/main/han-reporting/skills/stakeholder-summary/SKILL.md))

Thus a general skill that creates plans, breaks them into implementation tasks, repeatedly edits an existing plan, or summarizes a feature spec for pre-kickoff feedback would collide with Han's published boundaries. A retrospective on system-level execution patterns is a different input and purpose, provided it stays retrospective rather than becoming another plan author/reviewer or generic stakeholder-summary writer.

## Local coverage and candidate gap

Local materials describe four independent workflows at the time of this research: investment choices and roadmaps (`tech-planning`); metric definition/validity and evidence-to-action (`metric-decision`); evidence-based review of an existing proposal (`tech-review`); and audience-specific communication from existing material (`eng-reporting`). The portfolio says they are complementary, not a mandatory sequence. ([portfolio review](../evaluations/skills-portfolio-review.md), [README](../../../README.md), [four skill entrypoints](../../../skills))

The source map names the management-retrospective essay's method as eight judgments—problem, boundaries, alignment, context handoffs, closed loops, capacity, team growth, and retrospective—and says `eng-reporting` initially carries only selected ideas. The portfolio review independently records that it is not a complete dedicated workflow. This is the best-supported candidate gap. ([writing-to-skills map](../decisions/writing-to-skills-map.md), [portfolio review](../evaluations/skills-portfolio-review.md))

The other source-map candidate, AI productivity in complex systems, concerns bottleneck movement, system boundaries, failure ownership, resilience, cost, and attribution. It is potentially distinct from plan creation/review, but current local materials already route metric questions and proposals into existing skills, while Matt's catalog includes codebase architecture/design and engineering analysis. Evidence here is weaker for a discrete trigger/output than for a management retrospective; retain it as a specialist mode or eval topic until cases establish a sharper boundary. ([writing-to-skills map](../decisions/writing-to-skills-map.md), [Matt README](https://github.com/mattpocock/skills/blob/main/README.md))

## Prioritized design direction (recommendation)

1. **Management retrospective (candidate):** Trigger on explicit requests to diagnose recurring system/execution patterns from completed work or a defined period. Output: evidence and uncertainty ledger, judgments across the source method's relevant dimensions, system-level explanations separated from individual blame, and a small set of testable changes with owners only when confirmed. Eval boundary: distinguish source facts from inference, avoid unsupported causal claims, surface cross-team/capacity/feedback-loop causes where supported, and decline to turn a routine update into an audit. Validate the eight-judgment method against multiple contrasting cases before adding a standalone package.
2. **Keep structured decision communication in existing skills:** The source map already routes reader decision, evidence versus assumption, status/blocker/decision/next step to `tech-review` and `eng-reporting`; it does not support a separate generic communication skill.
3. **Keep AI/system productivity as a possible specialist mode:** Promote only if evaluations show a repeatable systems-level diagnosis task that cannot be served by `metric-decision`, `tech-review`, or a bounded retrospective.

## Explicit avoid list

- Do not add general coding-agent workflow, TDD, code review, debugging, codebase architecture, implementation, tracer-bullet ticket creation, or agent-task orchestration; these match Matt's published engineering catalog.
- Do not add plan-from-scratch, implementation-plan authoring, plan decomposition, or iterative in-place plan hardening; Han's planning suite explicitly owns those jobs.
- Do not add a generic stakeholder summary from a feature spec, general project-management, status-reporting, skill-router, or fixed portfolio funnel. Han has a feature-spec stakeholder-summary workflow; this repository already has evidence-based reporting. Existing local skills are intentionally independent, and the portfolio review says to invoke only the workflow that matches the actual task.
- Do not label a retrospective as root-cause proof. Require source attribution and distinguish observations, hypotheses, and proposed experiments, consistent with the repository's evidence contract.

## Sources

- First-party Matt Pocock repository [README](https://github.com/mattpocock/skills/blob/main/README.md) and [`to-tickets` skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md).
- First-party Test Double Han [repository README](https://github.com/testdouble/han), [`iterative-plan-review` operator docs](https://github.com/testdouble/han/blob/main/han-planning/docs/skills/iterative-plan-review.md), [`iterative-plan-review` skill](https://github.com/testdouble/han/blob/main/han-planning/skills/iterative-plan-review/SKILL.md), [`stakeholder-summary` docs](https://github.com/testdouble/han/blob/main/han-reporting/docs/skills/stakeholder-summary.md) and [`stakeholder-summary` skill](https://github.com/testdouble/han/blob/main/han-reporting/skills/stakeholder-summary/SKILL.md), [`plan-a-feature`](https://github.com/testdouble/han/blob/main/han-planning/skills/plan-a-feature/SKILL.md), and [`plan-implementation`](https://github.com/testdouble/han/blob/main/han-planning/skills/plan-implementation/SKILL.md).
- Local evidence: [README](../../../README.md), [skills portfolio review](../evaluations/skills-portfolio-review.md), [writing-to-skills map](../decisions/writing-to-skills-map.md), [tech-planning](../../../skills/tech-planning/SKILL.md), [metric-decision](../../../skills/metric-decision/SKILL.md), [tech-review](../../../skills/tech-review/SKILL.md), [eng-reporting](../../../skills/eng-reporting/SKILL.md), and [shared evidence contract](../../../agent/decision-and-review-contract.md).
