# 配置 API Key

## 步骤

### 1. 创建 .env 文件

在项目根目录创建 `.env` 文件（已存在 `.env.example` 可复制）：

```bash
cp .env.example .env
```

### 2. 获取 API Key

#### Qwen/通义千问
- **获取地址**: https://bailian.console.aliyun.com/
- **步骤**:
  1. 登录阿里云百炼控制台
  2. 进入 API-KEY 管理
  3. 创建新的 API-KEY
  4. 复制并填入 `.env`

#### 智谱 AI/GLM
- **获取地址**: https://open.bigmodel.cn/
- **步骤**:
  1. 登录智谱 AI 开放平台
  2. 进入个人中心 -> API Key
  3. 创建新的 API Key

#### 百川/Baichuan
- **获取地址**: https://platform.baichuan-ai.com/

### 3. 填入 .env 文件

```bash
# .env

# Qwen/通义千问
QWEN_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
# 可选：自定义请求地址
# QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1

# 智谱 AI/GLM
ZHIPU_API_KEY=xxxxxxxxxxxxxxxx

# 百川
BAICHUAN_API_KEY=xxxxxxxxxxxxxxxx

# 默认配置
DEFAULT_PROVIDER=qwen
DEFAULT_TYPE=medium
LOG_LEVEL=INFO
```

### 4. 安装依赖

```bash
pip install python-dotenv litellm
```

### 5. 测试

```python
from container import Container

agent = Container()
response = agent.chat(prompt="你好", provider="qwen", type="medium")
print(response)
```

---

## 环境变量列表

| 变量名 | 说明 | 获取地址 |
|--------|------|----------|
| `QWEN_API_KEY` | Qwen/通义千问 | https://bailian.console.aliyun.com/ |
| `ZHIPU_API_KEY` | 智谱 AI/GLM | https://open.bigmodel.cn/ |
| `BAICHUAN_API_KEY` | 百川 | https://platform.baichuan-ai.com/ |
| `LINGYI_API_KEY` | 零一万物 | https://platform.lingyi.ai/ |
| `MINIMAX_API_KEY` | MiniMax | https://platform.minimaxi.com/ |
| `ANTHROPIC_API_KEY` | Anthropic/Claude | https://console.anthropic.com/ |
| `OPENAI_API_KEY` | OpenAI/GPT | https://platform.openai.com/ |
| `GOOGLE_API_KEY` | Google/Gemini | https://makersuite.google.com/ |

---

## 安全提示

- `.env` 文件已被加入 `.gitignore`，不会被提交到 Git
- 不要将 API Key 硬编码到代码中
- 定期更换 API Key
- 在阿里云设置消费预警
