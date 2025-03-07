import logging
import sys
import pytz
from datetime import datetime

class BeijingFormatter(logging.Formatter):
    """ 自定义 Formatter，强制使用北京时间 """
    def formatTime(self, record, datefmt=None):
        beijing_tz = pytz.timezone("Asia/Shanghai")
        dt = datetime.fromtimestamp(record.created, beijing_tz)
        return dt.strftime(datefmt or "%Y-%m-%d %H:%M:%S")

def setup_logger(log_filename='app.log', log_level=logging.DEBUG):
    """
    设置日志记录器，支持输出到控制台和文件，确保中文字符正常显示，时间强制使用北京时间。

    :param log_filename: 日志文件的文件名 (默认 'app.log')
    :param log_level: 日志级别，默认 DEBUG
    :return: logger 对象
    """
    # 确保 Python 输出到控制台的编码为 UTF-8 (适用于 Python 3.7+)
    sys.stdout.reconfigure(encoding="utf-8")
    
    # 创建自定义 Logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(log_level)

    # 创建控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)

    # 创建文件处理器
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setLevel(log_level)

    # 创建自定义格式器，使用北京时间
    formatter = BeijingFormatter('%(asctime)s - %(levelname)s - %(message)s')

    # 设置格式器
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 将处理器添加到 logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# 示例
logger = setup_logger()
logger.info("测试日志，应该使用北京时间。")
