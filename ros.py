import requests
import re
from lxml import etree
from urllib import request
import os
from queue import Queue
import threading

class rosSpider(object):

    BASE_URL="http://www.mmxyz.net/"


    def parse_page(self,url):
        headers = {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

        }

        response =requests.get(url,headers=headers)
        text =response.text
        # print(text)
        html =etree.HTML(text)

        urls =html.xpath('//div[@class="post-content"]//dt[@class="gallery-icon"]//a')
        # altt =html.xpath('//div[@class="j-r-list-c-img"]//img')
        titles = html.xpath('//d1[@class="gallery-item"]//a')
        for url in urls:
            img = url.get('href')

            title =url.get('title')
            filename = title +'.jpg'
            request.urlretrieve(img, 'images/' + filename)
            print(filename)




    def write_page(self):
        self.head = int(input("初始编号（0-2222）:"))
        self.end = int(input("末尾编号（0-2222而且要大于厨师编号）:"))


    def run(self):

        base_url='http://www.mmxyz.net/rosi-{}'
        self.write_page()
        for x in range(self.head,self.end):
            url =base_url.format(x)
            self.parse_page(url)


if __name__ == '__main__':
    spider =rosSpider()

    spider.run()