from app import app, db
from .models import Article
from flask import render_template
from bs4 import BeautifulSoup
import requests
from sqlalchemy import desc


@app.route('/')
def home():
    hotnews_articles = Article.query.filter_by(source = "Hotnews").order_by(desc(Article.id)).limit(15)
    mediafax_articles = Article.query.filter_by(source = "Mediafax").order_by(desc(Article.id)).limit(15)
    digi_articles = Article.query.filter_by(source="Digi").order_by(desc(Article.id)).limit(15)
    g4media_articles = Article.query.filter_by(source="G4Media").order_by(desc(Article.id)).limit(15)
    context = {
        "hotnews":hotnews_articles,
        "mediafax":mediafax_articles,
        "digi":digi_articles,
        "g4media":g4media_articles,
    }
    return render_template('index.html', title = "Știri", context = context)