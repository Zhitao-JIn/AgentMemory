"""通信协议消息结构定义"""
from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from datetime import datetime


@dataclass
class Message:
    """层间通信消息结构"""

    type: str  # 消息类型
    from_layer: str  # 发送方
    to_layer: Optional[str] = None  # 接收方（None 表示广播）
    payload: Dict[str, Any] = field(default_factory=dict)  # 数据负载
    timestamp: float = field(default_factory=lambda: datetime.now().timestamp())  # 时间戳

    # 消息类型常量
    TYPE_INPUT = "input"
    TYPE_PROCESSED = "processed"
    TYPE_QUERIED = "queried"
    TYPE_RESPONSE = "response"
    TYPE_OUTPUT = "output"
