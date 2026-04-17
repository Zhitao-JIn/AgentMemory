"""直接测试 Qwen API - 不使用 LiteLLM"""
import sys
import os
import time
import requests

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 加载环境变量
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("QWEN_API_KEY")
if not api_key:
    print("错误：QWEN_API_KEY 未配置")
    sys.exit(1)

print("=" * 50)
print("Qwen API 直接调用测试 (不使用 LiteLLM)")
print("=" * 50)
print(f"API Key: {api_key[:10]}...{api_key[-5:]}")

# 阿里云百炼 API 地址
url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "qwen3.5-flash",
    "messages": [
        {"role": "user", "content": "你好，请用一句话介绍你自己"}
    ],
    "max_tokens": 100
}

print(f"\n请求地址：{url}")
print(f"模型：qwen3.5-flash")
print()

try:
    start_time = time.time()
    response = requests.post(url, headers=headers, json=data, timeout=30)
    elapsed = time.time() - start_time

    print(f"状态码：{response.status_code}")
    print(f"耗时：{elapsed:.2f}秒")
    print()

    if response.status_code == 200:
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        print("=" * 50)
        print("调用成功!")
        print("=" * 50)
        print()
        print("响应内容:")
        print(content)
        print()
        print("=" * 50)
        print(f"Usage: {result.get('usage')}")
    else:
        print("=" * 50)
        print("调用失败")
        print("=" * 50)
        print(f"响应内容：{response.text}")

except Exception as e:
    print("=" * 50)
    print("调用失败")
    print("=" * 50)
    print(f"错误：{e}")
