"""搜索记忆实现"""
from typing import Any, Dict, List

from src.memory.add_memory import _memories


def search_memory(query: str) -> List[Dict[str, Any]]:
    """关键词搜索记忆"""
    query = query.lower()
    return [m for m in _memories if query in m["content"].lower()]
