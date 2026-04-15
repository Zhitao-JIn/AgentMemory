"""入口 - 五层架构 AI Agent"""
from container import Container


def main():
    agent = Container()

    print("=== AI Agent 就绪 (五层架构) ===")
    print("输入 'quit' 退出\n")

    while True:
        try:
            user_input = input("你：").strip()
            if user_input.lower() in ["quit", "exit"]:
                print("Agent: 再见!")
                break

            response = agent.run(user_input)
            print(f"Agent: {response}\n")

        except KeyboardInterrupt:
            print("\nAgent: 再见!")
            break
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
