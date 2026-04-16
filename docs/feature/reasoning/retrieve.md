# reasoning/retrieve.py - 检索记忆

## 文件职责

根据上下文检索相关记忆。

## 函数签名

```python
def retrieve(context: Dict[str, Any], memory: IMemory) -> Dict[str, Any]
```

## 检索流程

1. 从上下文提取查询关键词
2. 调用记忆层搜索
3. 整合检索结果到上下文
