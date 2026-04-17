# Zhipu AI/智谱 AI 提供商

## 模型配置

| 级别 | 模型名称 | 上下文长度 | Max Tokens | 描述 |
|------|----------|------------|------------|------|
| `high` | `glm-z1` | 32k | 32,768 | 旗舰模型，最强推理能力 |
| `medium` | `glm-4` | 32k | 32,768 | 性价比模型，平衡性能与成本 |
| `low` | `glm-3-turbo` | 8k | 8,192 | 快速模型，适合简单任务 |

## API 配置

- **API Key**: `ZHIPU_API_KEY` (环境变量) / `config.zhipu_api_key`
- **API Base**: `https://open.bigmodel.cn/api/paas/v4` (默认)
- **LiteLLM 前缀**: 无 (如 `glm-4`)

## 使用示例

```python
router.generate("你好", provider="zhipu", type="medium")
```

## 相关文件

- `src/router/providers/zhipu.py` - 配置定义
- `litellm_client.md` - LiteLLM 封装
- `overview.md` - 提供商总览
