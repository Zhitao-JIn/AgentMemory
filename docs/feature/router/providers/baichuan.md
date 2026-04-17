# Baichuan/百川 提供商

## 模型配置

| 级别 | 模型名称 | 上下文长度 | Max Tokens | 描述 |
|------|----------|------------|------------|------|
| `high` | `baichuan2-128k` | 128k | 131,072 | 旗舰模型，支持 128k 上下文 |
| `medium` | `baichuan2` | 32k | 32,768 | 性价比模型 |
| `low` | `baichuan2-turbo` | 8k | 8,192 | 快速模型 |

## API 配置

- **API Key**: `BAICHUAN_API_KEY` (环境变量) / `config.baichuan_api_key`
- **API Base**: 默认配置（从环境变量读取）
- **LiteLLM 前缀**: 无 (如 `baichuan2`)

## 使用示例

```python
router.generate("你好", provider="baichuan", type="medium")
```

## 相关文件

- `src/router/providers/baichuan.py` - 配置定义
- `litellm_client.md` - LiteLLM 封装
- `overview.md` - 提供商总览
