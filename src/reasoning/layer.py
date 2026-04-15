"""推理层 - 协调推理流程"""
from typing import Any, Callable, Dict, Optional

from src.protocols.interfaces import IReasoning, IMemory
from src.tools.logger import get_logger

logger = get_logger("ReasoningLayer")


class ReasoningLayer(IReasoning):
    """推理层：协调推理流程"""

    def __init__(
        self,
        analyze_fn: Callable[[Dict[str, Any]], Dict[str, Any]],
        retrieve_fn: Callable[[Dict[str, Any], IMemory], Dict[str, Any]],
        generate_fn: Callable[[Dict[str, Any]], str],
        memory: Optional[IMemory] = None,
        query_memory_fn: Optional[Callable[[str, Dict[str, Any]], Dict[str, Any]]] = None,
        provide_feedback_fn: Optional[Callable[[str, Dict[str, Any]], None]] = None,
        run_fn: Optional[Callable[[Dict[str, Any], Any, IMemory], str]] = None,
    ):
        self._analyze = analyze_fn
        self._retrieve = retrieve_fn
        self._generate = generate_fn
        self._memory = memory
        self._query_memory = query_memory_fn
        self._provide_feedback = provide_feedback_fn
        self._run = run_fn

    def analyze(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """分析输入"""
        logger.info("analyze")
        logger.debug(f"analyze - 参数：input_data={input_data!r}")
        result = self._analyze(input_data)
        logger.debug(f"analyze - 返回：{result!r}")
        return result

    def retrieve(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """检索记忆"""
        logger.info("retrieve")
        logger.debug(f"retrieve - 参数：context={context!r}")
        if self._memory is None:
            result = {"retrieved_context": "无相关记忆", "memory_count": 0, **context}
            logger.debug(f"retrieve - 返回：{result!r} (无记忆层)")
            return result
        result = self._retrieve(context, self._memory)
        logger.debug(f"retrieve - 返回：{result!r}")
        return result

    def generate(self, context: Dict[str, Any]) -> str:
        """生成响应"""
        logger.info("generate")
        logger.debug(f"generate - 参数：context={context!r}")
        result = self._generate(context)
        logger.debug(f"generate - 返回：{result!r}")
        return result

    def query_memory(
        self,
        query_type: str,
        params: Dict[str, Any],
    ) -> Dict[str, Any]:
        """向记忆层发起指导性查询请求"""
        logger.info(f"query_memory - query_type={query_type}")
        logger.debug(f"query_memory - 参数：query_type={query_type!r}, params={params!r}")
        if self._query_memory:
            result = self._query_memory(query_type, params)
            logger.debug(f"query_memory - 返回：{result!r}")
            return result
        # 默认实现：直接调用记忆层
        if self._memory:
            result = self._memory.handle_query_request(query_type, params)
            logger.debug(f"query_memory - 返回：{result!r}")
            return result
        result = {"error": "No memory layer"}
        logger.debug(f"query_memory - 返回：{result!r}")
        return result

    def provide_feedback(
        self,
        feedback_type: str,
        content: Dict[str, Any],
    ) -> None:
        """向记忆层提供反馈"""
        logger.info(f"provide_feedback - feedback_type={feedback_type}")
        logger.debug(f"provide_feedback - 参数：feedback_type={feedback_type!r}, content={content!r}")
        if self._provide_feedback:
            self._provide_feedback(feedback_type, content)
        # 默认实现：直接调用记忆层
        if self._memory:
            self._memory.receive_feedback(feedback_type, content)

    def run(self, context: Dict[str, Any]) -> str:
        """执行完整推理流程：分析 + 查询 + 生成"""
        logger.info("run")
        logger.debug(f"run - 参数：context={context!r}")
        if self._run:
            result = self._run(context, self._memory)
            logger.debug(f"run - 返回：{result!r}")
            return result
        # 默认实现：分析 + 检索 + 生成
        analyzed = self._analyze(context)
        retrieved = self.retrieve(analyzed)
        result = self._generate(retrieved)
        logger.debug(f"run - 返回：{result!r}")
        return result
