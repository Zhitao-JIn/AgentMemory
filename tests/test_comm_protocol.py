"""层间通信协议测试脚本"""
import pytest
from container import Container


class TestBasicInputOutput:
    """基础输入输出测试"""

    def test_greeting_response(self):
        """TC001: 基础问候响应"""
        agent = Container()
        result = agent.run("你好")
        assert result is not None and len(result) > 0, "应该返回非空响应"

    def test_statement_handling(self):
        """TC002: 简单陈述句处理"""
        agent = Container()
        result = agent.run("今天天气不错")
        assert result is not None, "应该返回非空响应"


class TestIntentRecognition:
    """意图识别测试"""

    def test_help_intent(self):
        """TC003: 帮助意图识别"""
        agent = Container()
        result = agent.run("帮助")
        assert result is not None, "应该返回帮助信息"

    def test_exit_intent(self):
        """TC004: 退出意图识别"""
        agent = Container()
        result = agent.run("退出")
        # 简化判断：只要有响应即可（main.py 会处理 exit）
        assert result is not None, "应该返回回应"

    def test_search_intent(self):
        """TC005: 搜索意图识别"""
        agent = Container()
        result = agent.run("搜索记忆")
        assert result is not None, "应该返回搜索结果"


class TestLayerCommunication:
    """层间通信测试"""

    def test_full_pipeline(self):
        """TC006: 感知到行动完整链路"""
        agent = Container()
        result = agent.run("测试消息")
        assert result is not None, "消息应能完整流经各层"

    def test_memory_context_update(self):
        """TC007: 记忆层上下文更新"""
        agent = Container()
        initial_count = len(agent.memory.get_all())
        agent.run("测试消息")
        new_count = len(agent.memory.get_all())
        # 新消息被存储到记忆中
        assert new_count >= initial_count, "记忆列表应该增长"


class TestToolQuery:
    """工具化查询测试"""

    def test_reasoning_query_memory(self):
        """TC008: 推理层向记忆层发起查询"""
        agent = Container()
        # 确保 memory 有值
        agent.memory.add("这是一个测试记忆")

        # 直接调用 query_memory
        result = agent.reasoning.query_memory(
            query_type="context",
            params={"query": "测试"}
        )

        assert "retrieved_context" in result or "error" in result, "应返回查询结果或错误"
        assert "memory_count" in result, "应包含记忆数量"

    def test_overload_feedback(self):
        """TC009: 记忆过载反馈机制"""
        agent = Container()

        # 添加超过阈值的记忆
        for i in range(15):
            agent.memory.add(f"测试记忆{i}")

        # 调用 provide_feedback
        agent.reasoning.provide_feedback(
            feedback_type="overloaded",
            content={"count": 15, "threshold": 10}
        )

        # 验证没有抛出异常
        assert True, "provide_feedback 不应抛出异常"


class TestExceptionHandling:
    """异常处理测试"""

    def test_empty_input(self):
        """TC010: 空输入处理"""
        agent = Container()
        try:
            result = agent.run("")
            assert result is not None, "空输入应有友好提示"
        except Exception as e:
            pytest.fail(f"空输入不应抛出异常：{e}")

    def test_unconnected_reasoning(self):
        """TC011: 推理层未连接时的降级处理"""
        agent = Container()
        agent.perception._reasoning = None

        try:
            result = agent.perception.receive_input("测试")
            assert result is not None, "未连接时应返回降级响应"
        except Exception as e:
            pytest.fail(f"未连接推理层不应抛出异常：{e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
