"""推理层 - 分析输入并发起记忆查询的方法"""
from typing import Any, Dict


def analyze(
    context: Dict[str, Any],
    query_fn: callable,
    generate_fn: callable,
    memory_layer: Any = None,
) -> str:
    """分析上下文并生成响应

    流程：
    1. 记忆层更新上下文
    2. 向记忆层发起查询请求
    3. 结合结果生成响应
    """
    # 1. 记忆层更新上下文（主动维护）
    if memory_layer:
        context = memory_layer.update_context(context)

    # 2. 向记忆层发起查询请求
    retrieved = query_fn(
        query_type="context",
        params={"query": context.get("content", "")}
    )

    # 3. 检查是否需要提供反馈
    if retrieved.get("memory_count", 0) > 10:
        memory_layer.provide_feedback(
            feedback_type="overloaded",
            content={"count": retrieved["memory_count"], "threshold": 10}
        )

    # 4. 生成响应
    response = generate_fn(context)

    return response
