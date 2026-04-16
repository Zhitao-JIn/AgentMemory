# 配置说明文档

## 配置冲突解决

**已解决**: `src/config.py` 和 `src/router/litellm_client.py` 之间的配置方式冲突。

### 问题

之前存在两套配置方式：
1. `config.py` 中定义 API Key 字段（如 `qwen_key`, `zhipu_key`）
2. `litellm_client.py` 从环境变量读取（如 `QWEN_API_KEY`, `ZHIPU_API_KEY`）

两套配置没有统一，导致混淆。

### 解决方案

**统一使用环境变量方式**：

1. **API Keys 从环境变量读取**
   ```python
   # config.py 中不再硬编码 API Key
   qwen_api_key: str = Field(default_factory=lambda: os.getenv("QWEN_API_KEY", ""))
   ```

2. **litellm_client 继续从环境变量读取**
   ```python
   # litellm_client.py
   api_key = os.getenv("QWEN_API_KEY")
   ```

3. **用户在 `.env` 文件中配置**
   ```bash
   # .env
   QWEN_API_KEY=sk-xxx
   QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
   ```

---

## 当前配置方式

### 1. 默认配置（在 `config.py`）

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `default_provider` | `"qwen"` | 默认提供商 |
| `default_type` | `"medium"` | 默认模型层级 |
| `max_tokens` | `1024` | 最大 token 数 |
| `temperature` | `0.7` | 温度参数 |
| `log_level` | `"INFO"` | 日志级别 |

### 2. 环境变量（在 `.env`）

| 变量名 | 说明 |
|--------|------|
| `QWEN_API_KEY` | Qwen API Key |
| `QWEN_BASE_URL` | Qwen 请求地址（可选） |
| `ZHIPU_API_KEY` | 智谱 API Key |
| `ZHIPU_BASE_URL` | 智谱请求地址（可选） |
| `ANTHROPIC_API_KEY` | Anthropic API Key |
| `OPENAI_API_KEY` | OpenAI API Key |

### 3. 容器初始化参数

```python
from container import Container

# 使用 config 中的默认值
agent = Container()

# 覆盖日志级别
agent = Container(log_level="DEBUG")

# 覆盖记忆存储路径
agent = Container(memory_path="./my_memory.json")
```

---

## 使用示例

### 方式 1: 使用 `.env` 文件（推荐）

```bash
# 1. 创建 .env 文件
cp .env.example .env

# 2. 编辑 .env
QWEN_API_KEY=sk-xxx
DEFAULT_PROVIDER=qwen
DEFAULT_TYPE=medium
```

```python
# 3. 代码中直接使用
from container import Container
agent = Container()
response = agent.chat(prompt="你好")  # 使用 qwen3.5-plus
```

### 方式 2: 临时指定

```python
from container import Container
agent = Container()

# 指定提供商和层级
response = agent.chat(
    prompt="你好",
    provider="qwen",
    type="high"  # 使用 qwen3-max
)

# 或使用智能路由
response = agent.chat(
    prompt="这是一个非常复杂的问题...",
    type="auto"  # 根据输入长度自动选择
)
```

---

## 最佳实践

1. **不要将 API Key 提交到 Git**
   - `.env` 已在 `.gitignore` 中
   - 使用 `.env.example` 作为模板

2. **使用环境变量管理敏感信息**
   ```bash
   # 生产环境
   export QWEN_API_KEY=sk-xxx
   python main.py
   ```

3. **使用 config.py 管理非敏感配置**
   ```python
   # 可以修改 config.py 中的默认值
   default_provider = "qwen"
   default_type = "medium"
   ```

4. **需要时使用覆盖参数**
   ```python
   # 临时使用高端模型
   response = agent.chat(prompt="...", type="high")
   ```
