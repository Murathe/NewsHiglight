from flask import Flask,render_template
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

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        poster.append(myarticles['urlToImage'])

    newlist = zip(news, desc, poster)

    return render_template('home.html', context = newlist)