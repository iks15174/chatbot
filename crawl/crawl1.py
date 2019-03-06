import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import django

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawl.settings")
#django.setup()

from data.models import youtube

def makeadr(adr):
    k = adr.find('v')
    adr = adr[k+2:]
    return "https://www.youtube.com/embed/"+adr+"?rel=0;amp;autoplay=1&loop=1&playlist="+adr

def search(adr):
    driver = webdriver.Chrome()
    driver.get(adr)
    time.sleep(1)
    body = driver.find_element_by_tag_name("body")
    num=50
    while num:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        num-=1
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-video-renderer'})
    for li in lis:
        tem = li['title']
        index = tem.find('-')
        if(index==-1):
            continue
        author = tem[:index-1]
        #print(author)
        title = tem[index+2:]
        #print(title)
        address = li['href']
        #print(address)
        youtube(title=title, author = author, link=address).save()
    driver.close()


singer = input()
sing = input()
b = youtube.objects.filter(author__icontains = singer).count()
if b==0:
    print('no object')
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/')
    elem=driver.find_element_by_id('search')
    elem.send_keys(singer)
    but = driver.find_element_by_id('search-icon-legacy').click()
    time.sleep(1)
    adr = driver.current_url
    driver.close()
    search(adr)
    quit()
else:
    b = youtube.objects.filter(author__icontains = singer, title__icontains=sing)
    for ex in b:
        ex.save()
        print(ex.title)
        print(ex.author)
        print(ex.link)
    print(makeadr(b[0].link))
