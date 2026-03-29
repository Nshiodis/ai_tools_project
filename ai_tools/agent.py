class Agent:
    """所有对话代理的基类"""
    def __init__(self, name: str, role: str) -> None:
        """
        初始化代理。

        Args:
            name: 代理的名字（如 "小助"）
            role: 代理的角色描述（如 "通用助手"）
        """
        self.name = name
        self.role = role

    def respond(self, message: str) -> str:
        """
        对用户消息生成回复。子类应重写此方法。

        Args:
            message: 用户输入的消息

        Returns:
            回复字符串
        """
        # 这是一个默认实现，提示子类需要自己实现
        return f"【{self.name}】抱歉，我还没有学会如何回应"

class AssistantAgent(Agent):
    def respond(self, message: str) -> str:
        return f"【{self.name}】收到您的消息：\"{message}\"。我会尽力帮助您"

class CodeAgent(Agent):
    def respond(self, message: str) -> str:
        if "代码" in message or "编程" in message or "Python" in message or "函数" in message:
            return f"【{self.name}】这是一个示例代码：\nprint('Hello,AI!')"
        else:
            return f"【{self.name}】我擅长编程问题，您可以问我关于代码的问题。"

class TranslatorAgent(Agent):
    def __init__(self, name: str, role: str, target_lang: str = "英文") -> None:
        super().__init__(name, role)
        self.target_lang = target_lang
    def respond(self, message: str) -> str:
        return f"【{self.name}】将您的消息翻译成{self.target_lang}: {message} (模拟翻译)"
