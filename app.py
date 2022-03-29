from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

@app.route('/')
def newsFeed():  # put application's code here
    return render_template('index.html')


@app.route('/news/list')
def newsList():  # put application's code here
    return render_template('list.html')


@app.route('/news/edit')
def newsEdit():  # put application's code here
    return render_template('edit.html')


@app.route('/news/create')
def createNews():  # put application's code here
    return render_template('create.html')


@app.route('/news/article')
def viewNews():  # put application's code here
    return render_template('article.html')


if __name__ == '__main__':
    serve(app, host='127.0.0.1',port=5000)
