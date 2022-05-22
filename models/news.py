from app import db


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    category = db.Column(db.String(100))
    description = db.Column(db.String(100))
    content = db.Column(db.String(1000))

    def __init__(self, title, category, description, content):
        self.title = title
        self.category = category
        self.description = description
        self.content = content

    def __repr__(self):
        return '<News %r>' % self.title


db.create_all()