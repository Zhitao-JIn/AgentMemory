"""OpenAI 提供商配置"""

OPENAI_MODELS = {
    "high": {
        "model": "gpt-4.5-preview",
        "max_tokens": 4096,
        "description": "OpenAI 旗舰模型，适合复杂任务",
    },
    "medium": {
        "model": "gpt-4o",
        "max_tokens": 4096,
        "description": "OpenAI 性价比模型，平衡性能与成本",
    },
    "low": {
        "model": "gpt-4o-mini",
        "max_tokens": 4096,
        "description": "OpenAI 快速模型，适合简单任务",
    },
}
