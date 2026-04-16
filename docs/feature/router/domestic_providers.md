# 国内模型提供商

## 支持的国内模型

| 提供商 | 高端 (high) | 中端 (medium) | 低端 (low) |
|--------|-------------|---------------|-----------|
| Qwen/通义千问 | qwen3-max | qwen3.5-plus | qwen3.5-flash |
| 智谱 AI/GLM | glm-z1 | glm-4 | glm-3-turbo |
| 百川/Baichuan | baichuan2-128k | baichuan2 | baichuan2-turbo |
| 零一万物/Yi | yi-34b | yi-large | yi-medium |
| MiniMax | abab6.5 | abab5.5 | abab4 |
| 360 智脑 | sensechat-5 | sensechat-4 | sensechat-3 |

## 使用方式

```python
from container import Container
agent = Container()

# 使用通义千问
response = agent.chat(prompt="你好", provider="qwen", type="medium")

# 使用智谱 GLM
response = agent.chat(prompt="你好", provider="zhipu", type="medium")

# 使用别名
response = agent.chat(prompt="你好", provider="通义", type="high")  # → qwen-max
response = agent.chat(prompt="你好", provider="glm", type="high")   # → glm-z1
```

## 模型说明

### Qwen/通义千问
- **qwen3-max**: 适合复杂任务，能力最强
- **qwen3.5-plus**: 效果、速度、成本均衡
- **qwen3.5-flash**: 适合简单任务，速度快、成本低

### 智谱 AI/GLM
- **glm-z1**: 旗舰模型，最强推理
- **glm-4**: 主力模型，平衡性能和成本
- **glm-3-turbo**: 快速响应，适合简单任务

### 百川/Baichuan
- **baichuan2-128k**: 支持 128k 超长上下文
- **baichuan2**: 通用模型
- **baichuan2-turbo**: 快速模型
