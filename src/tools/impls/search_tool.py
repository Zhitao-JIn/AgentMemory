"""内置工具示例 - 搜索工具"""
from src.tools.base import BaseTool


class SearchTool(BaseTool):
    """示例搜索工具"""

    name = "search"
    description = "搜索信息"

    def execute(self, query: str, **kwargs) -> str:
        """执行搜索"""
        return f"搜索结果：{query}"


# 自动注册
SearchTool()  # 需要手动注册到 ToolRegistry
