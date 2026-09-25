# Engineering Decision Skills

五项可独立安装的 Agent Skills，主要面向**技术经理/工程经理，以及同时承担资深 Tech Lead 职责的人**。它把这两类角色的一线工程判断拆成五项独立任务：规划技术投入、评审别人写的技术方案和技术规划、判断指标能支持什么结论、从已完成工作中提炼改进，以及向管理层表达已形成的判断。评审他人方案是重要场景之一；整套能力覆盖工程工作从规划、执行观察到复盘和沟通的关键判断点。

方法起点是项目作者在工程写作中反复总结的规划、指标、评审、复盘和决策沟通经验。技能把这些判断步骤变成可按任务调用的能力，不把原文文章套成固定报告模板。可从[技术规划](https://liyuk.com/writing/2025/11/technical-planning-business-and-competitive-analysis/)、[指标定义](https://liyuk.com/writing/2021/03/define-the-measurement-before-arguing-about-metrics/)、[管理复盘](https://liyuk.com/writing/2026/08/management-retrospective/)和[决策沟通](https://liyuk.com/writing/2023/03/information-sync-for-decisions/)了解方法来源。

这些技能共享一条工作原则：保留事实来源和未知状态，只在证据支持的范围内下结论，并给出可核实的下一步。它们帮助技术负责人审查和形成判断，不替代领域专家或组织决策。

## Skills

| Skill | 适用问题 |
| --- | --- |
| [`tech-review`](skills/tech-review/SKILL.md) | 现有方案的证据和交付保障足以支持当前决定吗？ |
| [`tech-planning`](skills/tech-planning/SKILL.md) | 有限能力投向哪里，做、缓、停哪些工程工作？ |
| [`metric-decision`](skills/metric-decision/SKILL.md) | 一个指标测量什么、变化可信吗、支持什么行动？ |
| [`management-retro`](skills/management-retro/SKILL.md) | 已完成的工程工作说明了什么，下次保留、改变或停止什么？ |
| [`eng-reporting`](skills/eng-reporting/SKILL.md) | 怎样把已形成的结论整理成读者可判断、可行动的材料？ |

按当前任务安装和调用单项技能，无须顺序运行整套流程。

## 看实际报告会得出什么结论

下面三份案例报告各选一份公开材料，再分别交给五项能力处理，展示不同任务下的结论如何分工。报告引用 GitHub、Google 和 GitLab 的一手工程材料；为补齐用户交来的方案而构造的文本会明确标成“演示设定”，不冒充来源原文。

- [生产基础设施事故：Google 卫星集群误删事件](examples/reports/google-satellite-incident.md)
- [数据库迁移方案：GitHub gh-ost 与 MySQL 迁移流程](examples/reports/github-mysql-migrations.md)
- [工程生产力指标：GitLab MR Rate](examples/reports/gitlab-mr-rate.md)

每份报告都会分别展示 `tech-planning`、`metric-decision`、`tech-review`、`management-retro` 和 `eng-reporting` 的判断。技能不会为了“展示五项能力”而对不适用的问题硬给结论；信息不足时会写明未知和所需输入。

## 安装

每项技能都以 `SKILL.md` 为入口，可直接复制目录到 Codex 的个人技能目录：

```sh
mkdir -p ~/.codex/skills
cp -R skills/tech-review ~/.codex/skills/
```

也可使用 [Vercel Skills CLI](https://github.com/vercel-labs/skills) 从本仓库安装单项技能：

```sh
npx skills add Liyuk/engineering-decision-skills --skill tech-review --agent codex --global
```

把 `tech-review` 换成上表中的任一技能名即可。本项目是 Markdown 技能包，不需要发布 npm 包；`npx` 只负责运行通用安装工具。技能目录遵循 [Agent Skills 格式](https://agentskills.io)。目前只在 Codex 上完成安装与发现冒烟验证；Claude Code 等环境尚未逐一验证，格式兼容不等于行为已经验证。

## 从评审别人写的方案开始

如果你要审一份别人写的技术方案或技术规划，先试 `$tech-review`。让它检查目标、依据、方案取舍、资源与依赖、交付风险和验收证据，并把每项实质问题与原文依据、影响和建议动作对应起来。它会区分阻塞问题与改进建议；证据没有发现阻塞项时，可以给出通过结论。

```text
$tech-review
请评审这份技术规划：检查目标依据、备选方案、资源与依赖、实施顺序、主要风险和验收指标。逐项标明原文依据、影响和建议动作；只报告会影响决定的问题，不要直接重写。
```

如果需要从空白开始形成规划，改用 `$tech-planning`；如果主要问题是某个指标的口径或变化是否可信，再用 `$metric-decision`。更多实际报告见上方三个公开案例。

## 项目边界

项目聚焦于把技术经理和资深 Tech Lead 的一线判断步骤做成轻量、可单独调用的能力，让证据、未知、取舍和行动在 Agent 输出中保持清楚。职责范围不包含代码实现工作流，也不扩展到招聘、绩效、1:1 或团队健康管理。当前评测是有限案例检查，不能证明所有模型、团队或真实场景都会获得同等效果。

## 许可与版本

整个仓库采用 [MIT License](LICENSE)。版本变化见 [`CHANGELOG.md`](CHANGELOG.md) 与 [GitHub Releases](https://github.com/Liyuk/engineering-decision-skills/releases)。
