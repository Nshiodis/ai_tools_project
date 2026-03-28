#文本清洗函数
import re

def clean_text(text: str, to_lower: bool = True) -> str:
    """
    清洗文本：去除首尾空白、合并连续空白，可选转小写。

    Args:
        text: 原始文本
        to_lower: 是否转为小写，默认True

    Returns:
        清洗后的文本
    """
    if not isinstance(text, str):
        text = str(text)

    text = text.strip()
    text = re.sub(r'\s+', ' ', text)

    if to_lower:
        text = text.lower()
    return text

