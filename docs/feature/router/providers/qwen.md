# Qwen/通义千问 提供商

## 模型配置

| 级别 | 模型名称 | 上下文长度 | Max Tokens | 描述 |
|------|----------|------------|------------|------|
| `high` | `qwen3-max` | 256k | 256,000 | 适合复杂任务，能力最强 |
| `medium` | `qwen3.5-plus` | 128k | 128,000 | 效果、速度、成本均衡 |
| `low` | `qwen3.5-flash` | 64k | 64,000 | 适合简单任务，速度快、成本低 |

## API 配置

- **API Key**: `QWEN_API_KEY` (环境变量) / `config.qwen_api_key`
- **API Base**: `https://dashscope.aliyuncs.com/compatible-mode/v1` (默认)
- **LiteLLM 前缀**: `dashscope/` (如 `dashscope/qwen3.5-flash`)

## 使用示例

```python
# 通过 Router 层调用
router.generate("你好", provider="qwen", type="medium")

# 直接调用
from src.router.litellm_client import call_litellm
response = call_litellm(
    model="qwen3.5-flash",
    messages=[{"role": "user", "content": "你好"}],
    max_tokens=1024,
)
```

## 配置说明

- API Key 从 `.env` 或环境变量读取
- 模型名称会自动添加 `dashscope/` 前缀
- 支持上下文长度配置在 `QWEN_CONTEXT_LENGTHS` 中定义

## 相关文件

- `src/router/providers/qwen.py` - 配置定义
- `litellm_client.md` - LiteLLM 封装
- `overview.md` - 提供商总览
