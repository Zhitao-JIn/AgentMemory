"""获取所有记忆实现"""
from typing import Any, Dict, List

from src.memory.add_memory import _memories


def get_all_memories() -> List[Dict[str, Any]]:
    """获取所有记忆"""
    return _memories.copy()
