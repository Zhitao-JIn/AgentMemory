# container.py - 依赖注入容器

## 文件职责

组装 AI Agent 的所有层和依赖。

## Container 类

### 初始化流程

1. 配置日志级别
2. 初始化记忆存储
3. 创建记忆层
4. 创建行动层
5. 创建推理层（注入记忆层）
6. 创建感知层（注入推理层和行动层）

### 方法

- `run(user_input)` → str - 接收用户输入并返回结果

## 依赖关系

```
Container
├── PerceptionLayer
│   ├── process_input
│   ├── extract_intent
│   └── receive_input
├── ReasoningLayer
│   ├── analyze
│   ├── retrieve
│   └── generate
├── MemoryLayer
│   ├── add_memory
│   ├── search_memory
│   └── get_all
└── ActionLayer
    └── execute_output
```
