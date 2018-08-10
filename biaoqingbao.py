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
Cookie = {
    '__cfduid=dda9542773889391fd5551be7788d2e511533814605; UM_distinctid=1651e798b46307-064830d367b856-47e1039-1fa400-1651e798b483f0; CNZZDATA1256911977=1945189220-1533812909-null%7C1533812909; yjs_id=cccc2be012ddbdda338f2e41ffacc13e; ctrl_time=1; XSRF-TOKEN=eyJpdiI6ImNQMDRuTEI2ZVwvQ3lia3pFVEo2UEx3PT0iLCJ2YWx1ZSI6IlJaK2dFSXZENGF4dWNraFNwZ1BUSGUzeDkzdlRnYk1keU5aTEVFS0JjYVRSNzl3aGMrT2oyQlVIaEhXb2tYNHZIdXI1dVlITGw2Z1FEZzJwK3RMOHBnPT0iLCJtYWMiOiJhYjE2NWJjNGRkNTIwZWEzZWVjZmNkNjdiMDI2MTczZTJkYmE5MjZhYjU4ODU5MGFjMzY2M2QxMmI0ODU5YWUyIn0%3D; doutula_session=eyJpdiI6IkFTNUEyXC94N1JLOWZrNnhNWFlTVGZBPT0iLCJ2YWx1ZSI6IlV5M09YYmZSU2JncG5mMWo2U1JOdThESWJuUG02XC82QndzYjhcLytIWXNKR0UwQ2Y5THB4RUlcLzEyR0ZBbFBDQWhCYyszOUNFZU84YXlTekhcL3FMeFNrZz09IiwibWFjIjoiN2JlMWJjMTBlNTNjMzIzZmI5MzE2YTk3M2RkMGI5MmMxYzhmNGZlMGQ0M2FmNDk3NmE2YmYxNDE0NzM4MmIwNSJ9'
}
class Procuder (threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):#可传入所有参数
        super(Procuder,self).__init__(*args,**kwargs)
        self.page_queue =page_queue
        self.img_queue =img_queue
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
        html =etree.HTML(text)
        imgs =html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
        for img in imgs:
            bqbs = img.get('data-original')
            alts = img.get('alt')
            alts =re.sub(r'[\?？\.，。！]','',alts)
            suffix =os.path.splitext(bqbs)[1]
            filename = alts +suffix
            self.img_queue.put((bqbs,filename))

        # request.urlretrieve(bqbs,'images/'+filename)
class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue =page_queue
        self.img_queue =img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            bqbs,filename =self.img_queue.get()
            request.urlretrieve(bqbs,'images/'+filename)
            print(filename)
def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    base_url='http://www.doutula.com/photo/list/?page={}'
    for x in range(1,10):
        url = base_url.format(x)
        page_queue.put(url)
    # parse_page(base_url)
    for x in range(5):
        t = Procuder(page_queue,img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()

if __name__ == '__main__':
    main()