"""LiteLLM Completion 封装"""
from typing import Any, Dict, List, Optional

try:
    from src.config import config
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False
    config = None

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv 未安装时使用环境变量

try:
    import litellm
    from litellm import completion as litellm_completion
    LITELLM_AVAILABLE = True
except ImportError:
    LITELLM_AVAILABLE = False
    litellm = None


def call_litellm(
    model: str,
    messages: List[Dict[str, str]],
    api_base: Optional[str] = None,
    api_key: Optional[str] = None,
    enable_thinking: Optional[bool] = None,
    **kwargs,
) -> Dict[str, Any]:
    """调用 LiteLLM completion

    Args:
        model: 模型名称 (如 qwen3-max, qwen3.5-flash, claude-sonnet-4-0)
        messages: 消息列表 [{"role": "user", "content": "..."}]
        api_base: 可选的 API 请求地址（覆盖默认）
        api_key: 可选的 API Key（覆盖默认）
        enable_thinking: 是否启用思考模式（覆盖 config 默认配置）
        **kwargs: 其他参数 (max_tokens, temperature 等)

    Returns:
        LiteLLM 响应字典
    """
    if not LITELLM_AVAILABLE:
        return {
            "error": "LiteLLM not installed. Install with: pip install litellm",
            "choices": [{"message": {"content": "LiteLLM 未安装"}}]
        }

    # 获取 API Key 和请求地址
    setup_result = _get_api_key_and_base_for_model(model)

    # 使用传入的参数覆盖，或使用自动获取的值
    final_api_key = api_key or setup_result.get("api_key")
    final_api_base = api_base or setup_result.get("api_base")

    # 获取思考模式参数
    thinking_params = _get_thinking_params(model, enable_thinking)

    # 标准化模型名称（添加前缀）
    model = _normalize_model_name(model)

    try:
        response = litellm_completion(
            model=model,
            messages=messages,
            api_base=final_api_base,
            api_key=final_api_key,
            **thinking_params,
            **kwargs,
        )
        return response
    except Exception as e:
        # Fallback 处理
        return {
            "error": str(e),
            "choices": [{"message": {"content": f"请求失败：{e}"}}]
        }


def _get_thinking_params(model: str, enable_thinking: Optional[bool] = None) -> dict:
    """根据模型名称和配置获取思考模式参数

    Args:
        model: 模型名称
        enable_thinking: 是否启用思考模式（None 时使用 config 默认配置）

    Returns:
        思考模式参数字典
    """
    # 如果未指定，使用 config 中的默认配置
    if enable_thinking is None:
        if not CONFIG_AVAILABLE or not config:
            enable_thinking = True  # 默认启用
        else:
            # 根据模型层级判断
            model_lower = model.lower()
            if "max" in model_lower or "opus" in model_lower or "ultra" in model_lower:
                enable_thinking = config.thinking_mode_high
            elif "turbo" in model_lower or "flash" in model_lower or "mini" in model_lower or "haiku" in model_lower:
                enable_thinking = config.thinking_mode_low
            else:
                enable_thinking = config.thinking_mode_medium

    # 根据模型类型返回对应的思考模式参数
    model_lower = model.lower()

    # Qwen 模型：enable_thinking 参数
    if "qwen" in model_lower:
        if enable_thinking:
            return {"extra_body": {"enable_thinking": True}}
        else:
            # 显式禁用思考模式
            return {"extra_body": {"enable_thinking": False}}

    # OpenAI o1/o3 系列：固定启用思考模式（无法禁用）
    if "o1" in model_lower or "o3" in model_lower:
        return {}

    # Anthropic Claude：extended thinking
    if "claude" in model_lower:
        if enable_thinking:
            return {"extra_body": {"thinking": {"type": "enabled"}}}
        else:
            return {"extra_body": {"thinking": {"type": "disabled"}}}

    # DeepSeek：深度思考模式
    if "deepseek" in model_lower:
        if enable_thinking:
            return {"extra_body": {"enable_thinking": True}}
        else:
            return {"extra_body": {"enable_thinking": False}}

    # 其他模型：默认不启用
    return {}


def _get_api_key_and_base_for_model(model: str) -> dict:
    """根据模型名称获取对应的 API Key 和请求地址

    优先级：
    1. config.py 中的配置（如果可用）
    2. 环境变量
    3. 默认值

    Args:
        model: 模型名称（不带前缀，如 qwen3.5-flash）

    Returns:
        {"api_base": ..., "api_key": ...}
    """
    result = {"api_base": None, "api_key": None}

    # 如果 config 可用，优先使用 config 中的配置
    if CONFIG_AVAILABLE and config:
        # Qwen/通义千问
        if "qwen" in model.lower():
            result["api_key"] = config.qwen_api_key or None
            result["api_base"] = config.qwen_base_url or "https://dashscope.aliyuncs.com/compatible-mode/v1"

        # 智谱 GLM
        elif "glm" in model.lower():
            result["api_key"] = config.zhipu_api_key or None
            result["api_base"] = config.zhipu_base_url or "https://open.bigmodel.cn/api/paas/v4"

        # 百川
        elif "baichuan" in model.lower():
            result["api_key"] = config.baichuan_api_key or None
            result["api_base"] = config.baichuan_base_url

        # Anthropic
        elif "claude" in model.lower():
            result["api_key"] = config.anthropic_api_key or None
            result["api_base"] = config.anthropic_base_url or "https://api.anthropic.com"

        # OpenAI
        elif "gpt" in model.lower():
            result["api_key"] = config.openai_api_key or None
            result["api_base"] = config.openai_base_url or "https://api.openai.com/v1"

        # Google
        elif "gemini" in model.lower():
            result["api_key"] = config.google_api_key or None
            result["api_base"] = config.google_base_url

    else:
        # 回退到环境变量
        # Qwen/通义千问
        if "qwen" in model.lower():
            import os
            result["api_key"] = os.getenv("QWEN_API_KEY")
            result["api_base"] = os.getenv("QWEN_BASE_URL") or "https://dashscope.aliyuncs.com/compatible-mode/v1"

        # 智谱 GLM
        elif "glm" in model.lower():
            import os
            result["api_key"] = os.getenv("ZHIPU_API_KEY")
            result["api_base"] = os.getenv("ZHIPU_BASE_URL") or "https://open.bigmodel.cn/api/paas/v4"

        # 百川
        elif "baichuan" in model.lower():
            import os
            result["api_key"] = os.getenv("BAICHUAN_API_KEY")
            result["api_base"] = os.getenv("BAICHUAN_BASE_URL")

        # Anthropic
        elif "claude" in model.lower():
            import os
            result["api_key"] = os.getenv("ANTHROPIC_API_KEY")
            result["api_base"] = os.getenv("ANTHROPIC_BASE_URL") or "https://api.anthropic.com"

        # OpenAI
        elif "gpt" in model.lower():
            import os
            result["api_key"] = os.getenv("OPENAI_API_KEY")
            result["api_base"] = os.getenv("OPENAI_BASE_URL") or "https://api.openai.com/v1"

        # Google
        elif "gemini" in model.lower():
            import os
            result["api_key"] = os.getenv("GOOGLE_API_KEY")
            result["api_base"] = os.getenv("GOOGLE_BASE_URL")

    return result


def _normalize_model_name(model: str) -> str:
    """标准化模型名称，添加必要的提供商前缀

    Args:
        model: 原始模型名称

    Returns:
        标准化后的模型名称（带提供商前缀）
    """
    # 如果已有前缀，直接返回
    if "/" in model:
        return model

    # Qwen 模型需要 dashscope 前缀
    if "qwen" in model.lower():
        return f"dashscope/{model}"

    # 其他模型保持不变
    return model
