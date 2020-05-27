#!/usr/bin/bash

export DB_PATH="$HOME/projects/flask/news-aggregator/scraper.db"

$HOME/projects/flask/news-aggregator/scrapers/hotnews.py
$HOME/projects/flask/news-aggregator/scrapers/mediafax.py
$HOME/projects/flask/news-aggregator/scrapers/g4media.py
$HOME/projects/flask/news-aggregator/scrapers/digi.py

