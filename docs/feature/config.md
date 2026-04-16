# config.py - 配置管理

## 文件职责

使用 Pydantic 管理 AI Agent 的全局配置。

## 配置项

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `log_level` | str | "INFO" | 日志级别 (ERROR/INFO/DEBUG) |
| 模型参数 | - | - | LLM 相关配置 |
| 存储路径 | - | - | 记忆存储路径 |

## 使用方式

```python
from src.config import config

# 访问配置
level = config.log_level
```
