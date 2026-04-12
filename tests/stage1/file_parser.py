import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置日志记录器：设置级别为 INFO，并定义输出格式（时间 - 级别 - 消息）
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


def parse_file(filepath):
    """
    解析单个文件，统计行数和单词数。

    参数:
        filepath (str): 文件路径

    返回:
        tuple: (文件路径, 行数, 单词数) 若成功；
               (文件路径, None, 错误信息) 若失败
    """
    try:
        # 以 UTF-8 编码读取文件内容
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # 行数 = 换行符个数 + 1（最后一行如果没有换行符也算一行）
        lines = content.count('\n') + 1
        # 单词数 = 按空白字符（空格、换行、制表符等）分割后的元素个数
        words = len(content.split())
        return (filepath, lines, words)
    except Exception as e:
        # 发生任何异常（如文件不存在、编码错误等）返回错误信息
        return (filepath, None, str(e))


def main(folder_path, max_workers=5):
    """
    主函数：并发解析指定文件夹下的所有 .txt 文件。

    参数:
        folder_path (str): 文件夹路径
        max_workers (int): 线程池最大线程数，默认为 5
    """
    # 1. 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        logging.error(f"目录不存在: {folder_path}")
        return

    # 2. 获取所有 .txt 文件的完整路径（列表推导式）
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
    if not files:
        logging.warning("没有找到 .txt 文件")
        return

    logging.info(f"找到 {len(files)} 个文件，开始并发解析...")

    # 3. 使用线程池并发处理
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务：executor.submit(parse_file, f) 返回一个 Future 对象
        # 构建一个字典，将 Future 对象映射到对应的文件路径，便于后续获取结果
        future_to_file = {executor.submit(parse_file, f): f for f in files}

        # 4. 按完成顺序获取结果（as_completed 返回迭代器，每完成一个任务就产生对应的 Future）
        for future in as_completed(future_to_file):
            filepath, lines, words = future.result()
            if lines is not None:
                # 解析成功，记录信息
                logging.info(f"{filepath}: 行数={lines}, 单词数={words}")
            else:
                # 解析失败，记录错误（words 变量此时存放的是错误信息）
                logging.error(f"{filepath}: 解析失败 - {words}")


if __name__ == "__main__":
    # 当直接运行此脚本时，执行 main 函数，测试文件夹为当前目录下的 test_docs
    main("../../test_docs")
