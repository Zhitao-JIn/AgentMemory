"""日志工具 - 使用 loguru"""
from loguru import logger
import sys


def setup_logger(level: str = "INFO") -> None:
    """配置日志级别

    Args:
        level: 日志级别 (ERROR, INFO, DEBUG)
    """
    logger.remove()
    logger.add(
        sys.stderr,
        level=level.upper(),
        format="{time:HH:mm:ss} [{level}] [{name}] {message}",
    )


def get_logger(name: str = __name__):
    """获取日志记录器"""
    return logger.bind(name=name)


__all__ = ["setup_logger", "get_logger", "logger"]
