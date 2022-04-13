from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import requests
import mysql.connector
from .flaskSQL import BTC,ETH,XMR,app,db
from flask_sqlalchemy import SQLAlchemy

app.app_context().push()
db.create_all()

response = requests.get('https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&allData=true&api_key={ea0232c4ea8a3007655f1518de6af8ea6c4a5e546ddf83988ec885db9600a11e}')
res=response.json()
res=res['Data']['Data']
for days in res:
  if days['low']>0:
    row=BTC(time=days['time'],high=days['high'],low=days['low'],open=days['open'],close=days['close'],volumeto=days['volumeto'],volumefrom=days['volumefrom'])
    db.session.add(row)
    db.session.commit()

response = requests.get('https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=USD&allData=true&api_key={ea0232c4ea8a3007655f1518de6af8ea6c4a5e546ddf83988ec885db9600a11e}')
res=response.json()
res=res['Data']['Data']
for days in res:
  if days['low']>0:
    row=ETH(time=days['time'],high=days['high'],low=days['low'],open=days['open'],close=days['close'],volumeto=days['volumeto'],volumefrom=days['volumefrom'])
    db.session.add(row)
    db.session.commit()    

response = requests.get('https://min-api.cryptocompare.com/data/v2/histoday?fsym=XMR&tsym=USD&allData=true&api_key={ea0232c4ea8a3007655f1518de6af8ea6c4a5e546ddf83988ec885db9600a11e}')
res=response.json()
res=res['Data']['Data']
for days in res:
  if days['low']>0:
    row=XMR(time=days['time'],high=days['high'],low=days['low'],open=days['open'],close=days['close'],volumeto=days['volumeto'],volumefrom=days['volumefrom'])
    db.session.add(row)
    db.session.commit()