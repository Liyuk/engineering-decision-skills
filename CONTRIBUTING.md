# Contributing

感谢关注这个项目。它是一个小型、实验性的 Agent Skills 集合，贡献重点是让工程判断更清楚、更可验证，而不是不断增加管理场景。

## 适合贡献什么

- 能让一个 Skill 更准确区分事实、测量、估算、推断、假设和未知的改进。
- 能证明边界的正常、缺信息、冲突信息或反直觉 eval case。
- 真实但已匿名化的工程案例，且明确标注来源、演示设定和未知项。
- 能改善安装、发现、文档导航或跨环境验证的修改。

## 不建议提交什么

- 没有新触发条件或输出边界的泛管理 Skill。
- 为了填满模板而虚构数字、owner、因果关系或引用。
- 把评测 prompt 的单次结果描述成跨模型或真实业务效果。
- 把 review、retro、planning 和 reporting 合并成一个强制流程。

## 修改 Skill 的检查清单

1. 说明它解决的具体工程判断问题，以及不负责什么。
2. 保留证据状态、来源、时间窗口和未知项。
3. 至少补一个正常案例、一个缺信息案例和一个冲突信息案例。
4. 用 `agent/eval-rubric.md` 检查事实克制、任务匹配、可执行性、格式和语气。
5. 更新相关的 Skill 文档和当前入口；历史研究放入 `docs/archive/`，不要混入用户主路径。

## 本地验证

仓库不需要安装第三方依赖。提交前运行：

```sh
python3 -m unittest scripts/test_check_consistency.py -v
python3 scripts/check_consistency.py
python3 scripts/validate_repo.py
git diff --check
```

如果修改了共享规则，必须同时检查所有受影响的 Skill；如果移动 Skill 文件或本地引用，必须运行 `python3 scripts/validate_repo.py`。

## 提交说明

提交消息请说明实际改变的行为或入口，例如：

```text
docs: clarify metric-decision evidence boundary
test: add conflicting-denominator evaluation case
```

请在 Pull Request 中写清：改了什么、为什么需要、如何验证、哪些结论仍然没有证据支持。
