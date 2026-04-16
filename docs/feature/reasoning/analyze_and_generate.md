# reasoning/analyze_and_generate.py - 分析并生成响应

## 文件职责

协调分析、记忆查询和响应生成的完整流程。

## 函数签名

```python
def analyze_and_generate(
    context: Dict[str, Any],
    query_fn: callable,
    generate_fn: callable,
    memory_layer: Any = None,
) -> str
```

## 执行流程

1. 调用记忆层更新上下文
2. 向记忆层发起查询请求
3. 检查是否需要反馈（记忆>10 条）
4. 生成并返回响应
