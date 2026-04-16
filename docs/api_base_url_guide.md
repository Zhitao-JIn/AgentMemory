# API 请求地址配置指南

## 默认请求地址

LiteLLM 会自动使用各提供商的官方 API 地址，通常无需配置。

| 提供商 | 默认请求地址 |
|--------|-------------|
| Qwen/通义千问 | https://dashscope.aliyuncs.com/compatible-mode/v1 |
| 智谱 AI | https://open.bigmodel.cn/api/paas/v4 |
| 百川 | https://api.baichuan-ai.com/v1 |
| Anthropic | https://api.anthropic.com |
| OpenAI | https://api.openai.com/v1 |
| Google | https://generativelanguage.googleapis.com |

## 何时需要自定义请求地址？

1. **使用国内代理访问国际模型**
2. **使用第三方中转服务**（如 OpenRouter、Together 等）
3. **使用本地部署的模型**（如 Ollama、vLLM）
4. **企业内网 API 网关**

## 配置方式

### 方式 1: 在 `.env` 文件中配置

```bash
# .env

# Qwen 自定义请求地址
QWEN_BASE_URL=https://your-proxy.com/v1

# OpenAI 使用代理
OPENAI_BASE_URL=https://api-proxy.example.com/v1

# Ollama 本地部署
OLLAMA_BASE_URL=http://localhost:11434/v1
```

### 方式 2: 在代码中指定

```python
from container import Container

agent = Container()

# 方式 A: 使用 router.generate() 直接指定
response = agent.router.generate(
    prompt="你好",
    model="qwen3-max",
    api_base="https://your-proxy.com/v1"
)

# 方式 B: 使用 chat() 方法
response = agent.chat(
    prompt="你好",
    provider="qwen",
    type="high",
    api_base="https://your-proxy.com/v1"  # 需要更新 layer.py 支持此参数
)
```

## 常见代理服务商

### 1. OpenRouter (支持多模型)
```bash
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_API_KEY=sk-or-xxx
```

### 2. Together AI
```bash
TOGETHER_BASE_URL=https://api.together.xyz/v1
TOGETHER_API_KEY=xxx
```

### 3. 阿里云百炼（兼容模式）
```bash
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
QWEN_API_KEY=sk-xxx
```

### 4. Ollama (本地部署)
```bash
OLLAMA_BASE_URL=http://localhost:11434/v1
# 无需 API Key
```

## 使用示例

### Qwen 通过代理访问

```bash
# .env
QWEN_API_KEY=sk-xxx
QWEN_BASE_URL=https://your-proxy.com/v1
```

```python
from container import Container
agent = Container()
response = agent.chat(prompt="你好", provider="qwen", type="medium")
```

### Ollama 本地模型

```bash
# .env
OLLAMA_BASE_URL=http://localhost:11434/v1
```

```python
from container import Container
agent = Container()

# 使用本地 Llama3
response = agent.router.generate(
    prompt="你好",
    model="ollama/llama3.1:8b"
)
```

---

## 故障排查

### 问题 1: 请求超时
- 检查网络连接
- 尝试更换代理地址
- 检查防火墙设置

### 问题 2: 401 Unauthorized
- 检查 API Key 是否正确
- 检查 API Key 是否有足够额度

### 问题 3: 404 Not Found
- 检查 `BASE_URL` 是否正确
- 检查模型名称是否支持

### 问题 4: 证书错误
```python
# 临时方案（不推荐生产环境）
import os
os.environ["SSL_VERIFY"] = "false"
```
