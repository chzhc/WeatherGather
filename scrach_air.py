# coding=utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import re
import numpy as np
import pandas as pd
from datetime import datetime
import calendar
import sys
import time


def add_months(dt,months):
    month = dt.month - 1 + months
    year = dt.year + int(month / 12)
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)

today = datetime.now().date()
today=today.replace(year=2013,month=12,day=1)
print('start month'+str(today))

driver=webdriver.Chrome()
with open('WenZhou_air_.csv', 'w+', encoding='utf-8') as f:
    detail=today.strftime('%Y%m')
    while detail<='201902':
        driver.get(
        'https://www.aqistudy.cn/historydata/daydata.php?city=温州&month='+detail)
        time.sleep(3)
        elements = driver.find_elements_by_class_name("table")
        ele=elements[0].text.split('\n')
        print(ele[1])
        month_sum=[]
        s=[]
        for n, i in enumerate(ele):
            if n != 0:
                s.append(i)
                # s.append(re.sub('[\t\n\r]','',item.string))
                if n%3==0:
                    s+='\n'
                    month_sum.append(' '.join(s))
                    s=[]
        # month_sum=month_sum[::-1]
        for m in month_sum:
            f.writelines(m)
                
        today=add_months(today,1)
        detail=today.strftime('%Y%m')
        print(detail)

