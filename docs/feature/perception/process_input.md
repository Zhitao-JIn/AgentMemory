# perception/process_input.py - 输入处理

## 文件职责

处理原始用户输入，清洗和标准化。

## 函数签名

```python
def process_input(raw_input: str) -> Dict[str, Any]
```

## 处理流程

1. 去除首尾空格
2. 标准化编码
3. 返回结构化数据
