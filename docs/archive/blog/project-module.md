# 博客项目模块：工程分析与决策 Skills

以下正文可复制到博客项目介绍中。发布前可按页面篇幅调整。项目采用 MIT 许可证，公开仓库见 [GitHub](https://github.com/Liyuk/engineering-decision-skills)。

---

## 把一线工程判断整理成可调用的 AI 工作流

工程师和技术负责人经常需要做一些具体判断：有限的工程时间投在哪里，一个指标的变化能不能相信，一份方案是否足以支持上线或投资，项目结束后下次该改什么，以及怎样把已有结论交给真正需要作决定的人。

我把自己在工程工作和写作中反复使用的判断方法整理成五项可独立安装的 Agent Skills。它们做的是辅助分析和决策，不替人访问缺失的数据、代替专业评审或替组织拍板。共同方法是：先说清问题与决定，保留材料来源和证据状态，指出会改变判断的未知，只给证据能支持的结论，并把下一步变成可检查的行动。

目前包含五项独立能力：

- **技术规划（`tech-planning`）**：比较工程投资、能力约束和机会成本，说明做什么、暂缓或停止什么，以及何时根据新证据重评。
- **指标决策（`metric-decision`）**：先定义数字测量的任务和对象，再检查口径、数据质量与可比性，最后说明变化支持什么行动。
- **技术评审（`tech-review`）**：评审已有方案的证据、取舍和交付保障。发现要对应依据、影响和建议动作；没有阻塞问题时可以通过。
- **管理复盘（`management-retro`）**：从已完成的工程工作中分析有依据的执行与系统模式，决定下次保留、改变或停止什么；不从材料不足处推断个人责任或强加流程。
- **工程汇报（`eng-reporting`）**：把已经提供或确认的事实和结论整理成读者能判断、能行动的摘要。它负责传递结论，不是泛沟通教练，也不替代复盘分析。

这五项技能不需要按顺序全部运行。只调用当前任务需要的那一项；当工作真的跨越边界时再交接，例如先核验指标，再用已确认的结果调整投资选择。

### 为什么做成五项

这不是一个覆盖招聘、绩效、1:1、个人发展和团队士气的全面工程经理助手。`manager-dot-dev/manager-skills` 等社区项目已经覆盖了更广的工程管理场景；我借鉴它们具体任务触发、简短回答和可执行下一步的设计，但保留这五项更贴近工程决策现场的工作。个人写作是方法来源，不是独有优势。更值得验证的问题是：这些边界明确的技能，能否让 Agent 更稳定地保留事实来源、承认未知、避免越过证据下结论，并给出可行动的判断。

Matt Pocock 的 Skills 和 Han 更多围绕软件交付、实施计划和计划评审；工程管理类集合则常扩展到人员和团队场景。本项目刻意把范围留在五个具体问题：**投什么、数字说明什么、方案能否支持决定、过去的工作能说明什么、已知结论如何交给决策者**。这是一项产品假设，不是已经证明的效果或市场空白。社区对比及边界分析见[调研报告](../research/2026-09-25-github-demand-utility-review.md)。

### 如何试用

```text
$metric-decision
保存成功率从 98% 降到 93%，但同期迁移了埋点。请判断这两个数字是否可比，今天能得出什么结论，还缺什么证据，以及我下一步该做什么。
```

示例数字是虚构输入，不代表生产系统结果。完整案例见 [`metric-decision` 示例](../../../skills/metric-decision/examples/instrumentation-change.md)。五项入口、安装方法和适用边界见仓库 [README](../../../README.md)。

### 方法来源与评测

这些方法来自我对技术规划、指标定义、周期统计与复盘、信息同步和工程规范的持续写作。转成 Skill 时，我保留原文中的判断顺序和问题结构，同时把证据状态、未知、冲突、评审发现格式和边界用例写成可检查的指令。管理复盘保留原文“八个判断”的次序，但作为按情境选用的分析视角，而不是每次都要填满的报告章节。原文到技能的映射见[方法映射](../methodology/writing-to-skills-map.md)。

仓库目前五项技能共 **38 个评测 prompt**。其中包括基于 GitHub、GitLab 与 Google SRE 一手材料设计的案例、每项技能的正常/缺数据/冲突用例，以及 `management-retro` 的匹配基线与技能对照。评测记录包括首轮失败、针对性修订和回归结果；这些是小样本、单轮人工量规检查，不是盲测，也不能证明跨模型或真实业务效果。具体样本、评分和限制见[组合评审](../methodology/skills-portfolio-review.md)、[公开案例评测](../methodology/public-case-evaluation.md)和[`management-retro` 评测](../methodology/management-retro-evaluation.md)。

我想探索的不是让 AI 扮演一个无所不知的强势管理者，而是把在工程实践中有用的判断过程变得可调用、可检查、可修订。

相关写作：

- [技术规划，本质上是业务分析与竞品分析](https://liyuk.com/writing/2025/11/technical-planning-business-and-competitive-analysis/)
- [指标争论之前，先定义测量对象](https://liyuk.com/writing/2021/03/define-the-measurement-before-arguing-about-metrics/)
- [周期统计与复盘，让数字变成下一次行动](https://liyuk.com/writing/2021/05/periodic-metrics-and-retrospectives/)
- [管理复盘：从执行到系统的八个判断](https://liyuk.com/writing/2026/08/management-retrospective/)
- [信息同步不是抄送：怎样让对方能作决定](https://liyuk.com/writing/2023/03/information-sync-for-decisions/)

---

### 发布备注（不属于博客正文）

- GitHub 远端 `Liyuk/engineering-decision-skills` 目前公开，根仓库和五个独立 skill 均采用 MIT。
- Codex 已完成发现与复制安装烟雾检查。Claude Code 等其他 Agent 尚未逐一验证触发和输出行为。
- “38 个 prompt”指五份 `evals/evals.json` 中的案例总数，不等于 38 个都做过基线对照。`management-retro` 的 8 个用例中，3 个有匹配基线，其余 5 个为技能应用/路由检查；其他评测的设计和局限见上方链接。
- `public-case-evaluation.md` 记录四项原有技能在四个公开案例上的一轮比较，以及规划/汇报两项回归；它不是五项技能的统一比较批次。
