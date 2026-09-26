---
name: management-retro
description: Use when a user asks to learn from completed engineering work, a project period, or an incident by examining recurring execution and system patterns and choosing what to keep, change, or stop next time.
license: MIT
compatibility: Works in Agent Skills environments that can read the supplied project notes, records, and references.
---

# 工程复盘

从已经完成的项目、交付周期或事故中，找出下一次值得改变的地方。复盘关注工作的系统和决策，不是给个人定责，也不是把状态报告换一种格式。

## 什么时候用

- 想知道工作为什么偏离目标，以及哪些判断、交接或约束造成了影响；
- 想决定下次保留、改变或停止什么；
- 想把一次事故或一段交付经历变成下一轮可以验证的改进。

如果只是整理已有结论，用 `eng-reporting`。如果主要在查指标口径或数据变化，用 `metric-decision`；如果要评审一份还没实施的方案，用 `tech-review`；如果要安排未来投入，用 `tech-planning`。

## 工作方式

先把问题、范围、预期结果和要支持的决定说清楚。然后按时间顺序还原发生了什么：目标、决定和变化、交接与执行、最后观察到的结果。解释原因时，区分时间上的先后、相关关系和有证据支持的因果关系。

对重要说法保留来源和状态：用户提供、来源支持、实测、估算、推断、假设或待确认。不同人说法不一致时，先保留各自的说法；没有能区分它们的证据，就不要挑一个当“最可能原因”。输入里没有提到某件事，也不等于现实中没有这件事。

只使用能解释当前案例的视角，例如问题判断、责任边界、上下文传递、结果闭环、容量与能力、团队成长或下一次学习。不要求每次都把所有视角填一遍。

每个有依据的学习，落到一个小而可验证的下一步：保留/改变/停止什么，先做什么，用什么信号检查，何时复看。负责人和日期只有在材料确认过时才写；否则保留为待确认。

如果事故还在处理中，先写当前的预防、检测、止损和修复，不急着下根因结论。复盘不自动生成工单或执行计划，除非用户明确需要。

## 输出建议

完整复盘通常包括：

- 复盘问题与范围；
- 事实、来源和仍有分歧的地方；
- 当前能支持的判断，以及最强的替代解释；
- 下次保留、改变或停止的少数动作；
- 只有在会改变决定时才列出的待补证据。

短问题就直接回答，不要为了显得完整而制造固定数量的发现、负责人或行动项。可以得出的结论也可能是：目前没有证据支持某个系统性原因，某项改变应该先试验，或暂时没有需要阻塞决定的学习。

详细判断视角见 [references/eight-judgments.md](references/eight-judgments.md)。
