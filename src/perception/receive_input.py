"""感知层 - 接收输入并执行完整流程的方法"""
from typing import Any, Dict


def receive_input(
    raw_input: str,
    process_fn: callable,
    extract_fn: callable,
    reasoning_layer: Any = None,
    action_layer: Any = None,
) -> str:
    """接收用户输入，执行完整流程并返回结果

    流程：
    1. 处理输入 + 提取意图
    2. 发送给推理层分析
    3. 接收推理结果并执行行动
    4. 返回最终输出
    """
    # 1. 处理输入
    processed = process_fn(raw_input)
    processed["intent"] = extract_fn(processed)

    # 2. 发送消息给推理层
    if reasoning_layer:
        response = reasoning_layer.analyze(processed)
    else:
        response = "未连接到推理层"

    # 3. 发送消息给行动层获取最终输出
    if action_layer:
        output = action_layer.execute(response)
    else:
        output = response

    return output
