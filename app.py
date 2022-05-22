from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
from flask_migrate import Migrate
import re

app = Flask(__name__)
app.secret_key = 'app_secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5433/postgres"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.news import News

@app.route('/', methods=['GET', 'POST'])
def newsFeed():  # put application's code here
    category = request.args.get('category')
    if category:
        newsList = db.session.query(News).filter_by(category=category).all()
    else:
        newsList = db.session.query(News).all()
    categories = db.session.query(News).with_entities(News.category).all()
    setCategories = set()
    for count, value in enumerate(categories):
        setCategories.add(str(value).replace('(', '').replace(')', '').replace("'", '').replace(",", ''))

    return render_template('index.html', newsList=newsList, categories=setCategories)


@app.route('/news/article/<int:id>')
def viewNews(id=None):  # put application's code here
    news = News.query.get(id)
    return render_template('article.html', news=news)


if __name__ == '__main__':
    serve(app, host='127.0.0.1',port=5000)
