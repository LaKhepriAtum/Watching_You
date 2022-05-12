from selenium import webdriver
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd



headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

titles_ko = []
contents = []
links = []
images = []

df_orginal = pd.read_csv('C:\\Watching_You\\csv\\final_label.csv')

title = df_orginal[' 한글 이름'].values.tolist()
title_en = df_orginal['영어 이름'].values.tolist()
df = pd.DataFrame()


for title in title:
    url = f'https://terms.naver.com/search.naver?query={title}&searchType=&dicType=&subject='
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    titles_ko.append(title)

    image = soup.find('img',{"class":"lazyLoadImage"})['data-src']
    images.append(image)

    num = soup.find('img',{"class":"lazyLoadImage"})['data-id']
    num = num[2:]


    url2 = f'https://terms.naver.com/entry.naver?docId={num}'
    links.append(url2)


    req = requests.get(url2, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    content = soup.find_all('p', {"class": "txt"})

    if len(content) == 0 :
        content = soup.find_all('p', {"class": "t_txt"})
    if len(content) == 0:
        content = soup.find_all('div', {"class": "atomic-block breakable-block"})
    if len(content) == 0:
        content = soup.find_all('dl', {"class": "summary_area"})
    if len(content) == 0:

        image = soup.find_next_sibling('img', {"class": "lazyLoadImage"})['data-src']
        images.append(image)

        num = soup.find_next_sibling('img', {"class": "lazyLoadImage"})['data-id']
        num = num[2:]

        url2 = f'https://terms.naver.com/entry.naver?docId={num}'
        links.append(url2)
        print(title)




    content_2 = []
    for content in content:
        content = str(content.get_text())
        content = re.compile('[^가-힣1-9一-龥 ()]').sub('', content)
        content_2.append(content)
    content_2 = list(filter(None, content_2))
    a = ''.join(content_2)
    contents.append(a)


df['title'] = titles_ko
df['title_en'] = title_en
df['content'] = contents
df['link'] = links
df['image'] = images


df.to_excel('./cralwing_data.xlsx',encoding='utf-8-sig')
print(df)

