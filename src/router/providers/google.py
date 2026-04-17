"""Google 提供商配置"""

GOOGLE_MODELS = {
    "high": {
        "model": "gemini-2.0-ultra",
        "max_tokens": 8192,
        "description": "Google 旗舰模型，适合复杂任务",
    },
    "medium": {
        "model": "gemini-2.0-pro",
        "max_tokens": 8192,
        "description": "Google 性价比模型，平衡性能与成本",
    },
    "low": {
        "model": "gemini-2.0-flash",
        "max_tokens": 8192,
        "description": "Google 快速模型，适合简单任务",
    },
}
