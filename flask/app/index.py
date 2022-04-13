from flask import current_app, render_template
from .data import get_crypto
app = current_app

@app.route("/")
def home():
    data=get_crypto()
    print(data[0],data[1])
    return render_template("index.html",plot_urlbtc=data[0],plot_urleth=data[1])