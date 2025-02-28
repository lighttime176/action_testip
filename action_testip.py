import requests
import logging,sys
sys.stdout.reconfigure(encoding="utf-8")  # Python 3.7 及以上适用
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# response = requests.get('https://myip.ipip.net/', headers=headers)
print('中文字符')
# with open('file.txt', 'w', encoding='utf-8') as file:
#     file.writelines(response.text)



print(sys.getdefaultencoding())  # 检查默认编码
# 创建自定义 Logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# 创建控制台处理器和文件处理器
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log', encoding='utf-8')

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
