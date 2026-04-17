# Google 提供商

## 模型配置

| 级别 | 模型名称 | 描述 |
|------|----------|------|
| `high` | `gemini-2.0-ultra` | Google 旗舰模型 |
| `medium` | `gemini-2.0-pro` | Google 性价比模型 |
| `low` | `gemini-2.0-flash` | Google 快速模型 |

## API 配置

- **API Key**: `GOOGLE_API_KEY` (环境变量) / `config.google_api_key`
- **API Base**: 默认配置
- **LiteLLM 前缀**: 无 (如 `gemini-2.0-flash`)

## 使用示例

```python
router.generate("Hello", provider="google", type="medium")
```

## 相关文件

- `src/router/providers/google.py` - 配置定义
- `litellm_client.md` - LiteLLM 封装
- `overview.md` - 提供商总览
