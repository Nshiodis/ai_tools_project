import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def parse_file(filepath):
    """解析单个文件，返回 (文件路径, 行数, 单词数) 或 (文件路径, None, 错误信息)"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.count('\n') + 1
        words = len(content.split())
        return(filepath, lines, words)
    except Exception as e:
        return(filepath, None, str(e))

def main(folder_path, max_workers=5):
    # 1. 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        logging.error(f"目录不存在: {folder_path}")
        return

    # 2. 获取所有 .txt 文件的完整路径
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
    if not files:
        logging.warning("没有找到 .txt 文件")
        return
    logging.info(f"找到 {len(files)} 个文件，开始并发解析...")

    #3. 使用线程池并发处理
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务，得到一个 future 到文件路径的映射字典
        future_to_file={executor.submit(parse_file, f):f for f in files}

        # 4. 按完成顺序获取结果
        for future in as_completed(future_to_file):
            filepath, lines, words = future.result()
            if lines is not None:
                logging.info(f"{filepath}: 行数={lines}, 单词数={words}")
            else:
                logging.error(f"{filepath}: 解析失败 - {words}")

if __name__ == "__main__":
    # 请将这里的路径替换为你自己创建的测试文件夹路径
    main("test_docs")
# 生成一个编码错误的文件（放在 test_docs 目录下）