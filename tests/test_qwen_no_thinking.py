"""测试 Qwen 3.5-flash 调用 - 不开启思考模式"""
import sys
import os
import time

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 检查 .env 文件
env_path = ".env"
if not os.path.exists(env_path):
    print("=" * 50)
    print("错误：未找到 .env 文件")
    print("请先配置 API Key:")
    print("  cp .env.example .env")
    print("  然后编辑 .env 填入 QWEN_API_KEY")
    print("=" * 50)
    sys.exit(1)

# 加载环境变量
from dotenv import load_dotenv
load_dotenv()

# 检查 API Key
api_key = os.getenv("QWEN_API_KEY")
if not api_key:
    print("=" * 50)
    print("错误：QWEN_API_KEY 未配置")
    print("请在 .env 文件中添加:")
    print("  QWEN_API_KEY=sk-xxx")
    print("=" * 50)
    sys.exit(1)

print("=" * 50)
print("Qwen 3.5-flash API 调用测试 - 不开启思考模式")
print("=" * 50)
print(f"API Key: {api_key[:10]}...{api_key[-5:]}")
print()

# 使用 Router 类测试
try:
    from container import Container
    from src.router.litellm_client import call_litellm
    from src.config import config

    print("创建 Container...")
    agent = Container(log_level="DEBUG")

    print("调用 agent.chat() - provider='qwen', type='low', enable_thinking=False")
    print()

    start_time = time.time()

    # 直接调用 litellm_client 以获取完整响应
    model = "qwen3.5-flash"
    messages = [{"role": "user", "content": "你开启思考模式了吗"}]

    response_dict = call_litellm(
        model=model,
        messages=messages,
        enable_thinking=False,
    )

    elapsed = time.time() - start_time

    print("=" * 50)
    print("调用成功!")
    print("=" * 50)
    print()
    print("完整响应 JSON:")
    import json
    # LiteLLM 返回 ModelResponse 对象，需要转换为字典
    if hasattr(response_dict, 'model_dump'):
        response_dict = response_dict.model_dump()
    print(json.dumps(response_dict, indent=2, ensure_ascii=False))
    print()
    print("=" * 50)
    print(f"耗时：{elapsed:.2f}秒")
    print("=" * 50)
    print()
    print("配置说明:")
    print("- enable_thinking=False: 不启用思考模式")
    print("- 适用于简单任务，响应速度更快")
    print("=" * 50)

except Exception as e:
    print("=" * 50)
    print("调用失败")
    print("=" * 50)
    print(f"错误类型：{type(e).__name__}")
    print(f"错误信息：{e}")
    import traceback
    traceback.print_exc()
    print()
    print("可能的原因:")
    print("1. API Key 无效或已过期")
    print("2. 账户余额不足")
    print("3. 网络连接问题")
    print("=" * 50)

    # 检查是否是认证错误
    error_msg = str(e)
    if "AuthenticationError" in error_msg or "Incorrect API key" in error_msg:
        print()
        print("认证失败 - 请检查:")
        print("1. API Key 是否正确复制（无多余空格）")
        print("2. 阿里云账户是否完成实名认证")
        print("3. 账户是否有足够余额")
        print("4. API Key 是否已激活")
        print()
        print("获取 API Key: https://bailian.console.aliyun.com/")
    sys.exit(1)
