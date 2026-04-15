"""检索实现"""
from typing import Any, Dict, List

from src.protocols.interfaces import IMemory


def retrieve(context: Dict[str, Any], memory: IMemory) -> Dict[str, Any]:
    """检索相关记忆"""
    query = context.get("content", "")
    memories = memory.search(query)

    # 取前 3 条相关记忆
    context_text = "\n".join([m["content"] for m in memories[:3]]) if memories else "无相关记忆"

    return {
        **context,
        "retrieved_context": context_text,
        "memory_count": len(memories),
    }
