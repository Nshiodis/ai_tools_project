#数据格式化函数
import json #导入 Python 内置的 JSON 模块，用来处理 JSON 数据的转换
from typing import Any #从 typing 模块导入 Any，表示任意类型。data: Any 说明 data 参数可以是任何类型的值（字典、列表、数字等）。

def format_data(data: Any, indent: int = 2) -> str:  #indent：缩进空格数，默认 2
    """
    将数据格式化为可读的JSON字符串。

    Args:
        data: 任意可JSON序列化的数据
        indent: 缩进空格数，默认2

    Returns:
        格式化后的JSON字符串，若失败返回错误信息
    """
    try:
        return json.dumps(data, ensure_ascii=False, indent=indent) #将 Python 对象 data 转换为 JSON 字符串 ensure_ascii=False：允许输出非 ASCII 字符（如中文、emoji）
    except (TypeError, ValueError) as e:
        return f"格式化失败:{e}"