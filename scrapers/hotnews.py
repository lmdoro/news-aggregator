#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sqlite3
import os

print(t)
# Hotnews
hotnews_source = requests.get('https://www.hotnews.ro/').text
hotnews_soup = BeautifulSoup(hotnews_source, 'lxml')
center_news = hotnews_soup.find('div', {'class':'center'})
center_news_divs = center_news.find_all('div', {'class':'articol_lead_full'})


db = os.environ.get('DB_PATH')

dbConn = sqlite3.connect(db)
cursor = dbConn.cursor()
counter = 0
for a in center_news_divs:
    if counter <= 14:
        counter+=1
        title = a.find('h2')
        title_text = a.find('h2').text
        link = title.find('a')['href']
        hotnews_source = 'Hotnews'
        sql = "INSERT OR IGNORE INTO article (title, link, source) VALUES (?, ?, ?);" 
        hotnews_data = (title_text, link, hotnews_source)
        cursor.execute(sql, hotnews_data)
        dbConn.commit()



