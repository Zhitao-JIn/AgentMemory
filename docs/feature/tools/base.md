# tools/base.py - 工具基类

## 文件职责

定义工具的抽象基类。

## BaseTool 类

| 属性/方法 | 类型 | 说明 |
|-----------|------|------|
| `name` | str | 工具名称 |
| `execute(**kwargs)` | Any | 执行工具 |
