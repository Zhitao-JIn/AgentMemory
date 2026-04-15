"""依赖注入容器 - 组装各层"""
from typing import Optional

from src.protocols.interfaces import IPerception, IMemory, IReasoning, IAction
from src.perception import PerceptionLayer
from src.memory import MemoryLayer, init_memory_storage
from src.reasoning import ReasoningLayer
from src.action import ActionLayer
from src.tools.logger import setup_logger

# 导入具体实现
from src.perception.process_input import process_input
from src.perception.extract_intent import extract_intent
from src.perception.receive_input import receive_input
from src.memory.add_memory import add_memory, init_memory_storage as init_mem
from src.memory.search_memory import search_memory
from src.memory.get_all import get_all_memories
from src.reasoning.analyze import analyze
from src.reasoning.retrieve import retrieve
from src.reasoning.generate import generate_response
from src.action.execute_output import execute_output


class Container:
    """DI 容器 - 组装所有依赖"""

    def __init__(self, memory_path: Optional[str] = None, log_level: str = "INFO"):
        # 配置日志
        setup_logger(log_level)

        # 初始化记忆存储
        init_mem(memory_path)

        # 记忆层（先创建，以便其他层注入）
        self.memory = MemoryLayer(
            add_fn=add_memory,
            search_fn=search_memory,
            get_all_fn=get_all_memories,
        )

        # 行动层（先创建，以便感知层注入）
        self.action = ActionLayer(
            execute_fn=execute_output,
        )

        # 推理层（依赖记忆层）
        self.reasoning = ReasoningLayer(
            analyze_fn=analyze,
            retrieve_fn=lambda ctx: retrieve(ctx, self.memory),
            generate_fn=generate_response,
            memory=self.memory,
        )

        # 感知层（传递推理层和行动层引用）
        self.perception = PerceptionLayer(
            process_fn=process_input,
            extract_fn=extract_intent,
            receive_input_fn=receive_input,
            reasoning_layer=self.reasoning,
            action_layer=self.action,
        )

    def run(self, user_input: str) -> str:
        """向 Agent 发送输入，等待完整流程后返回结果"""
        return self.perception.receive_input(user_input)
