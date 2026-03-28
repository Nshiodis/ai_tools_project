#日志打印函数
from datetime import datetime
from typing import Optional
def log_message(level: str, message: str, log_file: Optional[str] = None) -> None:
    """
    打印带时间戳的日志消息，可选写入文件。

    Args:
        level: 日志级别（INFO, WARNING, ERROR）
        message: 日志内容
        log_file: 日志文件路径，若指定则追加写入
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level.upper()}] {message}"
    print(log_line)
    if log_file:
        with open(log_file, "a", encoding='utf-8') as f:
            f.write(log_line + "\n")