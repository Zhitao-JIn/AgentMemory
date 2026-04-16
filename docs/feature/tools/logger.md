# tools/logger.py - 日志系统

## 文件职责

使用 loguru 提供统一的日志功能。

## 函数

### setup_logger
```python
def setup_logger(level: str = "INFO") -> None
```
配置全局日志级别。

### get_logger
```python
def get_logger(name: str) -> Logger
```
获取命名日志记录器。

## 日志级别

| 级别 | 输出内容 |
|------|----------|
| ERROR | 错误信息 |
| INFO | 方法调用名 |
| DEBUG | 参数、返回值等详细信息 |
