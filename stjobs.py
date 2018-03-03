from sqlite3 import *
conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\stjobs.sqlite3')

import requests
from bs4 import BeautifulSoup
from numpy import *
from pandas import *
import re
import datetime

job_function = 'information-technology-jobs'
table = 'information_technology'
#----create table----
c = conn.cursor()
sql = 'create table information_technology ( title, company, description, postDate, experience, salary, PRIMARY KEY (title, company, description, postDate, experience, salary))'
c.execute(sql)

#----insert data----
for i in range(1,18):
    url = 'http://www.stjobs.sg/singapore-jobs/{}/view-50-jobs/page{}'.format(job_function, i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'}
    source_code = requests.get(url, headers=headers)
    source_code.encoding = 'utf-8'
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    cur = conn.cursor()
    x = soup.find_all("div", class_="row margin-bottom-20")
    for y in x:
        try:
            L = []
            div = y.find_all("div", class_="company-information-with-logo")
            for div1 in div:
                a = div1.find_all("a", class_="view_companyprofile text-bold")[0].text
                b = div1.find_all("small", style="font-size:85%")[0].text
                c = div1.find_all("small", class_="text-ellipsis-2-lines result-desc-info")[0].text
                l = [a, b, c]
            L += l
            div = y.find_all("div", class_="col-sm-3 col-md-3 col-lg-2 booking-img-description listing-right-info")
            for div1 in div:
                a = div1.find_all("small", class_="job-search-info")[0].text
                b = div1.find_all("small", class_="job-search-info")[1].text
                c = div1.find_all("small", class_="job-search-info")[2].text
                l = [a, b, c]
            L += l

            sql = 'INSERT INTO `{}` VALUES ("{}", "{}", "{}", "{}", "{}", "{}")'.format(table, L[0], L[1], L[2], L[3], L[4], L[5])
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            print(L)
            pass


job_function = 'data-statistical-analysis-jobs'
table = 'data_statistical_analysis'
#----create table----
c = conn.cursor()
sql = 'create table data_statistical_analysis ( title, company, description, postDate, experience, salary, PRIMARY KEY (title, company, description, postDate, experience, salary))'
c.execute(sql)

#----insert data----
for i in range(1,12):
    url = 'http://www.stjobs.sg/singapore-jobs/{}/view-50-jobs/page{}'.format(job_function, i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'}
    source_code = requests.get(url, headers=headers)
    source_code.encoding = 'utf-8'
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    cur = conn.cursor()
    x = soup.find_all("div", class_="row margin-bottom-20")
    for y in x:
        try:
            L = []
            div = y.find_all("div", class_="company-information-with-logo")
            for div1 in div:
                a = div1.find_all("a", class_="view_companyprofile text-bold")[0].text
                b = div1.find_all("small", style="font-size:85%")[0].text
                c = div1.find_all("small", class_="text-ellipsis-2-lines result-desc-info")[0].text
                l = [a, b, c]
            L += l
            div = y.find_all("div", class_="col-sm-3 col-md-3 col-lg-2 booking-img-description listing-right-info")
            for div1 in div:
                a = div1.find_all("small", class_="job-search-info")[0].text
                b = div1.find_all("small", class_="job-search-info")[1].text
                c = div1.find_all("small", class_="job-search-info")[2].text
                l = [a, b, c]
            L += l

            sql = 'INSERT INTO `{}` VALUES ("{}", "{}", "{}", "{}", "{}", "{}")'.format(table, L[0], L[1], L[2], L[3], L[4], L[5])
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            print(L)
            pass