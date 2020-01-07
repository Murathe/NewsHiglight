from flask import Flask,render_template
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def Index():
    # newsapi = NewsApiClient(api_key="c40d6d5c48504741980b4e27910dd4a4")
    # topheadlines = newsapi.get_top_headlines(sources="cnn")

    # articles = topheadlines['articles']

    # news = []
    # desc = []
    # img = []
    

    # for i in range(len(articles)):
    #     myarticles = articles[i]

    #     news.append(myarticles['title'])
    #     desc.append(myarticles['description'])
    #     img.append(myarticles['urlToImage'])

    # mylist = zip(news, desc, img)

    return render_template('index.html')

@app.route('/ars')
def Ars():
    newsapi = NewsApiClient(api_key="c40d6d5c48504741980b4e27910dd4a4")
    topheadlines = newsapi.get_top_headlines(sources="ars-technica")

    articles = topheadlines['articles']

    news = []
    desc = []
    img = []
    pubAt = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, pubAt, url)

    return render_template('ars.html', context = mylist)

@app.route('/google')
def Google():
    newsapi = NewsApiClient(api_key="c40d6d5c48504741980b4e27910dd4a4")
    topheadlines = newsapi.get_top_headlines(sources="google-news")

    articles = topheadlines['articles']

    news = []
    desc = []
    img = []
    pubAt = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, pubAt, url)
    return render_template('google.html', context = mylist)

@app.route('/verge')
def Theverge():
    newsapi = NewsApiClient(api_key="c40d6d5c48504741980b4e27910dd4a4")
    topheadlines = newsapi.get_top_headlines(sources="the-verge")

    articles = topheadlines['articles']

    news = []
    desc = []
    img = []
    pubAt = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, pubAt, url)
    return render_template('verge.html', context = mylist)

@app.route('/bbc')
def Bbc():
    newsapi = NewsApiClient(api_key="c40d6d5c48504741980b4e27910dd4a4")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    news = []
    desc = []
    img = []
    pubAt = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, pubAt, url)

    return render_template('bbc.html', context = mylist)

@app.route('/fox')
def Fox():
    newsapi = NewsApiClient(api_key="c40d6d5c48504741980b4e27910dd4a4")
    topheadlines = newsapi.get_top_headlines(sources="fox-news")

    articles = topheadlines['articles']

    news = []
    desc = []
    img = []
    pubAt = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pubAt.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, pubAt, url)
    return render_template('fox.html', context = mylist)

if __name__ == "__main__":
    app.run(debug = True)