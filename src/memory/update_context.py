"""记忆层 - 更新上下文的方法"""
from typing import Any, Dict, List


def update_context(
    data: Dict[str, Any],
    add_fn: callable,
    get_context_fn: callable = None,
) -> Dict[str, Any]:
    """根据近期数据主动更新上下文

    流程：
    1. 添加新记忆
    2. 维护上下文摘要
    3. 返回增强后的上下文
    """
    # 1. 添加记忆
    add_fn(data.get("content", str(data)), meta=data.get("intent", {}))

    # 2. 获取当前上下文摘要
    context = get_context_fn() if get_context_fn else {}

    # 3. 返回增强后的上下文
    return {**data, **context}


def get_context(
    memories: List[Dict[str, Any]],
    recent_count: int = 5,
) -> Dict[str, Any]:
    """获取近期记忆作为上下文摘要"""
    recent = memories[-recent_count:] if len(memories) > recent_count else memories
    content_summary = "\n".join([m.get("content", "") for m in recent])
    return {"recent_context": content_summary, "memory_count": len(memories)}
