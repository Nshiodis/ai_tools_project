from ai_tools import AssistantAgent, CodeAgent, TranslatorAgent

assistant = AssistantAgent("小助","通用助手")
code_bot = CodeAgent("码农","编程专家")
translator = TranslatorAgent("翻译官","多语言翻译", target_lang="法语")

# 定义测试消息列表
messages = [
    "你好，今天天气不错！",
    "请帮我写一个Python函数计算斐波那契数列。",
    "我想把'你好，世界'翻译成英文。"
]

# 循环测试
for msg in messages:
    print(f"用户: {msg}")
    print(assistant.respond(msg))
    print(code_bot.respond(msg))
    print(translator.respond(msg))
    print("-" * 50)