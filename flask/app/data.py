import numpy as np
import pandas as pd
from flask_mysqldb import MySQL
from flask import current_app, render_template,Flask
from .flaskSQL import BTC,ETH,XMR
from collections import defaultdict
from sqlalchemy.inspection import inspect

app = Flask(__name__)

def query_to_dict(rset):
    result = defaultdict(list)
    for obj in rset:
        instance = inspect(obj)
        for key, x in instance.attrs.items():
            result[key].append(x.value)
    return result

def get_crypto():
    btc=pd.DataFrame(query_to_dict(BTC.query.all()))
    eth=pd.DataFrame(query_to_dict(ETH.query.all()))
    xmr=pd.DataFrame(query_to_dict(XMR.query.all()))
    data=[btc,eth,xmr]
    # print(data)
    return data

