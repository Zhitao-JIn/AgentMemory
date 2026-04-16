# memory/search_memory.py - 搜索记忆

## 文件职责

通过关键词匹配搜索相关记忆。

## 函数签名

```python
def search_memory(query: str) -> List[Dict[str, Any]]
```

## 搜索算法

1. 遍历所有记忆
2. 关键词匹配（不区分大小写）
3. 返回匹配的记忆列表
