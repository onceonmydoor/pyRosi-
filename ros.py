import requests
import re
from lxml import etree
from urllib import request
import os
from queue import Queue
import threading


BASE_URL="http://www.mmxyz.net/"
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}





def parse_page(url):

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






def main():

    base_url='http://www.mmxyz.net/rosi-{}'

    for x in range(2114,2117):
        url =base_url.format(x)
        parse_page(url)


if __name__ == '__main__':
    main()