"""Router 层 - 多 AI 提供商路由"""
from .layer import RouterLayer
from .router import get_model, route_request, MODEL_MAP, PROVIDER_ALIASES
from .strategies import type_based_route, auto_route
from .litellm_client import call_litellm

__all__ = [
    "RouterLayer",
    "get_model",
    "route_request",
    "MODEL_MAP",
    "PROVIDER_ALIASES",
    "type_based_route",
    "auto_route",
    "call_litellm",
]
