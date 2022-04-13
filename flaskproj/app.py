from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
from collections import defaultdict
from sqlalchemy import inspect
import pandas as pd
api_key='api_key={ea0232c4ea8a3007655f1518de6af8ea6c4a5e546ddf83988ec885db9600a11e}'
btcUrl='https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&allData=true&'
ethUrl='https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=USD&allData=true&'
xmrUrl='https://min-api.cryptocompare.com/data/v2/histoday?fsym=XMR&tsym=USD&allData=true&'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskproj.sqlite3'

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

class ETH(db.Model):
    __tablename__ = 'eth'
    time = db.Column(db.Float(), primary_key=True)
    high = db.Column(db.Float())
    low = db.Column(db.Float())
    open = db.Column(db.Float())
    close = db.Column(db.Float())
    volumeto = db.Column(db.Float())
    volumefrom = db.Column(db.Float())
    
   
class XMR(db.Model):
    __tablename__ = 'xmr'
    time = db.Column(db.Float(), primary_key=True)
    high = db.Column(db.Float())
    low = db.Column(db.Float())
    open = db.Column(db.Float())
    close = db.Column(db.Float())
    volumeto = db.Column(db.Float())
    volumefrom = db.Column(db.Float())

def __init__(self,time,high,low,open,close,volumeto,volumefrom):
    self.time = time
    self.high = high
    self.low = low
    self.open = open
    self.close = close
    self.volumeto = volumeto
    self.volumefrom = volumefrom

db.create_all()
db.session.commit()

def dbConfig():
    resBTC = requests.get(btcUrl+api_key).json()['Data']['Data']
    resETH = requests.get(ethUrl+api_key).json()['Data']['Data']
    resXMR = requests.get(xmrUrl+api_key).json()['Data']['Data']
            
    for days in resBTC:
        if days['low']>0:
            row=BTC(time=days['time'],high=days['high'],low=days['low'],open=days['open'],close=days['close'],volumeto=days['volumeto'],volumefrom=days['volumefrom'])
            db.session.add(row)

    for days in resETH:
        if days['low']>0:
            row=ETH(time=days['time'],high=days['high'],low=days['low'],open=days['open'],close=days['close'],volumeto=days['volumeto'],volumefrom=days['volumefrom'])
            db.session.add(row)

    for days in resXMR:
        if days['low']>0:
            row=XMR(time=days['time'],high=days['high'],low=days['low'],open=days['open'],close=days['close'],volumeto=days['volumeto'],volumefrom=days['volumefrom'])
            db.session.add(row)

    db.session.commit()

def query_to_dict(rset):
    result = defaultdict(list)
    for obj in rset:
        instance = inspect(obj)
        for key, x in instance.attrs.items():
            result[key].append(x.value)
    return result

def get_crypto():
    btc=BTC.query.all()
    eth=ETH.query.all()
    xmr=XMR.query.all()
    btc=pd.DataFrame(query_to_dict(btc))
    eth=pd.DataFrame(query_to_dict(eth))
    xmr=pd.DataFrame(query_to_dict(xmr))
    data=[btc,eth,xmr]
    print(data)
    return data

@app.route('/')
def home():
    return "hi"