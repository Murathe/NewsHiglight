from flask import Flask
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="c40d6d5c48504741980b4e27910dd4a4")
    