# AI Agent 五层架构

基于 LangGraph 的五层架构 AI Agent，使用依赖注入解耦各层。

## 架构

```
用户输入 → 感知层 → 记忆层 → 推理层 → 行动层 → 输出
                ↑                    ↓
                └── 工具层 ──────────┘
```

### 五层职责

| 层级 | 职责 | 主模块 | 实现文件 |
|------|------|--------|----------|
| **感知层** | 输入处理、意图识别 | `perception/layer.py` | `process_input.py`, `extract_intent.py` |
| **记忆层** | 存储、检索 | `memory/layer.py` | `add_memory.py`, `search_memory.py`, `get_all.py` |
| **推理层** | 分析、规划、生成 | `reasoning/layer.py` | `analyze.py`, `retrieve.py`, `generate.py` |
| **行动层** | 输出执行 | `action/layer.py` | `execute_output.py` |
| **工具层** | 独立注册管理 | `tools/registry.py` | `impls/*.py` |

## 目录结构

```
AgentMemory/
├── src/
│   ├── protocols/           # 协议和接口定义
│   │   ├── interfaces.py    # 全局接口 (IPerception, IMemory, IReasoning, IAction, ITool)
│   │   └── message.py       # 消息数据结构
│   ├── config.py            # 配置
│   ├── perception/          # 感知层
│   ├── memory/              # 记忆层
│   ├── reasoning/           # 推理层
│   ├── action/              # 行动层
│   └── tools/               # 工具层
├── container.py             # 依赖注入容器
├── main.py                  # 入口
└── tests/                   # 测试
```

## 快速开始

### 运行
```bash
python main.py
```

### 测试
```bash
python -m pytest tests/test_comm_protocol.py -v
```

## 依赖注入设计

```python
# container.py - 组装各层
class Container:
    def __init__(self):
        self.perception = PerceptionLayer(process_fn, extract_fn)
        self.memory = MemoryLayer(add_fn, search_fn, get_all_fn)
        self.reasoning = ReasoningLayer(analyze_fn, retrieve_fn, generate_fn)
        self.action = ActionLayer(execute_fn)
```

每层主模块只定义**协议**，具体实现由注入的函数决定。

## 添加新工具

1. 继承 `BaseTool`
2. 实现 `execute` 方法
3. 通过 `ToolRegistry.register()` 注册

```python
from src.tools import BaseTool, ToolRegistry

class MyTool(BaseTool):
    name = "my_tool"
    def execute(self, **kwargs):
        return "result"

ToolRegistry.register(MyTool())
```

## 测试结果

详见 `tests/test_results_comm_protocol.md`
