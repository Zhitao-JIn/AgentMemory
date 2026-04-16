# memory/update_context.py - 更新上下文

## 文件职责

根据近期数据主动更新上下文摘要。

## 函数列表

### update_context
```python
def update_context(
    data: Dict[str, Any],
    add_fn: callable,
    get_context_fn: callable = None,
) -> Dict[str, Any]
```

**流程**:
1. 添加新记忆
2. 获取上下文摘要
3. 返回增强后的上下文

### get_context
```python
def get_context(
    memories: List[Dict[str, Any]],
    recent_count: int = 5,
) -> Dict[str, Any]
```

**功能**: 获取最近 N 条记忆作为上下文摘要。
