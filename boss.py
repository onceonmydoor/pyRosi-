import requests
from lxml import etree
from selenium import webdriver
import time
import re
import csv

from urllib import request


class boosSpider(object):
    driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=boosSpider.driver_path)

        self.url='https://www.zhipin.com/c101010100/h_101010100/?query=pyhon&page=1&ka=page-1'
        self.positions = []
        fp =open('boss.csv','a',newline='',encoding='utf-8')

        self.writer =csv.DictWriter(fp,['name','salary','workyear','city','education','company','content'])
        self.writer.writeheader()
    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_class_name('next')
            if "next disabled" in next_btn.get_attribute("class"):
                break
            else:
                next_btn.click()
            time.sleep(2)

    def parse_list_page(self,source):
        Base_url ="https://www.zhipin.com"
        html = etree.HTML(source)
        links = html.xpath("//div[@class='info-primary']//a[position()=1]/@href")
        #第一个a的位置position()=1
        for link in links:
            url1 = Base_url+link
            self.request_detail_page(url1)
            # print(url)
            time.sleep(3)
    def request_detail_page(self,url):
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    def parse_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath("//div[@class='name']/h1/text()")[0]
        job_request = html.xpath("//div[@class='info-primary']//p/text()")
        city1 = job_request[0]
        city = re.sub('城市：','',city1).strip()
        workyears = job_request[1]
        WY = re.sub('经验：','',workyears).strip()
        education = job_request[2]
        edu = re.sub('学历：','',education).strip()
        company =html.xpath("//h3[@class='name']/a/text()")[0]
        salary = html.xpath("//span[@class='badge']/text()")[0].strip()
        content ="".join(html.xpath("//div[@class='text']/text()")).splitlines()
        position={
            'name':position_name,
            'salary':salary,
            'workyear':WY,
            'city':city,
            'education':edu,
            'company':company,
            'content':content
        }
        self.writer_position(position)
        print("=" * 50)
    def writer_position(self,position):
        self.writer.writerow(position)
        print(position)



if __name__ == '__main__':
    spider = boosSpider()
    spider.run()
