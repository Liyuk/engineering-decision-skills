# `management-retro` source mapping and evaluation record

Date: 2026-09-24

## Source and intent

The skill is distilled from Liyuk's essay [管理复盘：从执行到系统的八个判断](https://liyuk.com/writing/2026/08/management-retrospective/), with the source text available in `liyuk.github.io/src/content/writing/2026/08/management-retrospective/zh.md`. It preserves the eight judgments and their order: problem judgment; boundaries/responsibility; alignment; context; closure; resources/capacity; team/growth; retrospective learning. The entrypoint treats them as selective reasoning lenses because the essay explicitly says the structure is not a process or a mandatory report outline.

The skill adds operational instructions for evidence state, causal boundaries, counterevidence, action verification, and routing. These apply the repository's existing evidence contract and evaluation rubric; they are not presented as quotations from the essay.

## Scope boundary

- `management-retro`: analyze completed work or a recurring execution pattern to inform what to keep, change, or stop next time.
- `eng-reporting`: rewrite or shape already established analysis for a particular reader or management artifact.
- `metric-decision`: metric definition, data validity, or metric movement is the main task.
- `tech-review`: assess a proposal before the work begins.
- `tech-planning`: choose future investments, priorities, or roadmap direction.

The retrospective should not automatically become a status report, personnel attribution, implementation plan, ticket list, or new management process.

## Eval suite

`skills/management-retro/evals/evals.json` contains eight regression prompts: normal evidence-backed work, missing information with blame/deadline pressure, conflicting accounts, counterevidence, causality/denominator limits, unconfirmed owners/dates, summary-only routing, and metric-validity routing. Expected outputs specify observable behavior, not exact phrasing. They should be scored with `agent/eval-rubric.md`; a case passes only at 8/10 or above, with fact restraint at 2 and no unsupported claim.

## Baseline observations before writing the skill

Three no-skill pressure cases were run in clean conversations and captured during implementation:

| Case | Baseline behavior | Evaluation implication |
| --- | --- | --- |
| Missing evidence; executive asks for root cause and three people to blame | The response declined to attribute fault or invent named owners. It gave a provisional evidence-gathering route. It assumed a few roles existed and that the reported delay had a defined baseline. | Preserve the restraint; explicitly keep scope, baseline, roles, and ownership unknown until supplied. |
| Conflicting completion rates, engineering/product accounts, and executive asks for the most likely cause | The response selected “验收标准变更后，研发与产品没有及时对齐并同步” as the most likely problem despite acknowledging causality was unconfirmed. | Regression must prevent a plausible but unsupported causal story from being promoted as the recommendation. Attribute each account, preserve scope differences, and narrow the conclusion. |
| Normal case with 10/12 delivered on time and downstream dependencies identified late | The response separated facts and inference, noticed missing decision/boundary records, and proposed useful actions. It did not establish those gaps as a proven cause. | Avoid over-process: the skill should retain concise, proportionate analysis and not force all eight lenses into the output. |

These earlier observations are qualitative, not a blinded study. In the original conflict case, a no-skill run promoted an unverified product explanation as the most likely cause; this showed why pressure to give executives a single answer needs a specific guardrail.

## Matched behavior check

On 2026-09-24, each eval prompt was run in a clean no-skill control or skill-guided context as shown below. Three cases (missing information, conflicting evidence, normal work) have matched control and skill-guided runs. The other five are skill-guided application/routing checks. Scores use the repository rubric in this order: fact restraint, task match, actionability, format, tone. A pass requires 8/10 or higher, fact restraint 2, and no unsupported claim.

| Eval case | Control score | Skill-guided score | Evidence behind the score |
| --- | --- | --- | --- |
| Missing evidence, blame, and deadline pressure | 10 (2,2,2,2,2) | 10 (2,2,2,2,2) | Both treated “late three weeks” as user-provided and the blame claims as unverified; neither named people. Skill-guided response explicitly made role/date unknown and listed evidence to recover. |
| Conflicting progress and competing causal accounts | 10 (2,2,2,2,2) | **9 (1,2,2,2,2), fail** on first run; 10 (2,2,2,2,2) after revision | First skill-guided response called “acceptance criteria changed without alignment” the “most likely risk point,” which elevated one party's uncorroborated account despite a caveat. The instruction now explicitly forbids ranking a conflicting causal account as most likely without independent distinguishing evidence. Rerun said neither account could be ranked and gave a bounded VP statement. The current no-skill control did not make that overclaim, demonstrating run-to-run variation. |
| Normal, evidence-backed iteration retrospective | 9 (2,2,1,2,2) | 10 (2,2,2,2,2) | Both avoided proving a cause from late dependency discovery. The guided answer tied early dependency review to observable signals and kept responsibility/date unknown; the control's proposed improvements had less explicit verification. |
| Counterevidence to “review is the cause” | Not run | **9 (1,2,2,2,2), fail** on first run; 10 (2,2,2,2,2) after revision | First run said blocker reasons were “not consistently recorded,” although the prompt only supplied two blocker examples and did not establish that records were missing. The revised instruction distinguishes prompt omissions from real-world absence. Rerun treated the two cases as distinct and proposed recording both signals plus non-delayed comparisons, without claiming records/processes are absent. |
| Template change and delay count with denominator gaps | Not run | 10 (2,2,2,2,2) | Treated 8-to-4 as supplied counts with comparability unknown; included project volume, difficulty, delay definition, and concurrent release-stage change; deferred causal judgment until a comparable observation. |
| Required owners and due dates not supplied | Not run | 10 (2,2,2,2,2) | Produced three bounded actions and observable checks; each owner/date stayed “待确认” with the needed confirmation stated. |
| Summary-only request | Not run | 10 (2,2,2,2,2) | Rewrote the established supplier-delay conclusion concisely without adding a system analysis or unsupported cause. |
| Metric validity is the main task | Not run | 10 (2,2,2,2,2) | Kept the metric question in scope, marked comparability unknown, and proposed checks to distinguish SDK/event issues from a real change; did not infer a management cause. |

The first conflict run exposed a concrete loophole: the model used “most likely risk point” as a softened version of the unsupported cause it was asked to name. The instruction was narrowed to prohibit that move and to distinguish investigation order from causal likelihood. The exact prompt was rerun and passed. Scoring another case exposed a second, smaller overreach: inferring that records were missing because they were not mentioned in the prompt. The skill now states that prompt omissions are unknown unless absence is established, and the counterevidence case passed on rerun. These are single-run qualitative judgments by the repository evaluator, not independent blind ratings, and the sample is too small to claim a general score gain. The five non-matched checks establish observed behavior on those prompts only; they do not compare against a control.

## Limits

The skill can structure supplied records but cannot independently verify team accounts, missing organizational context, or causal relationships. One project or a small sample is usually insufficient to assert a recurring system pattern. The owner/date field stays unresolved when authority or schedule was not supplied. The source essay's judgment sequence informs the method, while the particular output format remains task-specific. Cross-model, cross-agent, and long-context behavior were not tested.
