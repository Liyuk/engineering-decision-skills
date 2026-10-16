---
name: metric-decision
description: Use when a metric needs definition or validation, a product or engineering metric changes unexpectedly, or measurement evidence must support an action. Do not use it for a broader proposal review (use tech-review), a capacity roadmap (use tech-planning), learning from completed work (use management-retro), or rewriting an already settled conclusion (use eng-reporting).
license: MIT
---

# 指标判断

先确认这个数字在测什么、是怎么得到的，再决定它能支持什么行动。一个指标只有在对象、口径、数据质量和决策后果都清楚时，才适合拿来推动决定。

## 什么时候用

- 要定义一个指标，或核对它的对象、口径和数据质量；
- 一个数字变了，需要判断变化是否可比、哪些解释还没被分开、下一步怎样验证。

如果要评审一整份尚未实施的方案，用 `tech-review`。如果要决定能力投向和路线图，用 `tech-planning`。如果结论已经成立，只是要写成汇报，用 `eng-reporting`。如果要从已完成工作里决定下次保留、改变或停止什么，用 `management-retro`。

## 工作方式

1. 把问题说成一个可观察的用户任务或系统结果，并确认范围、比较窗口和读者。
2. 写清对象、分子、分母、排除项、来源、时间窗口、分段和样本量。输入不全时，说明缺什么以及怎样算出来。
3. 先检查定义、埋点覆盖、重复事件、延迟、样本量和可比性，再解释变化。产品真的变了，和报表或采集方式变了，是两件事。
4. 保留几个能被证伪的解释，写明什么证据能支持或排除它们。仅凭时间先后或相关关系，不下因果结论。
5. 把下一步写成一次可检查的动作：假设、预期变化、护栏指标、验证窗口，以及停止或回退条件。

最小设计通常只需要一个主指标、算出它所需的最小事件集合和一个关键数据质量检查。只有会改变当前决定的诊断项，才继续展开完整事件模型或看板。

## 输出

调查指标变化时，通常回答：现在能确认什么、口径和证据是否可靠、哪些解释仍未分开、下一步先查什么。

设计新指标时，先给出任务定义、事件或状态变化、主指标和一个关键数据质量检查；只有确实影响决定的诊断项才继续展开。

证据状态和字段定义见 [references/decision-and-review-contract.md](references/decision-and-review-contract.md)。详细方法见 [references/metric-decision-method.md](references/metric-decision-method.md)，示例见 [examples/instrumentation-change.md](examples/instrumentation-change.md)。
