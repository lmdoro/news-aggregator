#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sqlite3
import os

digi_source = requests.get('https://www.digi24.ro/').text
digi_soup = BeautifulSoup(digi_source, 'lxml')
digi_root = 'https://www.digi24.ro'
digisport_id = 'digisport'
db = os.environ.get("DB_PATH")

dbConn = sqlite3.connect(db)
cursor = dbConn.cursor()

# First column - top article
column_one_top = digi_soup.find('article', {'class':'article-lg'})
top_article = column_one_top.find('h2', {'class':'article-title'})
top_article_text = top_article.text
top_article_link = digi_root + top_article.find('a')['href']
top_article_source = 'Digi'
top_sql = 'INSERT OR IGNORE INTO article (title, link, source) VALUES (?, ?, ?);'
digi_top_data = (top_article_text, top_article_link, top_article_source)
cursor.execute(top_sql, digi_top_data)
dbConn.commit()

# First column - rest of the articles
column_one_articles = digi_soup.find('div',{'class':'col-8 col-md-7 col-sm-12'}).find_all('article',{'class':'article-alt'})
for article in column_one_articles:
    article_text = article.find('h4', {'class':'article-title'}).text
    article_link = digi_root + article.find('a')['href']
    source = 'Digi'
    sql = 'INSERT OR IGNORE INTO article (title, link, source) VALUES (?, ?, ?);'
    digi_data = (article_text, article_link, source)
    cursor.execute(sql, digi_data)
    dbConn.commit()

    

# Second column
column_two = digi_soup.find('div', {'class':'col-4 col-md-5 col-sm-12'})
column_two_articles = column_two.find_all('article',{'class':'brdr'})
for article in column_two_articles:
    article_text = article.find('h4', {'class':'article-title'}).text
    article_anchor = article.find('a')['href']
    if digisport_id not in article_anchor:
        article_link = digi_root + article_anchor
    else:
        article_link = article_anchor
    source = 'Digi'
    sql = 'INSERT OR IGNORE INTO article (title, link, source) VALUES (?, ?, ?);'
    digi_data = (article_text, article_link, source)
    cursor.execute(sql, digi_data)
    dbConn.commit()

