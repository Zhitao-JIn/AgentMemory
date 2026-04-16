# perception/extract_intent.py - 意图提取

## 文件职责

通过关键词匹配提取用户输入的真实意图。

## 函数签名

```python
def extract_intent(data: Dict[str, Any]) -> str
```

## 支持的意图类型

- 帮助意图：帮助/帮忙/请问
- 退出意图：退出/再见/bye
- 搜索意图：搜索/查找
- 闲聊意图：其他
