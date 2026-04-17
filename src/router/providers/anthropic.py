"""Anthropic 提供商配置"""

ANTHROPIC_MODELS = {
    "high": {
        "model": "claude-opus-4-0",
        "max_tokens": 4096,
        "description": "Anthropic 旗舰模型，适合复杂任务",
    },
    "medium": {
        "model": "claude-sonnet-4-0",
        "max_tokens": 4096,
        "description": "Anthropic 性价比模型，平衡性能与成本",
    },
    "low": {
        "model": "claude-haiku-4-0",
        "max_tokens": 4096,
        "description": "Anthropic 快速模型，适合简单任务",
    },
}
