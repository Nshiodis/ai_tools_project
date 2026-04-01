import json
import os
import logging
from os.path import dirname
from typing import Optional, List, Dict

logger = logging.getLogger(__name__)    # __name__ 是模块名，如 'ai_tools.history_utils'

def save_conversation(conversation: List[Dict[str,str]], filepath: str) -> None:
    """
    将对话历史保存为 JSON 文件。如果出错，记录错误但不抛出异常。
    """
    try:
        #确保目录存在
        dir_path = os.path.dirname(filepath)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(conversation, f, ensure_ascii=False, indent=2)
        logger.info(f"成功保存对话历史到{filepath}")
    except(OSError, IOError) as e:
        logger.error(f"保存文件失败:{e}")
    except TypeError as e:
        logger.error(f"对话数据包含不可序列化对象:{e}")
    except Exception as e:
        logger.error(f"保存对话历史时发生未知错误: {e}")

def load_conversation(filepath: str) -> List[Dict[str, str]]:
    """
    从 JSON 文件加载对话历史。如果出错，返回空列表并记录日志。
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data=json.load(f)
        logger.info(f"成功加载对话历史从{filepath}")
        return data
    except FileNotFoundError:
        logger.warning(f"文件不存在:{filepath}，返回空列表")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"JSON解析失败:{e}，返回空列表")
        return []
    except Exception as e:
        logger.error(f"未知错误:{e},返回空列表")
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