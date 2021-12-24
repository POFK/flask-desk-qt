from flask import Flask  
from flask import render_template, redirect
from flask_cors import CORS
from flaskwebgui import FlaskUI # import FlaskUI
import json
import requests

app = Flask(__name__)
CORS(app)
ui = FlaskUI(app, width=1920, height=1080, fullscreen=True) # add app and parameters

url = "http://10.10.0.10"

@app.route("/")
def home():  
    try:
        requests.get(url, 1)
    except:
        return render_template('404.html')
    return redirect(url)

@app.route("/checkurl", methods=['GET'])
def check():
    try:
        requests.get(url, 1)
        return json.dumps({'url': url})
    except:
        return json.dumps({'url': 'none'})


if __name__ == "__main__":
    # app.run() for debug
    ui.run()
