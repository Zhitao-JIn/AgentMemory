# Router 层 - 多 AI 提供商路由

## 目录结构

```
src/router/
├── __init__.py          # 导出 RouterLayer
├── layer.py             # RouterLayer 协议类
├── router.py            # 路由核心逻辑
├── providers/           # 提供商配置
│   ├── __init__.py
│   ├── anthropic.py
│   ├── openai.py
│   └── google.py
└── strategies/          # 路由策略
    ├── __init__.py
    ├── type_router.py
    └── auto_router.py
```
