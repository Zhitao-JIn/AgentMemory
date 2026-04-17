# OpenAI 提供商

## 模型配置

| 级别 | 模型名称 | 描述 |
|------|----------|------|
| `high` | `gpt-4.5-preview` | OpenAI 旗舰模型 |
| `medium` | `gpt-4o` | OpenAI 性价比模型 |
| `low` | `gpt-4o-mini` | OpenAI 快速模型 |

## API 配置

- **API Key**: `OPENAI_API_KEY` (环境变量) / `config.openai_api_key`
- **API Base**: `https://api.openai.com/v1` (默认)
- **LiteLLM 前缀**: 无 (如 `gpt-4o`)

## 使用示例

```python
router.generate("Hello", provider="openai", type="medium")
```

## 相关文件

- `src/router/providers/openai.py` - 配置定义
- `litellm_client.md` - LiteLLM 封装
- `overview.md` - 提供商总览
