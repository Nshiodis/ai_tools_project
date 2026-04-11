import logging
from ai_tools import LLMClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

client = LLMClient()

messages = [{"role": "user", "content": "你好，今天天气怎么样？"}]

print("=== 非流式模式 ===")
reply = client.chat(messages, stream=False)
print(reply)

print("\n=== 流式模式 ===")
def my_callback(chunk):
    print(chunk, end='', flush=True)

client.chat(messages, stream=True, callback=my_callback)
print()