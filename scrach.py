# coding=utf-8
from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import pandas as pd
from datetime import datetime
import calendar
import sys


def add_months(dt,months):
    month = dt.month - 1 + months
    year = dt.year + int(month / 12)
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)

today = datetime.now().date()
today=today.replace(year=2012,month=1,day=1)

print(today)

todaytime = datetime.now()
# todaytime=todaytime.date(2014,1,1)
# print (today.)
print(today.replace(2014).strftime('%Y%m'))

# print(isinstance(demo, unicode))
# with open('a.txt', 'w+', encoding="gb2312") as f:
#     f.write(wpage)


# print(ss.find_all('tr'))
# pd.dataframe

# https://www.aqistudy.cn/historydata/daydata.php?city=%E6%9D%AD%E5%B7%9E&month=2014-12
with open('ZhouShan.csv', 'w+', encoding='utf-8') as f:
    detail=today.strftime('%Y%m')
    while detail<='201902':
        
        response = requests.get(
        'http://qq.ip138.com/weather/zhejiang/ZhouShan/'+detail+'.htm')
        wpage = response.text
        wpage = wpage.encode('iso-8859-1').decode('gb2312')
        soup = BeautifulSoup(wpage, 'html.parser')
        if (soup.find_all('table', id='weatherHistory')!=[]):
            ss = soup.find_all('table', id='weatherHistory')[0]
        else :
            ss = soup.find_all('table',class_='t12')[0]
        month_sum=[]
        for n, i in enumerate(ss):
            if n != 0:
                ii = i.find_all('td')
                s = []
                for item in ii:
                    s.append(re.sub('[\t\n\r]','',item.string))
                month_sum.append(s)
        month_sum=month_sum[::-1]
        for m in month_sum:
            f.writelines(','.join(m)+'\n')
                
        today=add_months(today,1)
        detail=today.strftime('%Y%m')
        print(detail)

