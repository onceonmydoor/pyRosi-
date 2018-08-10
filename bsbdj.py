import requests
import re
from lxml import etree
from urllib import request
import os
from queue import Queue
import threading

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}

class Procuder (threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):#可传入所有参数
        super(Procuder,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
        #构造函数
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url =self.page_queue.get()
            self.parse_page(url)


    def parse_page(self,url):

        response =requests.get(url,headers=headers)
        text =response.content.decode("utf-8")
        # print(text)
        html =etree.HTML(text)

        imgs =html.xpath('//div[@class="j-r-list-c-img"]//img')
        # altt =html.xpath('//div[@class="j-r-list-c-img"]//img')
        for img in imgs:
            tps = img.get('data-original')
            print(tps)
            alts = img.get('alt')
            print(alts)
            alts = re.sub(r'[\?？\.，。！]','',alts)
            suffix =os.path.splitext(tps)[1]
            filename = alts +suffix
            self.img_queue.put((tps,filename))#用元组封包
            # print(filename)

        # request.urlretrieve(bqbs,'images/'+filename)
class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            abc,filename =self.img_queue.get()#解包
            request.urlretrieve(abc,'images/'+filename)
            print(filename)
def main():
    page_queue = Queue(5)
    img_queue = Queue(200)
    base_url='http://www.budejie.com/pic/{}'
    for x in range(1,5):
        url = base_url.format(x)
        page_queue.put(url)
    # parse_page(base_url)
    for x in range(2):
        t = Procuder(page_queue,img_queue)
        t.start()
    for x in range(6):
        t = Consumer(page_queue, img_queue)
        t.start()

if __name__ == '__main__':
    main()