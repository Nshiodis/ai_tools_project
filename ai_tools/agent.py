from typing import Dict, List, Optional
from .history_utils import save_conversation, load_conversation

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
        self.history: List[Dict[str,str]] = []

    def _generate_response(self, message: str) -> str:
        """子类重写此方法返回回复"""
        return f"【{self.name}】抱歉，我还没有学会如何回应"

    def _record_message(self, role: str, content: str) -> None:
        """内部方法：记录一条消息到历史"""
        self.history.append({"role": role, "content": content})

    def save_history(self, filepath: str) -> None:
        """保存当前对话历史到文件"""
        save_conversation(self.history, filepath)

    def load_history(self, filepath: str) -> None:
        """从文件加载对话历史到当前实例（替换原有历史）"""
        self.history = load_conversation(filepath)

    def respond(self, message: str) -> str:
        self._record_message("user", message)
        reply = self._generate_response(message) #子类实现
        self._record_message("agent", reply)
        return reply

class AssistantAgent(Agent):
    def _generate_response(self, message: str) -> str:
        return f"【{self.name}】收到您的消息：\"{message}\"。我会尽力帮助您"

class CodeAgent(Agent):
    def _generate_response(self, message: str) -> str:
        if "代码" in message or "编程" in message or "Python" in message or "函数" in message:
            return f"【{self.name}】这是一个示例代码：\nprint('Hello,AI!')"
        else:
            return f"【{self.name}】我擅长编程问题，您可以问我关于代码的问题。"

class TranslatorAgent(Agent):
    def __init__(self, name: str, role: str, target_lang: str = "英文") -> None:
        super().__init__(name, role)
        self.target_lang = target_lang
    def _generate_response(self, message: str) -> str:
        return f"【{self.name}】将您的消息翻译成{self.target_lang}: {message} (模拟翻译)"
