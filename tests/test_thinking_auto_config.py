"""测试 config 自动读取思考模式配置"""
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

from container import Container
from src.config import config

print("=" * 50)
print("测试 config 自动读取思考模式配置")
print("=" * 50)
print()
print(f"config.enable_thinking = {config.enable_thinking}")
print(f"config.thinking_mode_high = {config.thinking_mode_high}")
print(f"config.thinking_mode_medium = {config.thinking_mode_medium}")
print(f"config.thinking_mode_low = {config.thinking_mode_low}")
print()
print("结论：不传 enable_thinking 参数时，会根据模型层级自动判断")
print("  - high 层级模型 -> thinking_mode_high")
print("  - medium 层级模型 -> thinking_mode_medium")
print("  - low 层级模型 -> thinking_mode_low")
print()

try:
    agent = Container(log_level="INFO")

    print("=" * 50)
    print("测试 1: type='low' (qwen3.5-flash)")
    print("config.thinking_mode_low=False, 应不启用思考模式")
    print("=" * 50)

    start_time = time.time()
    response = agent.chat(
        prompt="你好，介绍一下你自己",
        provider="qwen",
        type="low",
    )
    elapsed = time.time() - start_time

    print(f"响应：{response.encode('gbk', errors='ignore').decode('gbk')}")
    print(f"耗时：{elapsed:.2f}秒 (应该<2 秒)")
    print()

    print("=" * 50)
    print("测试 2: type='low' (qwen3-max)")
    print("enable_thinking=True, 应启用思考模式")
    print("=" * 50)

    start_time = time.time()
    response = agent.chat(
        prompt="你好，介绍一下你自己",
        provider="qwen",
        type="low",
        enable_thinking=True
    )
    elapsed = time.time() - start_time

    print(f"响应：{response.encode('gbk', errors='ignore').decode('gbk')}")
    print(f"耗时：{elapsed:.2f}秒 (应该>5 秒)")
    print()

except Exception as e:
    print(f"测试失败：{e}")
    import traceback
    traceback.print_exc()
