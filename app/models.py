from . import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), index = True)
    link = db.Column(db.String(300), index = True, unique = True)
    source = db.Column(db.String(20), index = True)

    def __repr__(self):
        return 'Article {}'.format(self.title)