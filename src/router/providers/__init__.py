"""提供商配置模块"""
from .anthropic import ANTHROPIC_MODELS
from .openai import OPENAI_MODELS
from .google import GOOGLE_MODELS
from .qwen import QWEN_MODELS
from .zhipu import ZHIPU_MODELS
from .baichuan import BAICHUAN_MODELS

__all__ = [
    "ANTHROPIC_MODELS",
    "OPENAI_MODELS",
    "GOOGLE_MODELS",
    "QWEN_MODELS",
    "ZHIPU_MODELS",
    "BAICHUAN_MODELS",
]
