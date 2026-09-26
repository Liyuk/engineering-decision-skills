---
name: tech-review
description: Use when reviewing an existing technical proposal, architecture, benchmark, AI adoption plan, or decision brief for evidence, trade-offs, delivery risk, and decision readiness. Use tech-planning to create a new roadmap.
license: MIT
---

# 技术方案评审

帮助用户判断一份已有方案是否足以支持当前决定。评审不是为了证明评审者更懂，也不是顺手把原文重写一遍；只指出有材料依据、并且会影响决定或交付的问题。

## 工作方式

先确认材料、目标、读者、要作的决定和评审范围。没有原文时，明确结论只能基于用户的描述。

接着核对方案里的关键主张、数据口径、比较条件、假设和依赖。根据实际风险检查需求追溯、架构边界、迁移兼容、安全、容量、测试、可观测性、发布、回滚和运维；不相关的部分跳过。

每个实质问题都写清：问题是什么，依据在哪里，放着不改会怎样，建议下一步是什么，优先级和当前状态。偏好不是缺陷；材料不足以判断时，写成待确认。

最后给一个能帮助决策的结论：通过、带条件通过、暂缓决定或不通过，并说明依据和限制。没有阻塞问题时可以明确通过，把可读性或完善性建议单独列为非阻塞项。

评审不是问题越多越好。一条好的发现能让作者知道缺什么证据、会影响哪个决定，以及下一步怎样补齐；没有足够依据的问题就不要列成缺陷。

## 输出

短评审可以压缩成：结论 → 关键依据 → 主要风险或未知 → 下一步。

完整评审可按“决定请求、现状与依据、判断与选项、建议条件、执行护栏”组织，但不必为了套结构补齐不存在的内容。评审发现的字段和优先级见 [agent/decision-and-review-contract.md](../../agent/decision-and-review-contract.md)。

示例和提问参考见 [references/good_bad_examples.md](references/good_bad_examples.md) 与 [references/interrogation_snippets.md](references/interrogation_snippets.md)。需要说明方法来源时再看 [references/method-sources.md](references/method-sources.md)。
