from selenium import webdriver
from lxml import etree
import time
import re



# driver_path =r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#
# driver = webdriver.Chrome(executable_path=driver_path)

class lagouSpider(object):
    driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=lagouSpider.driver_path)

        self.url='https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []
    def run(self):
        self.driver.get(self.url)
        #self.driver.execute_script("window.open('https://www.douban.com/')")
        while True:
            source = self.driver.page_source
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_class_name('pager_next ')
            if "pager_next pager_next_disabled" in next_btn.get_attribute("class"):
                break
            else:
                next_btn.click()
            time.sleep(2)
    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(3)
    def request_detail_page(self,url):
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source =self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    def parse_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        job_request = html.xpath("//dd[@class='job_request']//p/span")
        salary = job_request[0].xpath('.//text()')[0]
        # print(salary)

        place = job_request[1].xpath('.//text()')[0].strip()
        city = re.sub(r'[\s/]', "", place)
        # print(city)
        work_years = job_request[2].xpath('.//text()')[0].strip()
        WY = re.sub(r'[\s/]', "", work_years)
        # print(WY)
        education = job_request[3].xpath('.//text()')[0].strip()
        edu = re.sub(r'[\s/]', "", education)
        # print(edu)
        content = "".join(html.xpath("//dd[@class='job_bt']//text()")).splitlines()
        company = html.xpath("//img[@class='b2']/@alt")[0]

        position ={
            'name':position_name,
            'salry':salary,
            'city':city,
            'workyears':WY,
            'education':edu,
            'content':content,
            'company':company

        }
        self.positions.append(position)
        print(position)
        print("="*50)




if __name__ == '__main__':
    spider = lagouSpider()
    spider.run()
