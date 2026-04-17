# litellm_client.py - LiteLLM 封装

## 职责

封装 LiteLLM 库，提供统一的 LLM 调用接口。支持多 AI 提供商，自动处理 API Key 和请求地址配置。

## 核心函数

### `call_litellm(model, messages, api_base=None, api_key=None, enable_thinking=None, **kwargs)`

调用 LiteLLM completion。

**参数**:
- `model`: 模型名称（如 `qwen3-max`, `claude-sonnet-4-0`）
- `messages`: 消息列表 `[{"role": "user", "content": "..."}]`
- `api_base`: 可选的 API 请求地址（覆盖默认）
- `api_key`: 可选的 API Key（覆盖默认）
- `enable_thinking`: 是否启用思考模式（覆盖 config 默认配置）
- `**kwargs`: 其他参数（`max_tokens`, `temperature` 等）

**返回**:
- LiteLLM 响应字典，包含 `choices[0].message.content`

**流程**:
1. 调用 `_get_api_key_and_base_for_model()` 获取 API 配置
2. 调用 `_get_thinking_params()` 获取思考模式参数
3. 调用 `_normalize_model_name()` 标准化模型名称
4. 调用 `litellm_completion()` 发起请求
5. 异常时返回错误响应

---

### `_get_thinking_params(model, enable_thinking=None)`

根据模型名称和配置获取思考模式参数。

**优先级**:
1. 调用时传入的 `enable_thinking` 参数
2. `config.py` 中的配置（根据模型层级：high/medium/low）
3. 默认值（True）

**各提供商思考模式参数**:

| 提供商 | 参数 | 说明 |
|--------|------|------|
| Qwen | `extra_body.enable_thinking=true` | 启用思考模式 |
| DeepSeek | `extra_body.enable_thinking=true` | 深度思考模式 |
| Anthropic | `extra_body.thinking.type=enabled` | Extended thinking |
| OpenAI o1/o3 | 无（默认启用） | 固定深度思考模式 |

---

### `_get_api_key_and_base_for_model(model)`

根据模型名称获取对应的 API Key 和请求地址。

**优先级**:
1. `config.py` 中的配置（从 `.env` 读取）
2. 环境变量
3. 默认值

**支持的提供商**:

| 模型前缀 | API Key 配置 | 默认 API Base |
|----------|-------------|---------------|
| `qwen` | `config.qwen_api_key` | `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| `glm` | `config.zhipu_api_key` | `https://open.bigmodel.cn/api/paas/v4` |
| `baichuan` | `config.baichuan_api_key` | - |
| `claude` | `config.anthropic_api_key` | `https://api.anthropic.com` |
| `gpt` | `config.openai_api_key` | `https://api.openai.com/v1` |
| `gemini` | `config.google_api_key` | - |

---

### `_normalize_model_name(model)`

标准化模型名称，添加必要的提供商前缀。

**规则**:
- 已有前缀（含 `/`）：直接返回
- Qwen 模型：添加 `dashscope/` 前缀
- 其他：保持不变

**示例**:
- `"qwen3.5-flash"` → `"dashscope/qwen3.5-flash"`
- `"claude-sonnet-4-0"` → `"claude-sonnet-4-0"`

---

## 依赖

- `litellm`: 核心库
- `src.config`: 配置管理
- `dotenv`: `.env` 文件加载（可选）

## 相关文档

- `layer.md` - Router 层协议
- `router.md` - 路由核心逻辑
- `../config.md` - 配置管理
- `providers/` - 各提供商模型配置
