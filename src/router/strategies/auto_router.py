"""智能路由策略 - 根据输入复杂度自动选择模型层级"""


def auto_route(
    input_text: str,
    provider: str,
    get_model_fn: callable,
    threshold_low: int = 50,
    threshold_medium: int = 200,
) -> str:
    """智能路由 - 根据输入复杂度选择模型层级

    Args:
        input_text: 用户输入文本
        provider: 提供商名称
        get_model_fn: 获取模型的函数
        threshold_low: 低于此字数使用 low 层级
        threshold_medium: 低于此字数使用 medium 层级

    Returns:
        模型名称
    """
    char_count = len(input_text)

    # 简单问题 → 低端模型
    if char_count < threshold_low:
        return get_model_fn(provider, "low")

    # 中等问题 → 中端模型
    if char_count < threshold_medium:
        return get_model_fn(provider, "medium")

    # 复杂问题 → 高端模型
    return get_model_fn(provider, "high")
