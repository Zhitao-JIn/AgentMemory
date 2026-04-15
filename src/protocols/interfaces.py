"""全局接口定义 - 各层协议"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


# ============ 基础接口 ============

class IPerception(ABC):
    """感知层接口"""

    @abstractmethod
    def process(self, raw_input: str) -> Dict[str, Any]:
        """处理原始输入"""
        pass

    @abstractmethod
    def extract_intent(self, data: Dict[str, Any]) -> str:
        """提取意图"""
        pass

    @abstractmethod
    def receive_input(self, raw_input: str) -> str:
        """接收用户输入，执行完整流程并返回结果"""
        pass

    @abstractmethod
    def broadcast_to_reasoning(self, data: Dict[str, Any]) -> None:
        """将处理后的结果广播给推理层"""
        pass

    @abstractmethod
    def archive_to_memory(self, data: Dict[str, Any]) -> None:
        """将处理后的结果归档到记忆层"""
        pass


class IMemory(ABC):
    """记忆层接口"""

    @abstractmethod
    def add(self, content: str, meta: Optional[Dict] = None) -> None:
        """添加记忆"""
        pass

    @abstractmethod
    def search(self, query: str) -> List[Dict[str, Any]]:
        """搜索记忆"""
        pass

    @abstractmethod
    def get_all(self) -> List[Dict[str, Any]]:
        """获取所有记忆"""
        pass

    @abstractmethod
    def update_context(self, data: Dict[str, Any]) -> None:
        """根据近期数据主动更新上下文（由记忆层内部维护）"""
        pass

    @abstractmethod
    def get_context(self) -> Dict[str, Any]:
        """获取当前维护的上下文摘要"""
        pass

    @abstractmethod
    def handle_query_request(self, query_type: str, params: Dict[str, Any]) -> Any:
        """处理来自推理层的查询请求（支持工具化执行）"""
        pass

    @abstractmethod
    def receive_feedback(self, feedback_type: str, content: Dict[str, Any]) -> None:
        """接收来自推理层的反馈（如：信息过载、实体缺失等）"""
        pass

class IReasoning(ABC):
    """推理层接口"""

    @abstractmethod
    def analyze(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """分析输入"""
        pass

    @abstractmethod
    def retrieve(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """检索相关记忆"""
        pass

    @abstractmethod
    def generate(self, context: Dict[str, Any]) -> str:
        """生成响应"""
        pass

    @abstractmethod
    def query_memory(self, query_type: str, params: Dict[str, Any]) -> Any:
        """向记忆层发起指导性查询请求（通过工具实现）"""
        pass

    @abstractmethod
    def provide_feedback(self, feedback_type: str, content: Dict[str, Any]) -> None:
        """向记忆层提供反馈（如：xxx 记忆太多需要过滤、缺少 xxx 实体）"""
        pass


class IAction(ABC):
    """行动层接口"""

    @abstractmethod
    def execute(self, response: str) -> str:
        """执行输出"""
        pass


class ITool(ABC):
    """工具接口"""

    name: str

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """执行工具"""
        pass

class ICommsHub(ABC):
    """通信中枢接口 - 各层通过它进行消息传递"""

    @abstractmethod
    def send(self, from_layer: str, to_layer: str, message: Dict[str, Any]) -> None:
        """发送消息到指定层"""
        pass

    @abstractmethod
    def request(self, target: str, method: str, params: Dict[str, Any]) -> Any:
        """同步请求某层的某个方法"""
        pass
