# Engineering Decision Skills

> 把混乱的工程讨论，变成有证据边界、可作决定、能继续验证的判断。

五项可独立安装的 Agent Skills，主要面向**技术经理/工程经理，以及同时承担资深 Tech Lead 职责的人**。它们处理工程现场最容易被一句话带偏的时刻：一个数字刚好下降、一份方案急着上线、一个项目延期要找根因，或者一堆执行记录需要交给真正有决定权的人。

它把这些判断拆成五项独立任务：规划技术投入、评审别人写的技术方案和技术规划、判断指标能支持什么结论、从已完成工作中提炼改进，以及向管理层表达已形成的判断。共同目标不是生成更像管理术语的文本，而是防止未知变成事实、相关变成因果、建议变成已确认安排。

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

## 它会阻止什么

例如：

```text
“团队 MR Rate 本季度上升 25%，说明个人生产力提高。下季度给每位工程师设 MR 目标。”
```

这个输入里，`+25%` 可能是真实观察，但它没有告诉我们分母、团队边界、MR 类型、评审负担、质量或交付结果。项目不会顺着这句话直接写出个人配额，而会先指出：当前只能确认一个聚合指标发生变化，无法据此证明个人生产力提升，更不能直接推出公平的个人目标。

它接着把争论变成可执行的下一步：核对指标卡和可比窗口，检查团队构成与分类质量，补充质量/交付护栏，再决定是否值得做团队级验证。完整的前后判断见[决策压力示例](examples/decision-pressure.md)。

## 从哪个 Skill 开始

如果你第一次使用，优先从这两个入口开始：

- `$metric-decision`：当一个数字正在推动决定，但你不确定它是否可比、能否归因或应该采取什么行动。
- `$tech-review`：当一份方案已经写出来，但你想知道它是否真的有足够证据支持当前决定。

其余三个入口分别处理未来投资取舍、已完成工作的学习，以及把已有结论压缩成读者能判断的材料。它们不是必须串成一条流水线的五步流程。

## 看它如何改变结论

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

项目聚焦于把技术经理和资深 Tech Lead 的一线判断步骤做成轻量、可单独调用的能力，让证据、未知、取舍和行动在 Agent 输出中保持清楚。当前仓库包含五项 Skill 和 39 个评测案例；评测是有限案例检查，不能证明所有模型、团队或真实场景都会获得同等效果。职责范围不包含代码实现工作流，也不扩展到招聘、绩效、1:1 或团队健康管理。

## 许可与版本

整个仓库采用 [MIT License](LICENSE)。版本变化见 [`CHANGELOG.md`](CHANGELOG.md) 与 [GitHub Releases](https://github.com/Liyuk/engineering-decision-skills/releases)。
