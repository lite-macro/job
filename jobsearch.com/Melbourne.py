from sqlite3 import *
conn = connect('C:\\Users\\ak66h_000\\Documents\\db\\Melbourne.sqlite3')

import requests
from bs4 import BeautifulSoup
from numpy import *
from pandas import *
import re
import datetime

# job_function = 'information-technology-jobs'

#----create table----
def createTable(table):
    c = conn.cursor()
    sql = 'create table {} (jobtitle, company, location, summary, postDate, PRIMARY KEY (jobtitle, company, location, summary))'.format(table)
    c.execute(sql)

createTable('developers_programmers')
createTable('engineering_software')
createTable('web_development_production')

#----insert data----

def insertData(table, job_function, lastPage):
    # first page
    l='Melbourne+VIC'
    # p='1'
    q= job_function
    sp='facet_category'
    surl='0'
    url = 'http://www.jobsearch.com.au/j?l={}&q={}&sp={}&surl={}'.format(l, q, sp, surl)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'}
    source_code = requests.get(url, headers=headers)
    source_code.encoding = 'utf-8'
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    cur = conn.cursor()
    x = soup.find_all("div", class_="job")
    for y in x:
        jobtitle = y.find_all("a", class_="jobtitle")[0].text
        company = y.find_all("span", class_="company")[0].text
        location = y.find_all("span", class_="location")[0].text
        summary = y.find_all("div", class_="summary")[0].text
        postDate = y.find_all("span", class_="date")[0].text
        print(jobtitle, company, location, summary, postDate)
        sql = 'INSERT INTO `{}` VALUES ("{}", "{}", "{}", "{}", "{}")'.format(table, jobtitle, company, location, summary, postDate)
        cur.execute(sql)
    conn.commit()

    # after first page
    for i in range(2, lastPage + 1):
        try:
            l = 'Melbourne+VIC'
            p = str(i)
            q = 'cat%3Adevelopers-programmers'
            sp = 'facet_category'
            surl = '0'
            url = 'http://www.jobsearch.com.au/j?l={}&p={}&q={}&sp={}&surl={}'.format(l, p, q, sp, surl)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'}
            source_code = requests.get(url, headers=headers)
            source_code.encoding = 'utf-8'
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, 'html.parser')
            cur = conn.cursor()
            x = soup.find_all("div", class_="job")
            # x[0].find_all("a", class_="jobtitle")[0].text
            # x[0].find_all("span", class_="company")[0].text
            # x[0].find_all("span", class_="location")[0].text
            # x[0].find_all("div", class_="summary")[0].text
            # x[0].find_all("span", class_="date")[0].text
            for y in x:
                try:
                    jobtitle = y.find_all("a", class_="jobtitle")[0].text
                    company = y.find_all("span", class_="company")[0].text
                    location = y.find_all("span", class_="location")[0].text
                    summary = y.find_all("div", class_="summary")[0].text
                    postDate = y.find_all("span", class_="date")[0].text
                    sql = 'INSERT INTO `{}` VALUES ("{}", "{}", "{}", "{}", "{}")'.format(table, jobtitle, company, location, summary, postDate)
                    cur.execute(sql)
                    conn.commit()
                except Exception as e:
                    print(e)
                    print(jobtitle, company, location, summary, postDate)
                    print('i:', i)
                    pass
        except Exception as e:
            print(e)
            print('----i:', i)
            pass

insertData('developers_programmers', 'cat%3Adevelopers-programmers', 2041//10+1)
insertData('engineering_software', 'cat%3Aengineering-software', 1641//10+1)
insertData('web_development_production', 'cat%3Aweb-development-production', 1421//10+1)
