# AI Agent Learning

一个从零开始学习和构建 AI Agent 的 Python 项目。

## 当前功能

- AI 多轮对话
- 聊天上下文记忆
- Function Calling / Tool Calling
- 多工具自动选择
- 乘法计算工具
- 实时天气查询工具
- GitHub 用户信息查询工具
- 工具异常处理
- Tool Registry 工具注册机制

## 项目结构

```text
ai-agent-learning/
├── chat_history.py      # Agent 主程序
├── tools.py             # Python 工具函数
├── tool_schemas.py      # 提供给 AI 的工具定义
├── .gitignore
└── README.md
```
## Agent 工作流程

用户输入  
→ AI 判断是否需要工具  
→ Function Call  
→ Python 执行工具  
→ 返回执行结果  
→ AI 生成最终回答

## 已实现工具

### multiply
计算两个数字的乘法。

### weather
通过天气 API 查询城市当前温度。

### github_user
通过 GitHub API 查询用户的公开信息。

## 学习目标

- Python
- API
- AI Agent
- Git / GitHub
- FastAPI
- MySQL
- RAG
- LangGraph
- Docker
- 项目部署