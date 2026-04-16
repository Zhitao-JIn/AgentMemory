# protocols/interfaces.py - 全局接口定义

## 文件职责

定义 AI Agent 五层架构的所有接口协议（Abstract Base Classes）。

## 接口列表

### IPerception (感知层接口)
- `process(raw_input)` - 处理原始输入
- `extract_intent(data)` - 提取意图
- `receive_input(raw_input)` - 接收输入并执行完整流程
- `broadcast_to_reasoning(data)` - 广播给推理层
- `archive_to_memory(data)` - 归档到记忆层

### IMemory (记忆层接口)
- `add(content, meta)` - 添加记忆
- `search(query)` - 搜索记忆
- `get_all()` - 获取所有记忆
- `update_context(data)` - 更新上下文
- `get_context()` - 获取上下文摘要
- `handle_query_request(query_type, params)` - 处理查询请求
- `receive_feedback(feedback_type, content)` - 接收反馈

### IReasoning (推理层接口)
- `analyze(input_data)` - 分析输入
- `retrieve(context)` - 检索记忆
- `generate(context)` - 生成响应
- `query_memory(query_type, params)` - 查询记忆
- `provide_feedback(feedback_type, content)` - 提供反馈

### IAction (行动层接口)
- `execute(response)` - 执行输出

### ITool (工具接口)
- `execute(**kwargs)` - 执行工具

### ICommsHub (通信中枢接口)
- `send(from_layer, to_layer, message)` - 发送消息
- `request(target, method, params)` - 同步请求

## 设计原则

- 所有接口继承自 `abc.ABC`
- 使用 `@abstractmethod` 强制实现
- 类型注解清晰定义输入输出
