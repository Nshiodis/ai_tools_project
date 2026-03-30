import os
from ai_tools import save_conversation, load_conversation, append_message

HISTORY_DIR = "histories"
os.makedirs(HISTORY_DIR, exist_ok=True)
# 1. 创建一个空对话列表
history=[]
# 2. 添加几条消息
history = append_message(history,"user","你好",
                         os.path.join(HISTORY_DIR, "chat_history.json"))
history = append_message(history,"assistant","你好！有什么可以帮助你？",
                         os.path.join(HISTORY_DIR, "chat_history.json"))
# 3. 查看当前对话
print("当前对话：")
for msg in history:
    print(f"{msg['role']}: {msg['content']}")
# 4. 重新加载，验证持久化
loaded = load_conversation(os.path.join(HISTORY_DIR, "chat_history.json"))
print("\n从文件加载的对话")
for msg in loaded:
    print(f"{msg['role']}: {msg['content']}")
