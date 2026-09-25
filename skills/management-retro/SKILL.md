---
name: management-retro
description: Use when a user asks to learn from completed engineering work, a project period, or an incident by examining recurring execution and system patterns and choosing what to keep, change, or stop next time.
license: MIT
compatibility: Works in Agent Skills environments that can read the supplied project notes, records, and references. It structures provided evidence and cannot independently verify unavailable organizational data.
metadata:
  author: Liyuk
  version: "1.0.0"
  domain: engineering-management-retrospective
---

# Management Retrospective

Help a team make a better next decision from completed work. Treat a retrospective as learning about the system of work, not a blame exercise, status report, or control process. Preserve the principle **Context, not control**: clarify outcomes, evidence, boundaries, and decision rights so people closest to the work can act.

## Use this skill when

- The user wants to analyze a completed project, delivery period, recurring execution pattern, or incident and decide what to keep, change, or stop.
- They ask why work diverged from its goal, where handoffs or decisions failed, or what learning should shape the next similar case.

Do not force a full retrospective when the user only wants established material summarized or rewritten; use `eng-reporting`. When metric definition or data validity is the main question, use `metric-decision`. For review of a proposal before work begins, use `tech-review`; for a future investment plan or roadmap, use `tech-planning`. A retrospective may hand off to these skills only when the user needs that distinct deliverable. Do not turn findings into implementation, tickets, or an execution plan unless asked.

## Method

1. **Set the question and boundary.** Identify the work or period, intended outcome, comparison/baseline if available, audience, and decision the retrospective should inform. Keep the scope proportionate; ask only for information that could change the conclusion. If an incident is active, prioritize prevention, detection, containment, and repair before retrospective analysis.
2. **Sort facts from explanations.** For each material claim, retain its source, scope/time, and state: user-provided, sourced, measured, estimated, inferred, assumed, or unknown/to confirm. Keep differing accounts attributed to their sources until there is enough evidence to explain the difference. Missing from the supplied prompt is not proof that a record or process is absent in reality; label that input unknown unless its absence is explicitly established. State the calculation and missing inputs when a number is requested but unavailable.
3. **Describe the sequence before explaining it.** Separate intended outcome, decisions/changes, handoffs, execution, and observed result. Distinguish correlation, chronology, and a supported causal explanation. Test the leading explanation against the strongest counterevidence and plausible alternative. When accounts conflict about cause, do not rank one as “most likely” without independent evidence that distinguishes them; adding a caveat after naming a winner does not fix the overclaim. If you suggest which evidence to collect first, state the practical reason (such as urgency or collection cost), not implied likelihood. If the evidence cannot choose between explanations, say what is known and what would distinguish them.
4. **Inspect only relevant system lenses.** Use the eight judgments in [the method reference](references/eight-judgments.md) as lenses, not mandatory sections: problem judgment; responsibility boundaries; alignment; context transfer; outcome closure; capacity/capability; team growth; and next-case learning. Select the few that explain this case; do not fill every lens or invent a systemic pattern from one anecdote.
5. **Turn learning into a small next-cycle experiment.** For each supported learning, state what to keep/change/stop, the next action, a verification signal or review condition, and a responsible role/date only when confirmed. Otherwise mark owner/date `待确认` and name who or what must confirm it. Prefer a reversible check over a broad new process when evidence is weak.
6. **Calibrate the conclusion.** State the bounded conclusion, evidence, material unknowns, and what evidence could change it. Do not assign personal fault from role labels or a single account. Do not claim an action worked merely because it was completed.

## Output

Fit the output to the user’s request. For a full retrospective, use a concise structure such as:

- **复盘问题与范围** — outcome, period, baseline/scope, decision to inform.
- **事实与来源** — key observations and their evidence state; keep estimates, inferences, differing accounts, and unknowns explicit.
- **判断** — supported pattern(s), impact, strongest alternative/counterevidence, and confidence boundary. Omit unsupported root-cause claims.
- **下次保留 / 改变 / 停止** — a small number of actions with verification signals; owner/date only if known, otherwise `待确认`.
- **待补证据** — only inputs that could change the judgment or action, with a collection method/calculation basis where useful.

For a short question, answer directly and include only the relevant evidence and next step. It is valid to conclude that no systemic cause is established, that a proposed change should be tested, or that no blocking learning is supported. Do not manufacture a minimum number of findings, owners, dates, action items, or recommendations. Avoid a polished management-report voice unless requested; that is `eng-reporting`’s job.

## Self-check

Before responding, check that (a) each conclusion is traceable to evidence or explicitly marked as inference, (b) contradictory evidence and the strongest alternative are represented, (c) unknown owners/dates stay unknown, (d) actions can be verified, and (e) the answer is a retrospective rather than an adjacent skill’s deliverable.
