# 配置统一说明

## 配置统一方案

**已解决**: `src/config.py` 和 `src/router/litellm_client.py` 之间的配置方式冲突。

### 配置优先级

```
1. 调用时传入的参数 (api_key, api_base)
       ↓
2. config.py 中的配置 (从 .env 读取)
       ↓
3. 环境变量 (如果 config 不可用)
```

---

## 配置流程

### 1. `.env` 文件（实际存储）

```bash
# .env
QWEN_API_KEY=sk-xxx
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

### 2. `config.py`（统一接口）

```python
class Config(BaseModel):
    qwen_api_key: str = Field(default_factory=lambda: os.getenv("QWEN_API_KEY", ""))
    qwen_base_url: str = Field(default_factory=lambda: os.getenv("QWEN_BASE_URL", ""))

config = Config()
```

### 3. `litellm_client.py`（使用配置）

```python
from src.config import config

def _get_api_key_and_base_for_model(model: str) -> dict:
    if CONFIG_AVAILABLE and config:
        result["api_key"] = config.qwen_api_key
        result["api_base"] = config.qwen_base_url
    else:
        # 回退到环境变量
        result["api_key"] = os.getenv("QWEN_API_KEY")
```

---

## 使用方式

### 方式 1: 通过 `.env` 配置（推荐）

```bash
# .env
QWEN_API_KEY=sk-xxx
DEFAULT_PROVIDER=qwen
DEFAULT_TYPE=medium
```

```python
from container import Container
agent = Container()
response = agent.chat(prompt="你好")
```

### 方式 2: 调用时指定

```python
from container import Container
agent = Container()

# 临时指定 API Key
response = agent.router.generate(
    prompt="你好",
    provider="qwen",
    type="low",
    api_key="sk-another-key"  # 覆盖 .env 中的配置
)
```

---

## 配置字段映射

| `.env` 变量 | `config.py` 字段 | 用途 |
|------------|-----------------|------|
| `QWEN_API_KEY` | `config.qwen_api_key` | Qwen API Key |
| `QWEN_BASE_URL` | `config.qwen_base_url` | Qwen 请求地址 |
| `ZHIPU_API_KEY` | `config.zhipu_api_key` | 智谱 API Key |
| `ANTHROPIC_API_KEY` | `config.anthropic_api_key` | Anthropic API Key |
| `OPENAI_API_KEY` | `config.openai_api_key` | OpenAI API Key |

---

## 为什么要这样设计？

1. **`.env` 文件**: 实际存储敏感信息，不提交到 Git
2. **`config.py`**: 提供统一的配置访问接口，支持默认值和验证
3. **`litellm_client.py`**: 从 config 读取，保证配置一致性
4. **回退机制**: 如果 config 不可用，回退到环境变量
