from flask import Flask
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="c40d6d5c48504741980b4e27910dd4a4")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    poster = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles[])