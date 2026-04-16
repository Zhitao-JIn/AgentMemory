# memory/layer.py - 记忆层协议

## 文件职责

MemoryLayer 类，协调记忆存储和检索操作。

## 依赖注入

| 注入项 | 类型 | 说明 |
|--------|------|------|
| `add_fn` | Callable | 添加记忆 |
| `search_fn` | Callable | 搜索记忆 |
| `get_all_fn` | Callable | 获取所有记忆 |
| `update_context_fn` | Callable | 更新上下文 |
| `handle_query_fn` | Callable | 处理查询 |
| `receive_feedback_fn` | Callable | 接收反馈 |

## 方法

- `add(content, meta)` → None - 添加记忆
- `search(query)` → List - 搜索记忆
- `get_all()` → List - 获取所有记忆
- `update_context(data)` → Dict - 更新上下文
- `get_context()` → Dict - 获取上下文摘要
- `handle_query_request(query_type, params)` → Dict - 处理查询
- `receive_feedback(feedback_type, content)` → None - 接收反馈
