"""工具注册中心"""
from typing import Any, Dict, List, Optional
from src.tools.base import BaseTool


class ToolRegistry:
    """全局工具注册表"""

    _tools: Dict[str, BaseTool] = {}

    @classmethod
    def register(cls, tool: BaseTool) -> None:
        """注册工具"""
        cls._tools[tool.name] = tool

    @classmethod
    def get(cls, name: str) -> Optional[BaseTool]:
        """获取工具"""
        return cls._tools.get(name)

    @classmethod
    def list_tools(cls) -> List[str]:
        """列出所有工具"""
        return list(cls._tools.keys())

    @classmethod
    def execute(cls, name: str, **kwargs) -> Any:
        """执行工具"""
        tool = cls.get(name)
        if tool is None:
            raise ValueError(f"Tool not found: {name}")
        return tool.execute(**kwargs)
