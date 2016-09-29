from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@10.1.1.3/crawltest'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120),unique=True)

    def __init__(self, username, email,password):
        self.username = username
        self.email = email
        self.password = email

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    pass
if __name__ == '__main__':
    app.run(debug=True)