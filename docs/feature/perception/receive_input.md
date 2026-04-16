# perception/receive_input.py - 接收输入主流程

## 文件职责

接收用户输入，协调感知→推理→行动的完整流程。

## 函数签名

```python
def receive_input(
    raw_input: str,
    process_fn: callable,
    extract_fn: callable,
    reasoning_layer: Any = None,
    action_layer: Any = None,
) -> str
```

## 执行流程

1. 调用 `process_fn` 处理输入
2. 调用 `extract_fn` 提取意图
3. 发送给推理层分析
4. 调用行动层执行输出
5. 返回最终结果
