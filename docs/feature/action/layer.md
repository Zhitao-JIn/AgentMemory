# action/layer.py - 行动层协议

## 文件职责

ActionLayer 类，协调输出执行。

## 依赖注入

| 注入项 | 类型 | 说明 |
|--------|------|------|
| `execute_fn` | Callable | 执行输出 |

## 方法

- `execute(response)` → str - 执行并格式化输出
