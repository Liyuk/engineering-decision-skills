# 一线工程分析与决策 Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将五项技能和项目文档统一定位为服务一线工程工作的独立辅助分析与决策工具，并完成真实场景验收。

**Architecture:** 保持五个独立 skill 的目录与调用方式。根 README 负责定位/选择/安装，`agent/` 保留跨技能证据规则，各 skill 入口描述具体工作和边界，方法映射、研究及博客说明保存来源和深入解释。

**Tech Stack:** Markdown、Agent Skills、JSON eval cases、Python repository validator。

**Spec:** `docs/superpowers/specs/2026-09-25-frontline-decision-skills-design.md`

## Global Constraints

- 独立安装边界不变，不添加根路由 Skill。
- 根 `LICENSE` 是规范许可，五个技能继续声明 MIT。
- 事实/来源/测量/估算/推断/假设/未知必须区分。
- 评审与改写分开；评审无阻塞项时允许通过。
- 技能行为变化同步更新 eval cases。

## Review Focus

- 读者会把项目误解成全面 EM 顾问：检查 README 与博客正文的定位语句及明确排除范围。
- `eng-reporting` 会被误用为泛沟通教练：增加/检查仅有已确认结论时的边界用例。
- 文档保留旧数量或夸大评测：逐项核对 5 个技能、38 个 prompt 及匹配对照数量和限制。
- 新增“辅助决策”后回答可能过度保守：检查正常案例仍能产出有根据的判断和下一步。
- 与 `manager-skills` 比较时把公开意图说成效果证明：只引用作者文件并标注证据限制。

---

### Task 1: 固化验收用例与文档基线

**Files:**
- Read: `docs/superpowers/specs/2026-09-25-frontline-decision-skills-design.md`
- Test: `skills/*/evals/evals.json`
- Read: `docs/methodology/skills-portfolio-review.md`, `docs/blog/project-module.md`

- [x] 核对五项技能各有正常、缺数据、冲突信息用例，并记录现有样本限制。
- [x] 对照 README、博客草稿和调研报告查找过时数量及不一致定位。
- [x] 将发现加入最终验收记录；本轮未发现需要改动 Skill 行为指令的问题。

### Task 2: 更新项目定位和发现路径

**Files:**
- Modify: `README.md`
- Modify: `docs/methodology/skills-portfolio-review.md`
- Modify: `docs/research/2026-09-25-github-demand-utility-review.md`

- [x] 将目标用户写为一线工程工作参与者，将产品价值写为辅助分析/决策。
- [x] 用五个“用户问题→技能输出”展示用途，声明技能独立使用而非固定流程。
- [x] 结合 manager-skills 对比明确能借鉴的交互设计和不纳入的人员/团队管理范围。
- [x] 区分产品假设、仓库评测观察和真实用户效果，避免把三者混为已证实效用。

### Task 3: 校准五项入口和原文映射

**Files:**
- Modify if needed: `skills/tech-planning/SKILL.md`
- Modify if needed: `skills/tech-review/SKILL.md`
- Modify if needed: `skills/metric-decision/SKILL.md`
- Modify if needed: `skills/management-retro/SKILL.md`
- Modify if needed: `skills/eng-reporting/SKILL.md`
- Modify if needed: `docs/methodology/writing-to-skills-map.md`

- [x] 检查触发描述是否对应可识别的具体工作，不靠宽泛“管理”关键词唤起。
- [x] 保留每篇个人写作对应的方法与边界；八个复盘判断仍为选择性分析视角。
- [x] 五项 Skill 入口已表达具体工作任务；没有为了统一文案而改行为指令。
- [x] 保持可单独安装的 skill 不依赖仓库外共享文件才能理解关键行为。

### Task 4: 更新可发布项目介绍

**Files:**
- Modify: `docs/blog/project-module.md`
- Read: `docs/methodology/public-case-evaluation.md`
- Read: `docs/methodology/management-retro-evaluation.md`

- [x] 改为五项能力，并以一线工程判断为主线。
- [x] 更新 prompt 总数、配对样例数量、已知失败修复及评测限制。
- [x] 在发布备注中将 Codex 已验证和其他 Agent 尚未逐一验证说准确。

### Task 5: 行为验收和修订

**Files:**
- Read: `skills/*/evals/evals.json`
- Read: `docs/methodology/skills-portfolio-review.md`
- Create: `docs/methodology/2026-09-25-portfolio-acceptance.md`
- Modify: `README.md`

- [x] 复核五份 eval 套件共 38 项，每项至少有缺信息、冲突信息、正常任务案例。
- [x] 复核现有行为验收/评分和具体修复记录；本轮未修改 Skill 行为，故不将历史测试描述为本轮重新生成的输出。
- [x] 验收报告区分仓库静态校验、历史单轮行为记录和未验证的真实用户效果。

### Task 6: 完整性校验与最终验收

**Files:**
- Verify: all modified Markdown and JSON files

- [x] Run `python3 scripts/validate_repo.py`。
- [x] Run `git diff --check`。
- [x] 核对 README、博客、调研和评测中的数字一致性及内部链接。
- [x] 逐项映射设计验收标准并在最终报告列出证据、未验证项和风险。

---

## Plan self-review

- Spec coverage: positioning and boundaries (Tasks 2–3), source preservation (Task 3), stale publication claims (Task 4), behavioral evidence (Task 5), repository integrity (Task 6).
- Placeholders: none; “if needed” means the skill is edited only if the audit finds a concrete trigger or boundary defect, with the required eval-first cycle.
- Interfaces: README links remain repo-relative; standalone skills retain their own essential instructions and references.
- Review focus: all five input/quality risks have an explicit inspection or eval location.

## Execution record

- Ruling: do not expand the `skills/` tree or add a sixth skill — the author's clarification says the five existing concrete workflows are the intended product, and current independent-install boundaries work; cost if wrong: a future unmet workflow will require a separate proposal.
- Ruling: do not change Skill behavior files or rerun model outputs for this documentation-only positioning revision — existing behavior records cover all five skills and no behavioral instruction changed; cost if wrong: stale behavior issues could remain until a skill edit or fresh user case exposes them.
- Verification: 38 eval prompts parsed; all five skills have missing/conflict/normal case coverage. `python3 scripts/validate_repo.py` passed and `git diff --check` passed.
- Final review: self-review (no subagent reviewer used); this is weaker than an independent fresh-context review.
