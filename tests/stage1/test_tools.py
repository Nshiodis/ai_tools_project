from ai_tools import clean_text, format_data, log_message

if __name__ == "__main__":
    # 测试文本清洗
    raw = "  Hello   AI   World!  "
    print(clean_text(raw))  # 输出: hello ai world!

    # 测试数据格式化
    data = {"name": "AI模型", "params": [1, 2, 3]}
    print(format_data(data))

    # 测试日志
    log_message("INFO", "测试完成")
    log_message("ERROR", "模型加载失败：文件不存在", log_file="../../app.log")