"""感知层 - 输入处理协议"""
from typing import Any, Callable, Dict, Optional

from src.protocols.interfaces import IPerception
from src.tools.logger import get_logger

logger = get_logger("PerceptionLayer")


class PerceptionLayer(IPerception):
    """感知层：协调输入处理流程"""

    def __init__(
        self,
        process_fn: Callable[[str], Dict[str, Any]],
        extract_fn: Callable[[Dict[str, Any]], str],
        receive_input_fn: Callable[[str, Callable, Callable, Any, Any], str],
        reasoning_layer: Optional[Any] = None,
        action_layer: Optional[Any] = None,
    ):
        self._process = process_fn
        self._extract_intent = extract_fn
        self._receive_input_fn = receive_input_fn
        self._reasoning = reasoning_layer
        self._action = action_layer

    def process(self, raw_input: str) -> Dict[str, Any]:
        """处理原始输入"""
        logger.info("process")
        logger.debug(f"process - 参数：raw_input={raw_input!r}")
        result = self._process(raw_input)
        logger.debug(f"process - 返回：{result!r}")
        return result

    def extract_intent(self, data: Dict[str, Any]) -> str:
        """提取意图"""
        logger.info("extract_intent")
        logger.debug(f"extract_intent - 参数：data={data!r}")
        result = self._extract_intent(data)
        logger.debug(f"extract_intent - 返回：{result!r}")
        return result

    def receive_input(self, raw_input: str) -> str:
        """接收用户输入，执行完整流程并返回结果"""
        logger.info("receive_input")
        logger.debug(f"receive_input - 参数：raw_input={raw_input!r}")
        result = self._receive_input_fn(
            raw_input=raw_input,
            process_fn=self._process,
            extract_fn=self._extract_intent,
            reasoning_layer=self._reasoning,
            action_layer=self._action,
        )
        logger.debug(f"receive_input - 返回：{result!r}")
        return result

    def broadcast_to_reasoning(self, data: Dict[str, Any]) -> None:
        """将处理后的结果广播给推理层"""
        logger.info("broadcast_to_reasoning")
        logger.debug(f"broadcast_to_reasoning - 参数：data={data!r}")
        if self._reasoning:
            self._reasoning.analyze(data)

    def archive_to_memory(self, data: Dict[str, Any]) -> None:
        """将处理后的结果归档到记忆层"""
        logger.info("archive_to_memory")
        logger.debug(f"archive_to_memory - 参数：data={data!r}")
        content = data.get("content", str(data))
        meta = data.get("intent", {})
        if hasattr(self, '_add'):
            self._add(content, meta)
