import requests
import logging,sys
sys.stdout.reconfigure(encoding="utf-8")  # Python 3.7 及以上适用
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://myip.ipip.net/', headers=headers)
print(response.text)
with open('file.txt', 'w', encoding='utf-8') as file:
    file.writelines(response.text)




def decode_unicode(message):
    return message.encode('utf-8').decode('unicode_escape')

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# 记录包含中文的日志
logging.debug(decode_unicode("这是一个调试信息"))
logging.info(decode_unicode("这是一个信息"))
logging.warning(decode_unicode("这是一个警告"))
logging.error(decode_unicode("这是一个错误"))
logging.critical(decode_unicode("这是一个严重错误"))

