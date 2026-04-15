"""配置管理"""
from pydantic import BaseModel


class Config(BaseModel):
    """Agent 配置"""

    # 模型配置
    model: str = "claude-sonnet-4-20250514"
    max_tokens: int = 1024
    temperature: float = 0.7

    # 记忆存储路径
    memory_path: str = "./data/memory_store.json"

    # 调试模式
    debug: bool = False


config = Config()
