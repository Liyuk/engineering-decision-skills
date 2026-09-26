---
name: metric-decision
description: Use when the metric itself needs definition or validation, when a product/engineering metric changes unexpectedly, or when measurement evidence must support an action. Use tech-review for broader proposal review.
license: MIT
---

# 指标判断

先确认这个数字在测什么、是怎么得到的，再决定它能支持什么行动。一个指标只有在对象、口径、数据质量和决策后果都清楚时，才适合拿来推动决定。

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

继续使用共享的证据状态和字段定义，见 [agent/decision-and-review-contract.md](../../agent/decision-and-review-contract.md)。详细方法见 [references/metric-decision-method.md](references/metric-decision-method.md)，示例见 [examples/instrumentation-change.md](examples/instrumentation-change.md)。
