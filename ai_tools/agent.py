import logging
from typing import Dict, List, Optional
from .history_utils import save_conversation, load_conversation

logger = logging.getLogger(__name__)

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
        """保存对话历史，捕获异常并记录日志"""
        save_conversation(self.history, filepath)

    def load_history(self, filepath: str) -> None:
        """加载对话历史，若失败则保持原历史不变"""
        try:
            loaded = load_conversation(filepath)
            self.history = loaded
            logger.info(f"成功加载 {len(self.history)} 条历史记录")
        except Exception as e:
            logger.error(f"加载历史时出错: {e}")

    def respond(self, message: str) -> str:
        """生成回复，确保即使子类出错也有兜底"""
        try:
            self._record_message("user", message)
            reply = self._generate_response(message) #子类实现
            self._record_message("agent", reply)
            return reply
        except Exception as e:
            logger.error(f"生成回复时出错: {e}")
            return f"【{self.name}】抱歉，我遇到了一些问题，暂时无法回复。"

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
