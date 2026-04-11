import time

class MockLLMClient:
    """模拟的大模型客户端，不需要 API Key 和网络"""
    def __init__(self,model:str="mock-model"):
        # 初始化，可以保存模型名称（其实这里用不到）
        self.model=model

    def chat(self, messages, stream=False, callback=None):
        """
        模拟对话方法。
        messages: 消息列表，例如 [{"role": "user", "content": "你好"}]
        stream: 是否流式输出（True 表示一个字一个字地输出）
        callback: 流式输出时，每生成一个字就调用一次这个函数
        """
        # 从 messages 中找到最后一条用户消息的内容
        last_user_msg=None
        for msg in reversed(messages):  # 反向遍历，更快找到最后一条用户消息
            if msg["role"] == "user":
                last_user_msg = msg["content"]
                break

        # 构造一个模拟回复
        reply = f"【模拟回复】您说的是：“{last_user_msg}”。这是一个模拟回复。"

        if stream:
            # 流式模式：逐个字符输出
            for ch in reply:
                if callback:
                    callback(ch)
                else:
                    print(ch,end='', flush=True)   #flush=True：立即将字符输出到屏幕
                time.sleep(0.05) # 每打印一个字符暂停,单纯为了制造明显的流式效果
            return None # 流式模式下不返回完整字符串,可以不写
        else:
            # 非流式模式：直接返回完整回复字符串
            return reply
