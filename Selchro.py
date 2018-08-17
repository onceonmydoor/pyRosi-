from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path =r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')



# driver.execute_script("window.open('https://www.douban.com/')")#使用selenium机器人打开这个网站
# driver.switch_to_window(driver.window_handles[1])
# print(driver.current_url)




# html = driver.page_source
# html.xpath("")

# inputTag1 = driver.find_element_by_id('kw')
# inputTag2 = driver.find_element_by_name('wd')
# inputTag3 = driver.find_element_by_class_name('s_ipt')
# inputTag4 = driver.find_element_by_xpath("//input[@id='kw']")
# inputTag5 = driver.find_element_by_css_selector('.quickdelete-wrap > input')
# inputTag6 = driver.find_element(By.CSS_SELECTOR,'.quickdelete-wrap > input')
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()
# inputTag1.send_keys('python')
submitTag = driver.find_element_by_id('su')
print(type(submitTag))
print(submitTag.get_attribute("value"))
#get_attribute获取
# actions =ActionChains(driver)
#
# actions.move_to_element(inputTag1)
# actions.send_keys_to_element(inputTag1)
# actions.move_to_element(submitTag)
# actions.click(submitTag)
# actions.perform()
#行为链



# for cookie in driver.get_cookies():
#     print(cookie)


# submitTag.click()

# time.sleep(5)
# driver.close()#关闭当前页面
# driver.quit()#退出整个浏览器
#selenium 可以对网页中的一些元素进行操作，点击某个按钮，或者向输入文本框输入
#print(driver.page_source)#打印源代码


