"""Router 层 - 多 AI 提供商路由"""
from typing import Dict, List, Optional, Any

from src.protocols.interfaces import IRouter


class RouterLayer(IRouter):
    """Router 层：协调多提供商路由"""

    def __init__(
        self,
        route_fn: callable,
        get_model_fn: callable,
        completion_fn: callable,
        default_provider: str = "anthropic",
        default_type: str = "medium",
    ):
        self._route = route_fn
        self._get_model = get_model_fn
        self._completion = completion_fn
        self._default_provider = default_provider
        self._default_type = default_type

    def route(
        self,
        provider: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs,
    ) -> str:
        """路由到指定提供商和层级的模型"""
        provider = provider or self._default_provider
        model_type = type or self._default_type
        return self._route(provider, model_type, **kwargs)

    def get_model(self, provider: str, type: str) -> str:
        """获取模型名称"""
        return self._get_model(provider, type)

    def completion(
        self,
        model: str,
        messages: List[Dict[str, str]],
        enable_thinking: Optional[bool] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """调用 LLM completion

        Args:
            model: 模型名称
            messages: 消息列表
            enable_thinking: 是否启用思考模式
            **kwargs: 其他参数

        Returns:
            LLM 响应字典
        """
        return self._completion(model, messages, enable_thinking=enable_thinking, **kwargs)

    def generate(
        self,
        prompt: str,
        provider: Optional[str] = None,
        type: Optional[str] = None,
        enable_thinking: Optional[bool] = None,
        **kwargs,
    ) -> str:
        """便捷方法：生成响应

        Args:
            prompt: 提示词
            provider: 提供商名称（可选，默认使用 config.default_provider）
            type: 模型层级 high/medium/low（可选，默认使用 config.default_type）
            enable_thinking: 是否启用思考模式（可选，默认使用 config 配置）
            **kwargs: 其他参数

        Returns:
            模型生成的响应
        """
        model = self.route(provider, type)
        messages = [{"role": "user", "content": prompt}]
        result = self.completion(model, messages, enable_thinking=enable_thinking, **kwargs)
        return result.get("choices", [{}])[0].get("message", {}).get("content", "")
