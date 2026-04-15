"""记忆层 - 存储检索协议"""
from typing import Any, Callable, Dict, List, Optional

from src.protocols.interfaces import IMemory
from src.tools.logger import get_logger

logger = get_logger("MemoryLayer")


class MemoryLayer(IMemory):
    """记忆层：协调记忆操作"""

    def __init__(
        self,
        add_fn: Callable[[str, Optional[Dict]], None],
        search_fn: Callable[[str], List[Dict[str, Any]]],
        get_all_fn: Callable[[], List[Dict[str, Any]]],
        update_context_fn: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None,
        handle_query_fn: Optional[Callable[[str, Dict[str, Any]], Dict[str, Any]]] = None,
        receive_feedback_fn: Optional[Callable[[str, Dict[str, Any]], None]] = None,
    ):
        self._add = add_fn
        self._search = search_fn
        self._get_all = get_all_fn
        self._update_context = update_context_fn
        self._handle_query = handle_query_fn
        self._receive_feedback = receive_feedback_fn

    def add(self, content: str, meta: Optional[Dict] = None) -> None:
        """添加记忆"""
        logger.info("add")
        logger.debug(f"add - 参数：content={content!r}, meta={meta!r}")
        self._add(content, meta)

    def search(self, query: str) -> List[Dict[str, Any]]:
        """搜索记忆"""
        logger.info("search")
        logger.debug(f"search - 参数：query={query!r}")
        result = self._search(query)
        logger.debug(f"search - 返回：{len(result)} 条结果")
        return result

    def get_all(self) -> List[Dict[str, Any]]:
        """获取所有记忆"""
        logger.info("get_all")
        result = self._get_all()
        logger.debug(f"get_all - 返回：{len(result)} 条记忆")
        return result

    def update_context(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """根据近期数据主动更新上下文"""
        logger.info("update_context")
        logger.debug(f"update_context - 参数：data={data!r}")
        if self._update_context:
            result = self._update_context(data)
            logger.debug(f"update_context - 返回：{result!r}")
            return result
        # 默认实现：只添加记忆，返回原数据
        self.add(data.get("content", str(data)), meta=data.get("intent", {}))
        logger.debug(f"update_context - 返回：{data!r}")
        return data

    def handle_query_request(
        self,
        query_type: str,
        params: Dict[str, Any],
    ) -> Dict[str, Any]:
        """处理来自推理层的查询请求（支持工具化执行）"""
        logger.info(f"handle_query_request - query_type={query_type}")
        logger.debug(f"handle_query_request - 参数：query_type={query_type!r}, params={params!r}")
        if self._handle_query:
            result = self._handle_query(query_type, params)
            logger.debug(f"handle_query_request - 返回：{result!r}")
            return result
        # 默认实现
        if query_type == "context":
            query = params.get("query", "")
            results = self.search(query)
            result = {
                "retrieved_context": "\n".join([m["content"] for m in results[:3]]) if results else "无相关记忆",
                "memory_count": len(results),
            }
            logger.debug(f"handle_query_request - 返回：{result!r}")
            return result
        result = {"error": f"Unknown query type: {query_type}"}
        logger.debug(f"handle_query_request - 返回：{result!r}")
        return result

    def get_context(self) -> Dict[str, Any]:
        """获取当前维护的上下文摘要"""
        logger.info("get_context")
        memories = self.get_all()
        recent = memories[-5:] if len(memories) > 5 else memories
        content_summary = "\n".join([m.get("content", "") for m in recent])
        result = {"recent_context": content_summary, "memory_count": len(memories)}
        logger.debug(f"get_context - 返回：{result!r}")
        return result

    def receive_feedback(
        self,
        feedback_type: str,
        content: Dict[str, Any],
    ) -> None:
        """接收来自推理层的反馈（如：信息过载、实体缺失等）"""
        logger.info(f"receive_feedback - feedback_type={feedback_type}")
        logger.debug(f"receive_feedback - 参数：feedback_type={feedback_type!r}, content={content!r}")
        if self._receive_feedback:
            self._receive_feedback(feedback_type, content)
        # 默认实现：无操作
