#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sqlite3
import os

g4media_source = requests.get('https://www.g4media.ro/').text
g4media_soup = BeautifulSoup(g4media_source, 'lxml')

db = os.environ.get("DB_PATH")
dbConn = sqlite3.connect(db)
cursor = dbConn.cursor()

# First column - articole
columnOne_articles = g4media_soup.find('div', {'class':'home-articole'}).find_all('h3',{'class':'post-title'})

counter = 0
for article in columnOne_articles:
    if counter<=9:
        counter+=1
        article_text = article.find('a').text
        article_link = article.find('a')['href']
        source = 'G4Media'
        sql = "INSERT INTO article (title, link, source) VALUES (?, ?, ?);" 
        g4media_data = (article_text, article_link, source)
        cursor.execute(sql, g4media_data)
        dbConn.commit()
        
# Second column - anchete
columnTwo_articles = g4media_soup.find('div', {'class':'home-anchete'}).find_all('h3',{'class':'post-title'})
counter = 0
for article in columnTwo_articles:
    if counter<=5:
        counter+=1
        article_text = article.find('a').text
        article_link = article.find('a')['href']
        source = 'G4Media'
        sql = "INSERT OR IGNORE INTO article (title, link, source) VALUES (?, ?, ?);" 
        g4media_data = (article_text, article_link, source)
        cursor.execute(sql, g4media_data)
        dbConn.commit()

#Third column - analize
columnThree_articles = g4media_soup.find('div', {'class':'home-analize'}).find_all('h3',{'class':'post-title'})
counter = 0
for article in columnThree_articles:
    if counter<=5:
        counter+=1
        article_text = article.find('a').text
        article_link = article.find('a')['href']
        source = 'G4Media'
        sql = "INSERT OR IGNORE INTO article (title, link, source) VALUES (?, ?, ?);" 
        g4media_data = (article_text, article_link, source)
        cursor.execute(sql, g4media_data)
        dbConn.commit()
