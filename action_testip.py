import logging
import os
import re
import sys
import time
from DrissionPage import ChromiumOptions, ChromiumPage


def logging_init():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)
    
    # 确保不重复添加 handler
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # 确保 coco 目录存在
        os.makedirs('coco', exist_ok=True)
        file_handler = logging.FileHandler('coco/coco.log', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    return logger

logger = logging_init()
co = ChromiumOptions().auto_port()
co.headless(True)   # 无头模式
co.set_argument('--no-sandbox')
co.set_argument('--headless=new')
co.set_paths(browser_path="/opt/google/chrome/google-chrome")
browser = ChromiumPage(co)
tab = browser.latest_tab
tab.get('https://user2.1000ws.top/#/register')

ele = tab.ele('css=#emailPrefix')
logger.info(ele)
ele.input('111')
tab.get_screenshot(path=r"./1.png", full_page=True)


