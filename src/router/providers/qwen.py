"""Qwen/通义千问 提供商配置"""

QWEN_MODELS = {
    "high": {
        "model": "qwen3-max",
        "max_tokens": 256000,
        "description": "Qwen3-Max - 适合复杂任务，能力最强",
    },
    "medium": {
        "model": "qwen3.5-plus",
        "max_tokens": 128000,
        "description": "Qwen3.5-Plus - 效果、速度、成本均衡",
    },
    "low": {
        "model": "qwen3.5-flash",
        "max_tokens": 64000,
        "description": "Qwen3.5-Flash - 适合简单任务，速度快、成本低",
    },
}

# 支持上下文长度
QWEN_CONTEXT_LENGTHS = {
    "qwen3-max": 256000,
    "qwen3.6-plus": 128000,
    "qwen3.5-flash": 64000,
}
