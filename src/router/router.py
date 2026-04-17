"""路由核心逻辑 - type 到 model 的映射"""
from typing import Dict, Optional, Callable

# 模型映射表：provider -> type -> model
MODEL_MAP: Dict[str, Dict[str, str]] = {
    "anthropic": {
        "high": "claude-opus-4-0",
        "medium": "claude-sonnet-4-0",
        "low": "claude-haiku-4-0",
    },
    "openai": {
        "high": "gpt-4.5-preview",
        "medium": "gpt-4o",
        "low": "gpt-4o-mini",
    },
    "google": {
        "high": "gemini-2.0-ultra",
        "medium": "gemini-2.0-pro",
        "low": "gemini-2.0-flash",
    },
    "bedrock": {
        "high": "anthropic.claude-3-opus-20240229-v1:0",
        "medium": "anthropic.claude-3-sonnet-20240229-v1:0",
        "low": "anthropic.claude-3-haiku-20240307-v1:0",
    },
    "azure": {
        "high": "azure/gpt-4.5",
        "medium": "azure/gpt-4o",
        "low": "azure/gpt-4o-mini",
    },
    "groq": {
        "high": "groq/llama-3.3-70b-versatile",
        "medium": "groq/llama-3.1-70b-instant",
        "low": "groq/llama-3.1-8b-instant",
    },
    "deepseek": {
        "high": "deepseek-chat",
        "medium": "deepseek-chat",
        "low": "deepseek-coder",
    },
    "ollama": {
        "high": "ollama/llama3.1:70b",
        "medium": "ollama/llama3.1:8b",
        "low": "ollama/phi3:3.8b",
    },
    # 国内模型提供商
    "qwen": {
        "high": "qwen3-max",
        "medium": "qwen3.5-plus",
        "low": "qwen3.5-flash",
    },
    "zhipu": {
        "high": "glm-z1",
        "medium": "glm-4",
        "low": "glm-3-turbo",
    },
    "baichuan": {
        "high": "baichuan2-128k",
        "medium": "baichuan2",
        "low": "baichuan2-turbo",
    },
    "lingyi": {
        "high": "yi-34b",
        "medium": "yi-large",
        "low": "yi-medium",
    },
    "minimax": {
        "high": "abab6.5",
        "medium": "abab5.5",
        "low": "abab4",
    },
    "sensechat": {
        "high": "sensechat-5",
        "medium": "sensechat-4",
        "low": "sensechat-3",
    },
}

# 提供商别名
PROVIDER_ALIASES: Dict[str, str] = {
    "claude": "anthropic",
    "gpt": "openai",
    "gemini": "google",
    "aws": "bedrock",
    # 国内模型别名
    "qwen": "qwen",
    "tongyi": "qwen",
    "通义": "qwen",
    "deepseek": "deepseek",
    "智谱": "zhipu",
    "zhipu": "zhipu",
    "glm": "zhipu",
    "baichuan": "baichuan",
    "百川": "baichuan",
    "yi": "lingyi",
    "零一": "lingyi",
    "minimax": "minimax",
}


def get_model(provider: str, type: str) -> str:
    """获取模型名称

    Args:
        provider: 提供商名称 (支持别名)
        type: 模型层级 (high/medium/low)

    Returns:
        模型名称
    """
    # 解析别名
    provider = PROVIDER_ALIASES.get(provider, provider)

    # 获取模型
    provider_models = MODEL_MAP.get(provider)
    if not provider_models:
        # 默认返回 anthropic
        provider = "anthropic"
        provider_models = MODEL_MAP[provider]

    model = provider_models.get(type, provider_models["medium"])
    return model


def route_request(
    provider: str,
    model_type: str,
    get_model_fn: Optional[Callable] = None,
    auto_fn: Optional[Callable] = None,
    input_text: Optional[str] = None,
) -> str:
    """路由请求到指定模型

    Args:
        provider: 提供商名称
        model_type: 模型层级 (high/medium/low/auto)
        get_model_fn: 获取模型的函数
        auto_fn: 智能路由函数
        input_text: 输入文本（用于智能路由）

    Returns:
        模型名称
    """
    # 智能路由
    if model_type == "auto" and auto_fn and input_text:
        return auto_fn(input_text, provider, get_model_fn)

    # 默认使用 get_model
    if get_model_fn:
        return get_model_fn(provider, model_type)

    return get_model(provider, model_type)
