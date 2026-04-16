# perception/layer.py - 感知层协议

## 文件职责

PerceptionLayer 类，协调输入处理流程。

## 依赖注入

| 注入项 | 类型 | 说明 |
|--------|------|------|
| `process_fn` | Callable | 处理原始输入 |
| `extract_fn` | Callable | 提取意图 |
| `receive_input_fn` | Callable | 接收输入主流程 |
| `reasoning_layer` | Any | 推理层引用 |
| `action_layer` | Any | 行动层引用 |

## 方法

- `process(raw_input)` → Dict - 处理原始输入
- `extract_intent(data)` → str - 提取意图
- `receive_input(raw_input)` → str - 完整流程入口
- `broadcast_to_reasoning(data)` → None - 广播给推理层
- `archive_to_memory(data)` → None - 归档到记忆层
