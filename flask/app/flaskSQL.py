from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, Float

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost:3306/flaskproj"
db = SQLAlchemy(app)

class BTC(db.Model):
    __tablename__ = 'btc'
    time = db.Column(db.Float(), primary_key=True)
    high = db.Column(db.Float())
    low = db.Column(db.Float())
    open = db.Column(db.Float())
    close = db.Column(db.Float())
    volumeto = db.Column(db.Float())
    volumefrom = db.Column(db.Float())
    
    if __name__ == "__main__":
        app.run(debug=True)

class ETH(db.Model):
    __tablename__ = 'eth'
    time = db.Column(db.Float(), primary_key=True)
    high = db.Column(db.Float())
    low = db.Column(db.Float())
    open = db.Column(db.Float())
    close = db.Column(db.Float())
    volumeto = db.Column(db.Float())
    volumefrom = db.Column(db.Float())
    
    if __name__ == "__main__":
        app.run(debug=True)

class XMR(db.Model):
    __tablename__ = 'xmr'
    time = db.Column(db.Float(), primary_key=True)
    high = db.Column(db.Float())
    low = db.Column(db.Float())
    open = db.Column(db.Float())
    close = db.Column(db.Float())
    volumeto = db.Column(db.Float())
    volumefrom = db.Column(db.Float())
    
    if __name__ == "__main__":
        app.run(debug=True)

