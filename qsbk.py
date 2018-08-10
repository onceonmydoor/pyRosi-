import requests
import re
from lxml import etree
from urllib import request
import os
from queue import Queue
import threading
import csv






BASE_url="https://www.qiushibaike.com"
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}
class Procuder (threading.Thread):
    def __init__(self,page_queue,dz_queue,*args,**kwargs):#可传入所有参数
        super(Procuder,self).__init__(*args,**kwargs)
        self.page_queue =page_queue
        self.dz_queue =dz_queue

        #构造函数
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url =self.page_queue.get()
            self.parse_page(url)


    def parse_page(self,url):
        # header = ['链接','段子']
        values = []
        response =requests.get(url,headers=headers)
        text =response.content.decode("utf-8")
        # print(text)
        html =etree.HTML(text)

        dzs =html.xpath('//div[@class="content"]//span')
        hrefs =html.xpath('//div[@id="content-left"]//a/@href')
        href = re.findall('id="qiushi_tag_(\d+)"',text)
        print(href)
        # for href in h
        #     # href refs:= re.findall('/article/\d+',hrefs)
        #     print(href)
        # href_url =BASE_url+href
        # values.append(href_url)
        for dz in dzs:
            duanzis=etree.tostring(dz,encoding='utf-8').decode('utf-8')
            duanzi = re.sub('<.*?>', "", duanzis)
            values.append(duanzi.split())
            print(duanzi.split())

        with open('duanzi.csv','w',encoding='utf-8',newline='') as fp:
            witer = csv.writer(fp)
            # witer.writerow(header)
            # self.lock.a
            witer.writerows(values)
        # imgs =html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
        # for img in imgs:
        #     bqbs = img.get('data-original')
        #     alts = img.get('alt')
        #     alts =re.sub(r'[\?？\.，。！]','',alts)
        #     suffix =os.path.splitext(bqbs)[1]
        #     filename = alts +suffix
        #     self.img_queue.put((bqbs,filename))

        # request.urlretrieve(bqbs,'images/'+filename)
class Consumer(threading.Thread):
    def __init__(self,page_queue,dz_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue =page_queue
        self.dz_queue =dz_queue

    def run(self):
        while True:
            if self.dz_queue.empty() and self.page_queue.empty():
                break

def main():
    page_queue = Queue(10)
    dz_queue = Queue(500)
    glock =threading.Lock()
    base_url='https://www.qiushibaike.com/text/page/{}/'
    for x in range(1,10):
        url = base_url.format(x)
        page_queue.put(url)
        break
    # parse_page(base_url)
    for x in range(5):
        t = Procuder(page_queue,dz_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue, dz_queue)
        t.start()

if __name__ == '__main__':
    main()