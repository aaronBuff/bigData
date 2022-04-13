import numpy as np
import pandas as pd
from flask import current_app, render_template,Flask
from flaskSQL import BTC,ETH,XMR
from collections import defaultdict
from sqlalchemy import inspect

app = current_app

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

