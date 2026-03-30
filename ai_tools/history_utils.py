import json
from typing import Optional, List, Dict

def save_conversation(conversation: List[Dict[str,str]], filepath: str) -> None:
    """
    将对话历史保存为 JSON 文件。

    Args:
        conversation: 对话列表，每个元素是包含 'role' 和 'content' 的字典
        filepath: 保存路径
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(conversation, f, ensure_ascii=False, indent=2)

def load_conversation(filepath: str) -> list:
    """
    从 JSON 文件加载对话历史。如果文件不存在，返回空列表。

    Args:
        filepath: 文件路径

    Returns:
        对话列表，若文件不存在则为空列表
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("文件不存在，使用默认数据")
        return []
    except json.decoder.JSONDecodeError:
        print("文件内容损坏，使用默认数据")
        return []

def append_message(conversation: List[Dict[str,str]], role: str, content:str,
                   filepath: Optional[str] = None) -> List[Dict[str,str]]:
    """
    向对话列表中添加一条消息，并可选择自动保存。

    Args:
        conversation: 对话列表
        role: 角色（如 'user' 或 'assistant'）
        content: 消息内容
        filepath: 若提供，则自动保存到该文件

    Returns:
        更新后的对话列表
    """
    conversation.append({"role": role, "content": content})
    if filepath:
        save_conversation(conversation, filepath)
    return conversation