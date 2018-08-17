from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class qbSpider(object):

    def __init__(self):
        self.login_url="https://kyfw.12306.cn/otn/login/init"
        self.initmy_url="https://kyfw.12306.cn/otn/index/initMy12306"
        self.search_url="https://kyfw.12306.cn/otn/leftTicket/init"
        self.passenger_url="https://kyfw.12306.cn/otn/confirmPassenger/initDc"
        self.driver= webdriver.Chrome(
        executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    )
    def _login(self):
        self.driver.get(self.login_url)
        #显示等待

        WebDriverWait(self.driver,1000).until(
            EC.url_to_be(self.initmy_url)
        )
        print("登陆成功")
    def wait_input(self):
        self.from_station =input("起始站：")
        self.to_station =input("目的地:")
        self.data=input("出发时间（时间格式必须是：YYYY-MM-DD）:")
        self.passengers=input("乘客姓名（如果有多个人用英文逗号隔开）:").split(",")
        self.trains = input("车次（如果有多个人用英文逗号隔开）：")
    def _order_ticket(self):
        #跳转到查询余票界面
        self.driver.get(self.search_url)
        #输入各个信息
        WebDriverWait(self.driver,1000).until(
            EC.text_to_be_present_in_element_value((By.ID,"fromStationText"),self.from_station

        ))
        WebDriverWait(self.driver,1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station

        ))
        WebDriverWait(self.driver,1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "train_data"), self.data

        ))
        WebDriverWait(self.driver,1000).until(
            EC.element_to_be_clickable((By.ID, "query_ticket"))
                                       )
        searchBtn = self.driver.find_element_by_id("query_ticket")
        searchBtn.click()
        WebDriverWait(self.driver,1000).until(
            EC.presence_of_all_elements_located((By.XPATH,".//tboy[@id='queryLeftTable']/tr")
        ))

        #查询是否可以点击
        tr_list = self.driver.find_element_by_xpath(".//tboy[@id='queryLeftTable']/tr[not(@datatran)]")
        for tr in tr_list:
            train_number = tr.find_element_by_class_name("number").text
            if train_number in self.trains:
                left_ticket=tr.find_element_by_xpath(".//td[4]").text
                if left_ticket=="有"or left_ticket.isdigit:#如果是数字或者是‘有’字
                    orderBtn = tr.find_element_by_class_name("btn72")
                    orderBtn.click()
                WebDriverWait(self.driver,1000).until(
                    EC.url_to_be(self.passenger_url)
                )
    def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()


if __name__ == '__main__':
    spider =qbSpider()
    spider.run()