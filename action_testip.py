import logging
import sys

sys.stdout.reconfigure(encoding="utf-8")  # 确保 Python 3.7+ 环境下控制台输出编码为 UTF-8

# 创建自定义 Logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# 创建控制台处理器，显式设置编码为 UTF-8
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# 创建文件处理器，显式设置编码为 UTF-8
file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# 创建日志格式器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 设置格式器
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将处理器添加到 logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 记录日志
logger.debug("这是一个调试信息")
logger.info("这是一个信息")
logger.warning("这是一个警告")
logger.error("这是一个错误")
logger.critical("这是一个严重错误")
