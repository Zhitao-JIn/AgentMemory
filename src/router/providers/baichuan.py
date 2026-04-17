"""百川/Baichuan 提供商配置"""

BAICHUAN_MODELS = {
    "high": {
        "model": "baichuan2-128k",
        "max_tokens": 131072,
        "description": "百川旗舰模型，支持 128k 上下文",
    },
    "medium": {
        "model": "baichuan2",
        "max_tokens": 32768,
        "description": "百川性价比模型",
    },
    "low": {
        "model": "baichuan2-turbo",
        "max_tokens": 8192,
        "description": "百川快速模型",
    },
}
