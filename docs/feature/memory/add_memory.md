# memory/add_memory.py - 添加记忆

## 文件职责

添加新记忆到存储并持久化。

## 函数签名

```python
def add_memory(content: str, meta: Optional[Dict] = None) -> None
```

## 处理流程

1. 创建记忆记录（含时间戳）
2. 添加到内存列表
3. 持久化到磁盘
