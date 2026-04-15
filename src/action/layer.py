"""行动层 - 输出执行协议"""
from typing import Any, Callable

from src.protocols.interfaces import IAction
from src.tools.logger import get_logger

logger = get_logger("ActionLayer")


class ActionLayer(IAction):
    """行动层：协调输出执行"""

    def __init__(self, execute_fn: Callable[[str], str]):
        self._execute = execute_fn

    def execute(self, response: str) -> str:
        """执行输出"""
        logger.info("execute")
        logger.debug(f"execute - 参数：response={response!r}")
        result = self._execute(response)
        logger.debug(f"execute - 返回：{result!r}")
        return result
