# Anthropic 提供商

## 模型配置

| 级别 | 模型名称 | Max Tokens | 描述 |
|------|----------|------------|------|
| `high` | `claude-opus-4-0` | 4,096 | 旗舰模型，适合复杂任务 |
| `medium` | `claude-sonnet-4-0` | 4,096 | 性价比模型，平衡性能与成本 |
| `low` | `claude-haiku-4-0` | 4,096 | 快速模型，适合简单任务 |

## API 配置

- **API Key**: `ANTHROPIC_API_KEY` (环境变量) / `config.anthropic_api_key`
- **API Base**: `https://api.anthropic.com` (默认)
- **LiteLLM 前缀**: 无 (如 `claude-sonnet-4-0`)

## 使用示例

```python
router.generate("Hello", provider="anthropic", type="medium")
```

## 相关文件

- `src/router/providers/anthropic.py` - 配置定义
- `litellm_client.md` - LiteLLM 封装
- `overview.md` - 提供商总览
