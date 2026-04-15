"""执行输出实现"""
from typing import Any, Dict


def execute_output(response: Any) -> str:
    """执行输出（格式化）"""
    if isinstance(response, dict):
        return response.get("response", str(response))
    return str(response).strip()
