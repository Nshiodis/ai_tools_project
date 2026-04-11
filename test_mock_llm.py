from ai_tools import MockLLMClient

# 1. 创建客户端实例
client = MockLLMClient()

# 2. 准备消息（对话历史）
messages=[
    {"role":"user","content":"你好，今天天气怎么样？"}
]

# 3. 非流式调用
print("===非流式模式===")
reply=client.chat(messages,stream=False)
print(reply)

# 4. 流式调用（使用回调函数打印每个字符）
print("\n=== 流式模式 ===")
def my_callback(char):
    print(char,end='',flush=True)   # 每收到一个字符就打印，不换行

client.chat(messages,stream=True,callback=my_callback)
print() # 最后换行