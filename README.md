[Chinese](README.zh-CN.md)

# Engineering Decision Skills

[![Validate](https://github.com/Liyuk/engineering-decision-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/Liyuk/engineering-decision-skills/actions/workflows/validate.yml)

> Turn a messy engineering discussion into a judgment with an evidence boundary, a decision, and a way to verify it next.

## Start in five minutes

Install the skill closest to the current problem:

```sh
npx skills add Liyuk/engineering-decision-skills --skill metric-decision --agent codex --global
```

Then hand it the real question:

```text
$metric-decision
Save success fell from 98% to 93%, and the instrumentation was migrated the same week. What can we conclude now, which explanations are still unconfirmed, and how should we verify the next step?
```

To see a result before installing, read the [decision-pressure example](examples/decision-pressure.md) and the [three public case reports](#how-the-conclusion-changes). Those examples are written in Chinese. The skill instructions are written in Chinese.

Five independently installable Agent Skills, for **technical managers, engineering managers, and people who also carry a senior Tech Lead role**. They handle the moments when one sentence pulls an engineering discussion off course: a number just dropped, a proposal is rushing toward launch, a delayed project needs a cause, or a pile of execution notes has to reach the person who can actually decide.

The collection splits that judgment into five separate tasks: where to put technical effort, reviewing someone else's technical proposal or technical plan, deciding what a metric can support, learning from completed work, and stating a judgment that has already been formed for management. The shared aim is not text that sounds more managerial. It is to keep an unknown from becoming a fact, a correlation from becoming a cause, and a suggestion from becoming a confirmed arrangement.

The methods start from planning, metric, review, retrospective, and decision-communication practice that the author has repeatedly written up from engineering work. The skills turn those judgment steps into something that can be invoked for a task. They do not pour the original essays into a fixed report template. The sources are [technical planning](https://liyuk.com/writing/2025/11/technical-planning-business-and-competitive-analysis/), [defining a metric before arguing about it](https://liyuk.com/writing/2021/03/define-the-measurement-before-arguing-about-metrics/), [management retrospectives](https://liyuk.com/writing/2026/08/management-retrospective/), and [decision communication](https://liyuk.com/writing/2023/03/information-sync-for-decisions/).

The skills share one working rule: keep the source of a fact and what is still unknown, conclude only inside what the evidence supports, and give a next step that can be checked. They help a technical owner examine and form a judgment. They do not replace a domain specialist or the organization's decision.

## Skills

| Skill | Question it answers | Use another skill when |
| --- | --- | --- |
| [`tech-review`](skills/tech-review/SKILL.md) | Does the evidence and delivery readiness of an existing proposal support the current decision? | Drafting a roadmap from scratch: `tech-planning`. Explaining a metric change: `metric-decision` |
| [`tech-planning`](skills/tech-planning/SKILL.md) | Where should limited capacity go, and which engineering work should be done, deferred, or stopped? | Reviewing a proposal that is already written: `tech-review` |
| [`metric-decision`](skills/metric-decision/SKILL.md) | What does a metric measure, is the change trustworthy, and what action can it support? | Reviewing a whole proposal: `tech-review`. Rewriting a conclusion that is already settled: `eng-reporting` |
| [`management-retro`](skills/management-retro/SKILL.md) | What did completed engineering work show, and what should be kept, changed, or stopped next time? | Only compressing a confirmed conclusion: `eng-reporting` |
| [`eng-reporting`](skills/eng-reporting/SKILL.md) | How should an existing conclusion be written so a reader can judge it and act on it? | Still deciding the cause and what to change next time: `management-retro` |

Install and invoke the one skill that matches the current task. There is no need to run the set in order. Each skill's `description` names the neighboring skill to use when a task crosses a boundary.

## What it stops

For example:

```text
"The team's MR Rate rose 25% this quarter, so individual productivity improved. Next quarter, set an MR target for every engineer."
```

In this input, `+25%` may be a real observation, but it does not say what the denominator is, where the team boundary is, what kinds of MRs were counted, what the review load was, or what happened to quality and delivery. The project does not continue from that sentence into personal quotas. It first says what can be confirmed: an aggregate metric changed. That does not prove that individual productivity rose, and it does not support a fair individual target.

It then turns the argument into a next step that can be carried out: check the metric card and a comparable window, check team composition and classification quality, add quality and delivery guardrails, and only then decide whether a team-level check is worth doing. The before-and-after judgment is in the [decision-pressure example](examples/decision-pressure.md).

## Which skill to start with

When you are unsure, use the "Use another skill when" column above. On a first use, start with one of these:

- `$metric-decision`: a number is driving a decision, and you are not sure it is comparable, causal, or the right basis for action.
- `$tech-review`: a proposal has already been written, and you want to know whether the evidence is actually enough for the current decision.

The other three cover future investment choices, learning from completed work, and compressing an existing conclusion into something a reader can judge. They are not five required steps in one pipeline.

## How the conclusion changes

Each case report below takes one public source and runs it through the five skills, so the tasks stay distinct. The reports cite first-party engineering material from GitHub, Google, and GitLab. Text added to stand in for a proposal the user supplied is marked as a demonstration setting and is not presented as the source text. The reports are written in Chinese.

- [Production incident: accidental deletion in a Google satellite cluster](examples/reports/google-satellite-incident.md)
- [Database migration: GitHub gh-ost and the MySQL migration flow](examples/reports/github-mysql-migrations.md)
- [Engineering productivity metric: GitLab MR Rate](examples/reports/gitlab-mr-rate.md)

Each report shows the judgment from `tech-planning`, `metric-decision`, `tech-review`, `management-retro`, and `eng-reporting`. A skill does not force a conclusion onto a question it does not fit. When the information is insufficient, it names the unknown and the input that is still needed.

## Install

Each skill is entered through `SKILL.md`. The directory includes the references that skill needs and a copy of the evidence contract, so a copied skill does not depend on other paths in the repository. Copy a directory into Codex's personal skills directory:

```sh
mkdir -p ~/.codex/skills
cp -R skills/tech-review ~/.codex/skills/
```

You can also install one skill from this repository with the [Vercel Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add Liyuk/engineering-decision-skills --skill tech-review --agent codex --global
```

Replace `tech-review` with any skill name in the table above. This project is a Markdown skill package and does not publish an npm package; `npx` only runs the shared installer. Skill directories follow the [Agent Skills format](https://agentskills.io). Installation and discovery have been smoke-tested on Codex only. Claude Code and other hosts have not been checked one by one. A compatible format is not evidence that the behavior has been verified.

## Start by reviewing someone else's proposal

To review a technical proposal or technical plan written by someone else, try `$tech-review`. Ask it to check the goal, the evidence, the options, resources and dependencies, delivery risk, and acceptance evidence, and to tie each material issue to the source text, the impact, and a suggested action. It separates blockers from suggestions. When the evidence does not support a blocker, it can give a pass.

```text
$tech-review
Review this technical plan. Check the evidence for the goal, the alternatives, resources and dependencies, implementation order, the main risks, and the acceptance metrics. For each issue, name the source text, the impact, and the suggested action. Report only issues that would change the decision. Do not rewrite the plan.
```

To form a plan from a blank page, use `$tech-planning`. When the main question is whether a metric's definition or change is trustworthy, use `$metric-decision`. The three public cases above are further reports.

## Project boundaries

The project turns the frontline judgment steps of a technical manager or senior Tech Lead into light skills that can be called on their own, so evidence, unknowns, trade-offs, and actions stay clear in the agent's output. The repository currently contains five skills and 42 evaluation cases. Those evaluations are a limited case check. They do not show that every model, team, or real situation will get the same result. The scope does not include a code-implementation workflow, and it does not extend to hiring, performance, 1:1s, or team-health management.

Cases, evaluations, and documentation changes with a clear boundary are welcome through the [contributing guide](CONTRIBUTING.md), which is written in Chinese. Repository CI checks skill entrypoints, the evaluation inventory, and local links.

## License and versions

The repository is under the [MIT License](LICENSE). Version history is in [`CHANGELOG.md`](CHANGELOG.md) and [GitHub Releases](https://github.com/Liyuk/engineering-decision-skills/releases).
