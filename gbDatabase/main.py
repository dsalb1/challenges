#pip install flask
#pip install flask_sqlalchemy
#pip install pymysql
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

"""establish application properties to connect to mysql database"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gatewayblend:challenge@localhost:3306/gatewayblend'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
"""
To build the database on localhost I used the following commands in my terminal (Git Bash on windows):
>>>python -i
>>>from main import db, Article, Slide
>>>db.create_all()
"""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(60))
    email = db.Column(db.String(120))
    articles = db.relationship('Article', backref='user') #one to many relationship with the Article class

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    slides = db.relationship('Slide', backref='article') #one to many relationship with the Slide class
    author_id = db.Column(db.Integer, db.ForeignKey('user.id')) #many to one relationship with the User class
    
    def __init__(self, title, author):
        self.title = title
        self.user = author

class Slide(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    imagePath = db.Column(db.Text) #path to disk holding appropriate image
    body = db.Column(db.Text)
    source = db.column(db.String(120)) #link to the source of the information for the slide
    article_id = db.Column(db.Integer, db.ForeignKey('article.id')) #many to one relationship with the Article class

    def __init__(self, title, imagePath, body, source, article):
        self.title = title
        self.imagePath = imagePath
        self.body = body
        self.source = source
        self.article = article


"""
Debugging code. The route handler creates Article, Slide, and User objects to save to the database. The handler will also return 
the title of the slide using a database query. I used this to make sure the database, queries, and commits were working 
properly, but it lets you see my logic.
"""
@app.route("/")
def index():
    dan = User("daniel", "password", "daniel.j.salberg@gmail.com")
    db.session.add(dan)
    article = Article("first article", dan)
    db.session.add(article)
    slide = Slide("harry potter", "path/blahblahblah.jpg", "content content content", "reddit.com", article)
    db.session.add(slide)
    db.session.commit()
    show_slide = Slide.query.get(1)
    return show_slide.title #prints the title of the slide to the browser



if __name__ == '__main__':
    app.run()
