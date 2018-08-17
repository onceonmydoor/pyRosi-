import requests
from lxml import etree
import time
import re

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_pyhon?labelWords=&fromSearch=true&suginput=',
    'Cookie': '_ga=GA1.2.1007242487.1532526367; user_trace_token=20180725214608-15cb373d-9011-11e8-9ee6-5254005c3644; LGUID=20180725214608-15cb3b06-9011-11e8-9ee6-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAFCAAEG319D1432B8FB5917446BAEA57D26E25D; _gat=1; LGSID=20180814192926-4ccd2140-9fb5-11e8-bbda-525400f775ce; PRE_UTM=; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gid=GA1.2.745524975.1534246165; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532526367,1532699996,1532781084,1534246166; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1534246173; LGRID=20180814192933-51272037-9fb5-11e8-bbda-525400f775ce; SEARCH_ID=4e58f21e71bf4a6db9f2306dccbaccd5'
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}


def request_list_page():
    # url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    # headers ={
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    #     'Referer':'https://www.lagou.com/jobs/list_pyhon?labelWords=&fromSearch=true&suginput=',
    #     'Cookie':'_ga=GA1.2.1007242487.1532526367; user_trace_token=20180725214608-15cb373d-9011-11e8-9ee6-5254005c3644; LGUID=20180725214608-15cb3b06-9011-11e8-9ee6-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAFCAAEG319D1432B8FB5917446BAEA57D26E25D; _gat=1; LGSID=20180814192926-4ccd2140-9fb5-11e8-bbda-525400f775ce; PRE_UTM=; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gid=GA1.2.745524975.1534246165; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532526367,1532699996,1532781084,1534246166; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1534246173; LGRID=20180814192933-51272037-9fb5-11e8-bbda-525400f775ce; SEARCH_ID=4e58f21e71bf4a6db9f2306dccbaccd5'
    # }
    # data ={
    #     'first':'true',
    #     'pn':1,
    #     'kd':'python'
    # }
    for x in range(1,10):
        data['pn'] = x
        response = requests.post(url,headers=headers,data=data)
        time.sleep(3)
        #response =requests.post(url,headers=headers,data=data)
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionid = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html'% positionid
            parse_postion_detail(position_url)
            break
        break

def parse_postion_detail(url):
    respone =requests.get(url,headers=headers)
    text = respone.text
    # print(text)
    html = etree.HTML(text)
    position_name =html.xpath("//span[@class='name']/text()")[0]
    job_request = html.xpath("//dd[@class='job_request']//p/span")
    salary = job_request[0].xpath('.//text()')[0]
    print(salary)

    place = job_request[1].xpath('.//text()')[0].strip()
    city =re.sub(r'[\s/]',"",place)
    print(city)
    work_years = job_request[2].xpath('.//text()')[0].strip()
    WY = re.sub(r'[\s/]', "", work_years)
    print(WY)
    education = job_request[3].xpath('.//text()')[0].strip()
    edu = re.sub(r'[\s/]', "", education)
    print(edu)
    content ="".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
    print(content)
    print(position_name)
    #如果返回来的是json文件就会返回一个字典

def main():
    request_list_page()


if __name__ == '__main__':
    main()