# AI Agent 文件结构文档

**最后更新**: 2026-04-15  
**历史版本**: `docs/structure_history/`

## 目录树

```
AgentMemory/
├── src/
│   ├── __init__.py          # 包入口，导出配置和接口
│   ├── protocols/           # 协议和接口模块
│   │   ├── interfaces.py    # 全局接口定义 (IPerception, IMemory, IReasoning, IAction, ITool + 扩展接口)
│   │   ├── message.py       # 消息数据结构
│   │   └── __init__.py      # 协议模块入口
│   ├── config.py            # 配置管理 (Config 类，config 实例)
│   │
│   ├── perception/          # 感知层
│   │   ├── __init__.py      # 导出 PerceptionLayer
│   │   ├── layer.py         # 感知层协议 (协调输入处理流程)
│   │   ├── process_input.py # 输入处理实现
│   │   └── extract_intent.py# 意图提取实现
│   │
│   ├── memory/              # 记忆层
│   │   ├── __init__.py      # 导出 MemoryLayer, init_memory_storage
│   │   ├── layer.py         # 记忆层协议 (协调记忆操作)
│   │   ├── add_memory.py    # 添加记忆实现 (含存储逻辑)
│   │   ├── search_memory.py # 搜索记忆实现 (关键词匹配)
│   │   └── get_all.py       # 获取所有记忆实现
│   │
│   ├── reasoning/           # 推理层
│   │   ├── __init__.py      # 导出 ReasoningLayer
│   │   ├── layer.py         # 推理层协议 (协调推理流程)
│   │   ├── analyze.py       # 分析实现
│   │   ├── retrieve.py      # 检索实现 (依赖 IMemory)
│   │   └── generate.py      # 响应生成实现
│   │
│   ├── action/              # 行动层
│   │   ├── __init__.py      # 导出 ActionLayer
│   │   ├── layer.py         # 行动层协议 (协调输出执行)
│   │   └── execute_output.py# 执行输出实现
│   │
│   └── tools/               # 工具层
│       ├── __init__.py      # 导出 BaseTool, ToolRegistry
│       ├── base.py          # 工具基类
│       ├── registry.py      # 工具注册中心
│       └── impls/           # 工具实现目录
│           ├── __init__.py
│           └── search_tool.py # 示例搜索工具
│
├── container.py             # 依赖注入容器 (组装所有层)
├── main.py                  # 程序入口 (交互式命令行)
├── README.md                # 项目说明文档
├── FILE_STRUCTURE.md        # 本文件 - 文件结构文档
└── tests/
    ├── test_plan.md         # 测试计划
    ├── test_agent.py        # 测试脚本
    └── test_results.md      # 测试结果记录
```

## 文件说明

### 核心文件

| 文件 | 行数 | 职责 |
|------|------|------|
| `src/interfaces.py` | ~60 | 定义 5 个接口：IPerception, IMemory, IReasoning, IAction, ITool |
| `src/config.py` | ~20 | Pydantic 配置类，管理模型参数和存储路径 |
| `container.py` | ~50 | DI 容器，组装所有层的依赖 |
| `main.py` | ~25 | 交互式命令行入口 |

### 各层文件

#### 感知层 (perception/)
| 文件 | 职责 |
|------|------|
| `layer.py` | PerceptionLayer 类，接收注入的函数，协调流程 |
| `process_input.py` | process_input 函数，清洗输入 |
| `extract_intent.py` | extract_intent 函数，关键词匹配意图 |

#### 记忆层 (memory/)
| 文件 | 职责 |
|------|------|
| `layer.py` | MemoryLayer 类，接收注入的函数，协调操作 |
| `add_memory.py` | add_memory 函数，管理存储和持久化 |
| `search_memory.py` | search_memory 函数，关键词搜索 |
| `get_all.py` | get_all_memories 函数，获取全部 |

#### 推理层 (reasoning/)
| 文件 | 职责 |
|------|------|
| `layer.py` | ReasoningLayer 类，接收注入的函数，协调推理 |
| `analyze.py` | analyze 函数，分析输入数据 |
| `retrieve.py` | retrieve 函数，检索记忆 (依赖 IMemory) |
| `generate.py` | generate_response 函数，生成响应 |

#### 行动层 (action/)
| 文件 | 职责 |
|------|------|
| `layer.py` | ActionLayer 类，接收注入的函数 |
| `execute_output.py` | execute_output 函数，格式化输出 |

#### 工具层 (tools/)
| 文件 | 职责 |
|------|------|
| `base.py` | BaseTool 抽象基类 |
| `registry.py` | ToolRegistry 注册中心 |
| `impls/search_tool.py` | 示例工具实现 |

#### 工具层 (tools/impls/)
| 文件 | 职责 |
|------|------|
| `search_tool.py` | 示例搜索工具实现 |

### 测试文件

| 文件 | 职责 |
|------|------|
| `tests/test_plan.md` | 测试计划和用例 |
| `tests/test_agent.py` | pytest 风格测试脚本 |
| `tests/test_results.md` | 测试结果记录 |

## 依赖关系

```
main.py → container.py
container.py → 各层 layer.py
各层 layer.py → 对应实现文件
实现文件 → protocols/interfaces.py (通过类型注解)
```

## 修改历史

历史快照存储在 `docs/structure_history/` 目录。

| 日期 | 变更 | 快照文件 |
|------|------|----------|
| 2026-04-15 20:00 | 初始创建：五层架构 + 测试框架 | - |
| 2026-04-15 20:05 | 创建 FILE_STRUCTURE.md 文档 | - |
| 2026-04-15 20:10 | 清理旧文件 | `v2026-04-15-2010.md` |
| 2026-04-15 20:15 | 创建项目控制 skill 文档 | `v2026-04-15-2015.md` |
| 2026-04-15 20:19 | DI 优化 - ReasoningLayer 注入 memory 参数 | `v2026-04-15-2019.md` |
| 2026-04-15 20:21 | 层间通信协议实现 | `v2026-04-15-2021.md` |
| 2026-04-15 20:30 | 清理冗余 protocols 目录（3 个文件） | `v2026-04-15-2030.md` |
| 2026-04-15 20:35 | 接口统一：所有文件引用 protocols/interfaces.py | `v2026-04-15-2035.md` |
| 2026-04-15 20:45 | 修正 layer.py 依赖注入：所有方法使用注入函数 | `v2026-04-15-2045.md` |
| 2026-04-16 00:03 | 日志系统实现：使用 loguru，支持 ERROR/INFO/DEBUG 级别 | `v2026-04-16-0003.md` |
