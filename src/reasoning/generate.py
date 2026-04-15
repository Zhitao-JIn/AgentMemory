"""生成响应实现"""
from typing import Any, Dict


def generate_response(context: Dict[str, Any]) -> str:
    """基于上下文生成响应"""
    intent = context.get("intent", "general")
    retrieved = context.get("retrieved_context", "")

    if intent == "help":
        return "帮助：输入 → 感知 → 记忆 → 推理 → 行动 → 输出"
    elif intent == "exit":
        return "exit"
    elif intent == "memory" and retrieved != "无相关记忆":
        return f"找到记忆:\n{retrieved}"
    else:
        content = context.get("content", "")
        return f"收到：{content}\n上下文：{retrieved}"
