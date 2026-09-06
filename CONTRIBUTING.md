# CONTRIBUTING

欢迎贡献！本文件说明如何在本仓库中提出修改、参与讨论与提交合并请求。

主要流程：

1. 提案（RFC）
   - 在 proposals/ 下创建 RFC-XXXX-*.md（可先新建 Issue 讨论）。
   - RFC 应包含变更理由、精确修改建议（diff 或完整条文）、兼容性影响与表决建议。
2. 讨论阶段
   - 使用 GitHub Discussions 或 Issue 进行公开讨论。
   - 提案作者应在 14 天内回应重大意见。
3. PR 阶段
   - 当讨论成熟，由提案者或维护者提交 PR 修改 constitution/ 下的条款文件，PR 标题格式建议：RFC-XXXX: 简短标题。
   - PR 请关联对应的 Issue/Discussion/RFC 编号。
4. 表决与合并
   - 按 GOVERNANCE.md 中规定的阈值与流程进行表决。

格式与元数据：
- 条款文件采用 Markdown，文件顶部请使用 YAML front-matter，示例字段：
  - id, title, status, section, proposer, created_at, rationale, references

行为守则与贡献者须遵守 CODE_OF_CONDUCT.md。
