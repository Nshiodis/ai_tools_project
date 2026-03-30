import os
from ai_tools import AssistantAgent, CodeAgent, TranslatorAgent

assistant = AssistantAgent("小助","通用助手")
code_bot = CodeAgent("码农","编程专家")
translator = TranslatorAgent("翻译官","多语言翻译", target_lang="法语")

# 测试对话
messages = [
    "你好，今天天气不错！",
    "请帮我写一个Python函数计算斐波那契数列。",
    "我想把'你好，世界'翻译成英文。"
]

for msg in messages:
    print(f"用户：{msg}")
    print(assistant.respond(msg))
    print(code_bot.respond(msg))
    print(translator.respond(msg))
    print("-"*50)



# 定义历史文件存放目录
HISTORY_DIR = "histories"
# 如果目录不存在，则创建
os.makedirs(HISTORY_DIR, exist_ok=True)

# 保存 Agent 的历史
assistant.save_history(os.path.join(HISTORY_DIR, "assistant_history.json"))
code_bot.save_history(os.path.join(HISTORY_DIR, "code_bot_history.json"))
translator.save_history(os.path.join(HISTORY_DIR, "translator_history.json"))
print("三个 Agent 的历史已分别保存")
print("-"*50)

# 加载历史（演示）
loaded_assistant = AssistantAgent("小助", "通用助手")
loaded_assistant.load_history(os.path.join(HISTORY_DIR,"assistant_history.json"))
print(f"{loaded_assistant.name}加载的历史条数：{len(loaded_assistant.history)}")
for msg in loaded_assistant.history:
    print(f"{msg['role']}: {msg['content']}")