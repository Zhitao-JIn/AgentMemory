"""输入处理实现"""
from typing import Any, Dict


def process_input(raw_input: str) -> Dict[str, Any]:
    """处理原始输入"""
    cleaned = raw_input.strip()
    return {
        "content": cleaned,
        "length": len(cleaned),
        "meta": {},
    }
