# reasoning/generate.py - 生成响应

## 文件职责

根据上下文生成自然语言响应。

## 函数签名

```python
def generate_response(context: Dict[str, Any]) -> str
```

## 生成逻辑

1. 整合分析结果和检索记忆
2. 生成连贯响应
3. 返回响应字符串
