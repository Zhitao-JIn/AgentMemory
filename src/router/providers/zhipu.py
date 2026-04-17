"""智谱 AI/GLM 提供商配置"""

ZHIPU_MODELS = {
    "high": {
        "model": "glm-z1",
        "max_tokens": 32768,
        "description": "智谱 AI 旗舰模型，最强推理能力",
    },
    "medium": {
        "model": "glm-4",
        "max_tokens": 32768,
        "description": "智谱 AI 性价比模型，平衡性能与成本",
    },
    "low": {
        "model": "glm-3-turbo",
        "max_tokens": 8192,
        "description": "智谱 AI 快速模型，适合简单任务",
    },
}
