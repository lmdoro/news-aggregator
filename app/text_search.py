from app import app
import sqlite3
from flask import render_template, request
import os

db = os.environ.get("DB_PATH")
dbConn = sqlite3.connect(db)
cursor = dbConn.cursor()

@app.route('/search', methods = ['GET'])
def text_search():
    links = []
    w = request.args.get("search")
    searchInput = ('%'+w+'%',)
    sql_link = "SELECT link FROM article WHERE link LIKE ? ORDER BY id DESC"
    cursor.execute(sql_link, searchInput)
    titles_raw = cursor.fetchall()
    for l in titles_raw:
        m = ''.join(l)
        links.append(m)
    return render_template('test.html', title = 'Rezultate', links = links, w = w)
