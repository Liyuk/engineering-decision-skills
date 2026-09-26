# 历史资料与仓库一致性整理 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 整理历史资料的目录和入口，并增加当前 Skill/eval 元数据的一致性校验。

**Architecture:** 保持 `README.md`、`agent/`、`skills/` 和 `examples/` 为当前入口；只移动 `docs/archive/` 下的历史文件并增加索引。新增独立的标准库 Python 校验脚本，不改变既有 validator 的职责。

**Tech Stack:** Markdown, Python 3 标准库, Git 文件移动。

**Spec:** `docs/archive/decisions/2026-09-25-history-and-consistency-design.md`

## Global Constraints

- 保持五项 Skill 可独立安装。
- 不删除历史文本；移动文件时保留 Git 历史。
- 不引入第三方依赖或联网校验。
- 当前 eval 总数以仓库实际 JSON 为准，应为 39。
- 只有当前文档和发布草稿更新当前状态；历史快照保留其原始状态。

## Review Focus

- 旧目录移动后本地 Markdown 链接仍可解析：由 Task 1 的 validator 验证。
- 评测分类不能只看字符串猜测：由 Task 2 的分类规则和测试验证。
- 历史文档的旧数字不能污染当前统计：由 Task 2 的 archive exclusion 测试验证。
- Skill 缺少正常/缺信息/冲突案例时必须失败：由 Task 2 的 fixture 测试验证。
- 当前入口链接和归档索引不能指向不存在文件：由 Task 3 和完整校验验证。

### Task 1: 归档目录重排与导航

**Files:**
- Move: `docs/archive/blog/project-module.md` -> `docs/archive/publication/project-module.md`
- Move: `docs/archive/methodology/` evaluation records -> `docs/archive/evaluations/`
- Move: `docs/archive/methodology/writing-to-skills-map.md` -> `docs/archive/decisions/writing-to-skills-map.md`
- Move: `docs/archive/research/` remains in place
- Move: `docs/archive/superpowers/specs/` -> `docs/archive/decisions/`
- Move: `docs/archive/superpowers/plans/` -> `docs/archive/plans/`
- Create: `docs/archive/index.md`
- Modify: `docs/archive/README.md`
- Modify: moved Markdown links affected by the new relative paths

**Interfaces:**
- Produces: an archive tree whose categories describe content type and an index linking every archive file.

- [ ] **Step 1: Move files with Git-aware renames and update local links.**
- [ ] **Step 2: Add the archive index with status, date, type, and current-entry columns.**
- [ ] **Step 3: Update archive README to explain the new categories and historical snapshot rule.**
- [ ] **Step 4: Run `python3 scripts/validate_repo.py` and confirm all local links resolve.**
- [ ] **Step 5: Commit with `docs: reorganize historical archive`.**

### Task 2: Add consistency checker with tests first

**Files:**
- Create: `scripts/check_consistency.py`
- Create: `scripts/test_check_consistency.py`

**Interfaces:**
- Produces: executable `scripts/check_consistency.py` returning 0 for the current repository and non-zero with actionable errors for invalid fixtures.

- [ ] **Step 1: Write failing tests for current counts, required eval categories, stale archive exclusion, and broken README/index links.**
- [ ] **Step 2: Run `python3 -m unittest scripts/test_check_consistency.py -v` and verify the new checker/imports are missing or tests fail for the intended reason.**
- [ ] **Step 3: Implement small pure helpers for loading Skill evals, classifying case prompts/ids, checking local links, and reporting errors.**
- [ ] **Step 4: Run the focused unittest suite and verify all tests pass.**
- [ ] **Step 5: Run `python3 scripts/check_consistency.py` against the repository and verify a zero exit code.**
- [ ] **Step 6: Commit with `test: add repository consistency checks`.**

### Task 3: Correct current-facing metadata

**Files:**
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Modify: `docs/archive/publication/project-module.md`
- Modify: `docs/archive/README.md` or `docs/archive/index.md` if current-count references need alignment

**Interfaces:**
- Produces: current-facing documentation that says five Skills and 39 eval prompts, while historical snapshots remain time-qualified.

- [ ] **Step 1: Replace current stale counts and clarify that the fifth Skill is part of the unreleased/current working tree until a release is cut.**
- [ ] **Step 2: Add a small current-state inventory used by the consistency checker rather than scattering hardcoded counts.**
- [ ] **Step 3: Run both validators and focused tests.**
- [ ] **Step 4: Commit with `docs: align current repository metadata`.**

### Task 4: Final verification and review

**Files:**
- Review: all changed files

- [ ] **Step 1: Run `python3 scripts/test_check_consistency.py -v`.**
- [ ] **Step 2: Run `python3 scripts/check_consistency.py`.**
- [ ] **Step 3: Run `python3 scripts/validate_repo.py`.**
- [ ] **Step 4: Run `git diff --check` and inspect `git diff --stat` plus the full changed-file list.**
- [ ] **Step 5: Confirm no historical file was deleted and no current Skill boundary changed.**
