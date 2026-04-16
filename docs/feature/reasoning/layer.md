# reasoning/layer.py - 推理层协议

## 文件职责

ReasoningLayer 类，协调推理流程（分析→检索→生成）。

## 依赖注入

| 注入项 | 类型 | 说明 |
|--------|------|------|
| `analyze_fn` | Callable | 分析输入 |
| `retrieve_fn` | Callable | 检索记忆 |
| `generate_fn` | Callable | 生成响应 |
| `memory` | IMemory | 记忆层引用 |
| `query_memory_fn` | Callable | 查询记忆 |
| `provide_feedback_fn` | Callable | 提供反馈 |
| `run_fn` | Callable | 完整流程 |

## 方法

- `analyze(input_data)` → Dict - 分析输入
- `retrieve(context)` → Dict - 检索记忆
- `generate(context)` → str - 生成响应
- `query_memory(query_type, params)` → Dict - 查询记忆
- `provide_feedback(feedback_type, content)` → None - 提供反馈
- `run(context)` → str - 完整推理流程
