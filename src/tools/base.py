"""工具基类"""
from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """工具基类"""

    name: str = "base_tool"
    description: str = "Base tool"

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """执行工具逻辑"""
        pass
