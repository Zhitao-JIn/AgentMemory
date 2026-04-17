# Router 提供商配置

## 概述

Router 层支持多 AI 提供商路由，各提供商的模型配置在 `providers/` 目录下独立定义。

## 支持的提供商

### 国内厂商

| 提供商 | 配置目录 | 文档 |
|--------|----------|------|
| Qwen/通义千问 | `src/router/providers/qwen.py` | `qwen.md` |
| 智谱 AI/GLM | `src/router/providers/zhipu.py` | `zhipu.md` |
| 百川/Baichuan | `src/router/providers/baichuan.py` | `baichuan.md` |

### 国际厂商

| 提供商 | 配置目录 | 文档 |
|--------|----------|------|
| Anthropic | `src/router/providers/anthropic.py` | `anthropic.md` |
| OpenAI | `src/router/providers/openai.py` | `openai.md` |
| Google | `src/router/providers/google.py` | `google.md` |

## 模型分级

每个提供商提供三档模型：

| 级别 | 用途 | 典型场景 |
|------|------|----------|
| `high` | 旗舰模型 | 复杂推理、长上下文、高精度任务 |
| `medium` | 均衡模型 | 日常任务、平衡性能与成本 |
| `low` | 快速模型 | 简单任务、低延迟、低成本 |

## 配置结构

每个提供商的配置文件包含：

```python
PROVIDER_MODELS = {
    "high": {
        "model": "model-name",
        "max_tokens": 4096,
        "description": "模型描述",
    },
    "medium": { ... },
    "low": { ... },
}
```

## 相关文件

- `layer.md` - Router 层协议
- `router.md` - 路由核心逻辑
- `litellm_client.md` - LiteLLM 封装
- `domestic_providers.md` - 国内厂商完整列表
