"""分析实现"""
from typing import Any, Dict


def analyze(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """分析输入数据"""
    content = input_data.get("content", "")
    intent = input_data.get("intent", "general")

    return {
        "content": content,
        "intent": intent,
        "length": len(content),
    }
