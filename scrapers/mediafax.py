#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sqlite3
import os



# Mediafax
mediafax_source = requests.get('https://www.mediafax.ro/').text
mediafax_soup = BeautifulSoup(mediafax_source, 'lxml')
mediafax_root = "https://www.mediafax.ro"
content_news = mediafax_soup.find('div', {'id':'content'})
db = os.environ.get("DB_PATH")


dbConn = sqlite3.connect(db)
cursor = dbConn.cursor()

#Scrape the top title from the page
top_title_a = content_news.find('a', {'class':'title'})
top_title_text = content_news.find('a', {'class':'title'}).text
top_title_link = mediafax_root + top_title_a['href']
mediafax_source = "Mediafax"
sql_top_title = "INSERT OR IGNORE INTO article (title, link, source) VALUES (?, ?, ?);"
mediafax_data_top = (top_title_text, top_title_link,mediafax_source)
cursor.execute(sql_top_title, mediafax_data_top)
dbConn.commit()

#Scrape the rest of the relevant titles
breaking_news = content_news.find('ul').find_all('li')

for news in breaking_news:
    news = news.find('a', {'class':'title'})
    news_text = news['title']
    news_link = mediafax_root + news['href']
    source = "Mediafax"
    sql = "INSERT OR IGNORE INTO article (title, link, source) VALUES (?, ?, ?);"
    data = (news_text, news_link, source)
    cursor.execute(sql, data)
    dbConn.commit()
