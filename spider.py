import requests
import json
import os
from lxml import etree
from selenium import webdriver

query = '李智恩'
downloadPath = 'C:/Users/20180503/PycharmProjects/all/image/李智恩/'


# downloadPath = '/home/lee/data/images/'


def download(scr, id):
    dir = downloadPath + str(id) + '.jpg'
    try:
        pic = requests.get(scr, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')
    if not os.path.exists(downloadPath):
        os.mkdir(downloadPath)
    if os.path.exists(dir):
        print('已存在:' + id)
    return


def searchImages():
    for i in range(0, 1321, 20):
        """
            你条粉肠居然抄漏一个 j
            还在q 后面的等号前后加了空格（这跟命名变量不一样，url 是字符串，空格也是一个字符）
             url = 'https://www.douban.com/search_photo?q = '+query+'&limit=20&start='+str(i)
        """
        url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
        html = requests.get(url).text
        print('html:' + html)
        response = json.loads(html, encoding='utf-8')
        for image in response['images']:
            print(image['src'])
            download(image['src'], image['id'])


"""
    这就是程序的入口，记住这个格式
    if __name__ == "__main__":
    然后在下面写代码去调用上面的函数
"""
if __name__ == "__main__":
    searchImages()
