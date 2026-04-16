"""Type 路由策略"""

def type_based_route(provider: str, model_type: str, get_model_fn: callable) -> str:
    """基于 type 字段的路由"""
