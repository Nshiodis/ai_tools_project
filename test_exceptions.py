import logging
from ai_tools.history_utils import load_conversation, save_conversation
from ai_tools.agent import AssistantAgent, Agent

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

print("=== 1. 测试文件不存在 ===")
load_conversation("nonexistent.json")

print("\n=== 2. 测试损坏的 JSON ===")
with open("histories/corrupt.json", "w") as f:
    f.write("{")
load_conversation("histories/corrupt.json")

print("\n=== 3. 测试保存到无效路径 ===")
save_conversation([], "C:/invalid/path/history.json")

print("\n=== 4. 测试 Agent 子类异常 ===")
class BrokenAgent(Agent):
    def _generate_response(self, message):
        raise ValueError("故意出错")

broken = BrokenAgent("坏蛋", "测试")
print(broken.respond("你好"))

print("\n=== 5. 测试 Agent 加载不存在文件 ===")
agent = AssistantAgent("小助", "通用助手")
agent.load_history("nonexistent.json")
print("历史记录条数:", len(agent.history))