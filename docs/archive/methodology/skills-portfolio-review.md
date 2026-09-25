# Skills Portfolio Review

Date: 2026-09-24

This note synthesizes the independent discussion group review of the skills, the source-to-skill map, and the author's writing in `liyuk.github.io`. It records product boundaries and selected behavioral comparisons; it is not a claim that the skills outperform a capable base model in general.

## Portfolio purpose

The collection packages five concrete analysis and decision-support tasks drawn from the author's engineering work and writing. Its primary users are people close to engineering delivery—engineers, tech leads, project owners, and product/data collaborators—not only engineering managers. The shared thread is to make a judgment easier to inspect: define the task and decision, preserve evidence and its status, compare only relevant constraints and options, expose material unknowns, and name what would change the conclusion. The five skills are complementary, independent entry points, not a mandatory sequence or a general management assistant.

| Skill | User's question | Useful output | Boundary |
| --- | --- | --- | --- |
| `tech-planning` | Where should limited engineering capacity go, and what should we defer or stop? | Investment options, trade-offs, roadmap and decision gates | Does not conduct market research or supply missing business data by itself. |
| `metric-decision` | What does this number measure, can I trust its movement, and what action can it support? | Metric definition, data checks, bounded hypotheses and verification plan | Does not replace analysis of source data or prove causality from chronology. |
| `tech-review` | Does an existing proposal have enough evidence and delivery safeguards for the decision? | Findings tied to evidence, impact, action and a bounded conclusion | Does not guarantee production safety or replace specialist security, privacy, legal, or compliance review. |
| `eng-reporting` | How can established project evidence and conclusions help this reader decide or act? | Audience-shaped update, summary, or promotion draft with provenance preserved | Does not perform open-ended system-retrospective analysis, create business impact, inflate an individual's role, or turn estimates into measured results. |
| `management-retro` | What should we learn from completed work and carry into the next similar case? | Bounded analysis of execution/system patterns; a few keep/change/stop actions with verification | Does not force blame, claim unsupported causes, rewrite established conclusions for an audience, or prescribe a full management process. |

Use one skill for the actual task. Combine them only when the work crosses a real handoff: planning may need metric definition; a proposal review may need evidence validation; established findings may then need a short update for a decision maker. `eng-reporting` carries forward conclusions—it is not a broad communication-coaching capability. Likewise, `management-retro` analyzes work patterns, not employee performance, morale, or individual profiles. The same evidence labels should follow any handoff.

## Differentiation and limits

The author's writing and experience are the source material, not by themselves the market distinction: `manager-dot-dev/manager-skills` also derives its methods from an author's articles and experience. The portfolio should therefore be described by the work it helps with: five bounded engineering decisions, with explicit evidence states and conclusions sized to the evidence. That is a testable product hypothesis, not a proven advantage. Relevant source essays include [technical planning as business and competitive analysis](https://liyuk.com/writing/2025/11/technical-planning-business-and-competitive-analysis/), [define the measurement before arguing about metrics](https://liyuk.com/writing/2021/03/define-the-measurement-before-arguing-about-metrics/), [periodic metrics and retrospectives](https://liyuk.com/writing/2021/05/periodic-metrics-and-retrospectives/), [information sync for decisions](https://liyuk.com/writing/2023/03/information-sync-for-decisions/), and [AI productivity in complex systems](https://liyuk.com/writing/2026/08/ai-productivity-complex-systems/).

Compared with `manager-dot-dev/manager-skills`, the collection intentionally does not cover hiring, 1:1s, feedback/performance, career development, employee context memory, team-health diagnosis, or generic manager communication. It borrows useful interaction patterns—narrow triggers, only consequential follow-up questions, answer-first output, and concrete next action—without adding those management domains. Its five working questions are: where to invest; what a measure means; whether a proposal is decision-ready; what completed work supports learning; and how to carry an established conclusion to its reader.

The packages can structure supplied information and expose missing evidence. They cannot independently verify unavailable source data, make an organization's decision, or ensure a proposal succeeds. Planning's external comparison is conditional on relevant sources being supplied or researched. The repository now has a unified MIT license and a public GitHub remote at [`Liyuk/engineering-decision-skills`](https://github.com/Liyuk/engineering-decision-skills).

## Source method coverage

The source writing contains more method than any skill entrypoint can responsibly load on every task. The planning reference preserves its ten-part reasoning map as an on-demand map, not a mandatory answer template.

The management retrospective's eight judgments now have a dedicated workflow in `management-retro`; they are preserved as selective lenses in the author's stated order, not fixed report sections. The structured-thinking article's five lenses remain distributed across relevant skills rather than being forced into another overlapping invocation. See [`writing-to-skills-map.md`](writing-to-skills-map.md) and [`management-retro-evaluation.md`](management-retro-evaluation.md) for the mapping and its limits.

## Discussion group findings

- **Planning:** the strongest fit is investment choice under constraints, including explicit defer/validate/abandon decisions. Do not market it as automatic competitor analysis; the current skill only uses external comparison when it helps and has evidence.
- **Measurement:** distinguish measurement validity from causal explanation, and use one primary metric plus minimal instrumentation when the user asks for a minimum design.
- **Review:** credible findings need evidence, impact and action; no-blocker proposals may pass. The skill can surface specialist-review gaps but cannot act as that specialist review.
- **Reporting:** organize material for a particular reader and decision. Preserve individual/team contribution boundaries and preserve conflicting source scopes; forceful writing must remain supportable.
- **Portfolio:** avoid a fixed multi-step funnel. The user should call the one relevant workflow, then hand off only when another deliverable is needed.

## Matched behavioral spot checks

For one pressure case per skill, an evaluator agent generated a no-skill answer and then a skill-guided answer, scoring each against the shared five-dimension rubric. This is one sample per condition, not a blinded human study.

| Skill and case | Baseline → skill | Observed difference |
| --- | --- | --- |
| Planning: management demands a 20% conversion commitment without baseline | 10/10 (2,2,2,2,2) → 10/10 (2,2,2,2,2) | Both rejected unsupported commitment and avoided fictional staffing. Skill made the unproven link between checkout feedback, release delays and refactoring more explicit, and added decision gates. |
| Review: deadline pressure despite an unrepresentative benchmark and incomplete rollback plan | 10/10 (2,2,2,2,2) → 10/10 (2,2,2,2,2) | Both found material gaps; skill more consistently stated the review's evidence scope and fields. No failure in the baseline on this sample. |
| Reporting: request to inflate personal ownership and claim unmeasured growth | 9/10 (2,2,1,2,2) → 10/10 (2,2,2,2,2) | Both preserved facts. Baseline named missing evidence but did not give a concrete collection path; skill listed scope, integration result, personal contribution and metrics to gather. |
| Metric decision: completion rate rises while event linkage coverage falls | 10/10 (2,2,2,2,2) → 10/10 (2,2,2,2,2) | Both rejected celebrating or removing old monitoring; skill enumerated the reconciliation inputs and exit condition more explicitly. No score failure in the baseline on this sample. |

Score tuple order is fact restraint, task match, actionability, format, tone. Each 0–2 judgment is tied to the corresponding behavior described in the observation column. The only observed scored gap was reporting actionability in this sample; the other comparisons are consistency checks, not evidence that the skill is necessary for a capable model to reach the same conclusion.

These results show format and method consistency in these prompts, not a general score gain. The repository contains 38 eval prompts across five skills after adding `management-retro` and an `eng-reporting` routing-boundary case. The new skill has eight guided checks, three matched control/guided cases, and two initial fact-restraint failures that were corrected and rerun. These remain small-sample qualitative judgments; do not describe them as broad effectiveness evidence or claim a general measured gain for the new skill. Details and scores are in [`management-retro-evaluation.md`](management-retro-evaluation.md).

## Additional skill-guided behavior check

### Technical-plan review rerun (2026-09-25)

The same cache-rewrite plan prompt was compared with a no-skill baseline and `tech-review` loaded. The plan described timeout complaints without a source or baseline; cache rewrite as the only option, with no slow-query repair; 20% quarterly capacity against a two-team full migration; unconfirmed database-team approval; and “significantly improved” performance without a threshold, workload, or rollback condition.

| Condition | Observed result |
| --- | --- |
| No-skill baseline | Found all five material gaps, tied them to the supplied facts, stated that the current plan should not pass pending evidence, preserved unknowns, and did not rewrite the plan. It passed all five task-specific checks. |
| `tech-review` guided | Grouped the findings into two blockers (unverifiable acceptance claim and unconfirmed approval) and two important issues (capacity/scope mismatch and unexamined alternative), with evidence, impact, and actions. It bounded the conclusion to the submitted material and did not assert the cache rewrite would fail. |

The guided answer made severity and review structure more explicit, while the baseline already reached the same core decision and identified the gaps. This rerun therefore supports a consistency/format benefit on one case, not a demonstrated improvement in decision quality. It was not blind, repeated, or tested across models.

On 2026-09-24, separate runs used each skill for one missing-data case, one conflicting-information case, and one normal case. Rubric scores were planning 10/10, 10/10, 9/10; review 10/10 on all three; reporting 10/10 on all three; and metric decision 10/10 on all three. The 9/10 planning answer stated that a checkout owner was responsible for the outcome even though the prompt had not assigned that role. This was a concrete evidence-boundary failure, not a general weakness in the skill.

The planning instructions now distinguish confirmed responsibility from suggested assignment, and the eval suite includes an explicit unconfirmed-owner boundary case. The same normal case and the new boundary case were rerun with the updated skill; both scored 10/10. These are single-run rubric judgments by the repository evaluator, not blind or no-skill comparisons. They show that the observed defect was corrected on these prompts; they do not establish broad effectiveness.

## Publication guidance

Describe this as a method-packaging and evaluation project. Suitable claims: five independent skills; eval prompts and pressure scenarios; explicit treatment of source, estimate, inference and unknown states; Codex discovery/install smoke-tested. Avoid claims of measured productivity gains, universal model compatibility, or proven decision-quality improvement. Claude Code behavior has not yet been directly tested.
