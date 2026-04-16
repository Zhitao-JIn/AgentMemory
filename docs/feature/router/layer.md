# Router 层 - 多 AI 提供商路由

## 文件职责

通过 LiteLLM 统一接口路由到不同 AI 提供商的模型。

## 支持的提供商

| 提供商 | 高端 (high) | 中端 (medium) | 低端 (low) |
|--------|-------------|---------------|-----------|
| Anthropic | claude-opus-4-0 | claude-sonnet-4-0 | claude-haiku-4-0 |
| OpenAI | gpt-4.5-preview | gpt-4o | gpt-4o-mini |
| Google | gemini-2.0-ultra | gemini-2.0-pro | gemini-2.0-flash |
| AWS Bedrock | claude-3-opus | claude-3-sonnet | claude-3-haiku |
| Azure | gpt-4.5 | gpt-4o | gpt-4o-mini |
| Groq | llama-3.3-70b | llama-3.1-70b | llama-3.1-8b |
| DeepSeek | deepseek-chat | - | deepseek-coder |
| Ollama | llama3.1:70b | llama3.1:8b | phi3:3.8b |

## 路由策略

### Type 路由
根据 `type` 字段选择模型层级：
- `high` - 旗舰模型，适合复杂推理任务
- `medium` - 性价比模型，日常使用
- `low` - 快速模型，简单任务
- `auto` - 智能路由，根据输入复杂度自动选择

### 智能路由
根据输入字符数自动选择层级：
- < 50 字 → low
- 50-200 字 → medium  
- > 200 字 → high
