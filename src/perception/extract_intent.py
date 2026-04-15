"""意图提取实现"""
from typing import Any, Dict


def extract_intent(data: Dict[str, Any]) -> str:
    """基于关键词提取意图"""
    content = data.get("content", "").lower()

    intent_map = {
        "搜索": "search",
        "search": "search",
        "记忆": "memory",
        "memory": "memory",
        "帮助": "help",
        "help": "help",
        "退出": "exit",
        "quit": "exit",
    }

    for keyword, intent in intent_map.items():
        if keyword in content:
            return intent

    return "general"
