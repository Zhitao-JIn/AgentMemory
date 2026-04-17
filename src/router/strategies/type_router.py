"""Type 路由策略 - 根据 type 字段选择模型层级"""
from typing import Optional


def type_based_route(
    provider: str,
    model_type: str,
    get_model_fn: callable,
) -> str:
    """基于 type 字段的路由

    Args:
        provider: 提供商名称
        model_type: 模型层级 (high/medium/low)
        get_model_fn: 获取模型的函数

    Returns:
        模型名称
    """
    return get_model_fn(provider, model_type)
