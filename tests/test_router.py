"""Router 层测试脚本"""
import pytest
from src.router import get_model, route_request, auto_route, MODEL_MAP, PROVIDER_ALIASES


class TestTypeRouting:
    """Type 路由测试"""

    def test_anthropic_high_model(self):
        """TC001: Anthropic high 层级"""
        model = get_model("anthropic", "high")
        assert model == "claude-opus-4-0"

    def test_anthropic_medium_model(self):
        """TC001: Anthropic medium 层级"""
        model = get_model("anthropic", "medium")
        assert model == "claude-sonnet-4-0"

    def test_anthropic_low_model(self):
        """TC001: Anthropic low 层级"""
        model = get_model("anthropic", "low")
        assert model == "claude-haiku-4-0"

    def test_openai_high_model(self):
        """TC002: OpenAI high 层级"""
        model = get_model("openai", "high")
        assert model == "gpt-4.5-preview"

    def test_openai_medium_model(self):
        """TC002: OpenAI medium 层级"""
        model = get_model("openai", "medium")
        assert model == "gpt-4o"

    def test_openai_low_model(self):
        """TC002: OpenAI low 层级"""
        model = get_model("openai", "low")
        assert model == "gpt-4o-mini"

    def test_provider_alias_claude(self):
        """TC003: 提供商别名解析 - claude"""
        model = get_model("claude", "high")
        assert model == "claude-opus-4-0"

    def test_provider_alias_gpt(self):
        """TC003: 提供商别名解析 - gpt"""
        model = get_model("gpt", "high")
        assert model == "gpt-4.5-preview"

    def test_unknown_provider_fallback(self):
        """未知提供商降级到 anthropic"""
        model = get_model("unknown_provider", "high")
        assert "claude" in model


class TestDomesticProviders:
    """国内模型提供商测试"""

    def test_qwen_models(self):
        """测试 Qwen/通义千问模型"""
        assert get_model("qwen", "high") == "qwen3-max"
        assert get_model("qwen", "medium") == "qwen3.5-plus"
        assert get_model("qwen", "low") == "qwen3.5-flash"

    def test_qwen_aliases(self):
        """测试 Qwen 别名"""
        assert get_model("通义", "high") == "qwen3-max"
        assert get_model("tongyi", "high") == "qwen3-max"

    def test_zhipu_models(self):
        """测试智谱 GLM 模型"""
        assert get_model("zhipu", "high") == "glm-z1"
        assert get_model("zhipu", "medium") == "glm-4"
        assert get_model("zhipu", "low") == "glm-3-turbo"

    def test_zhipu_aliases(self):
        """测试智谱别名"""
        assert get_model("智谱", "high") == "glm-z1"
        assert get_model("glm", "high") == "glm-z1"

    def test_baichuan_models(self):
        """测试百川模型"""
        assert get_model("baichuan", "high") == "baichuan2-128k"
        assert get_model("baichuan", "medium") == "baichuan2"
        assert get_model("baichuan", "low") == "baichuan2-turbo"

    def test_lingyi_models(self):
        """测试零一万物模型"""
        assert get_model("lingyi", "high") == "yi-34b"
        assert get_model("yi", "high") == "yi-34b"

    def test_minimax_models(self):
        """测试 MiniMax 模型"""
        assert get_model("minimax", "high") == "abab6.5"


class TestAutoRouting:
    """智能路由测试"""

    def test_short_input_uses_low(self):
        """TC004: 短输入使用 low 层级"""
        short_text = "你好"  # 2 字
        model = auto_route(short_text, "anthropic", get_model)
        assert model == get_model("anthropic", "low")

    def test_medium_input_uses_medium(self):
        """TC005: 中等输入使用 medium 层级"""
        medium_text = "这是一段中等长度的输入文本，用于测试智能路由是否能正确选择中端模型。" * 2  # 约 60 字
        model = auto_route(medium_text, "anthropic", get_model)
        assert model == get_model("anthropic", "medium")

    def test_long_input_uses_high(self):
        """TC006: 长输入使用 high 层级"""
        long_text = "这是一段很长的输入文本，" + "继续增加长度，" * 30  # >200 字
        model = auto_route(long_text, "anthropic", get_model)
        assert model == get_model("anthropic", "high")


class TestRouteRequest:
    """路由请求测试"""

    def test_type_route(self):
        """测试 type 路由"""
        model = route_request("openai", "high", get_model_fn=get_model)
        assert model == "gpt-4.5-preview"

    def test_auto_route(self):
        """测试自动路由"""
        model = route_request(
            "anthropic",
            "auto",
            get_model_fn=get_model,
            auto_fn=auto_route,
            input_text="简短",
        )
        assert "haiku" in model


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
