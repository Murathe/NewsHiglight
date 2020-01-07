# Project

-NEWS-HIGHLIGHT

by: Murathe Isaac 

## Description

News-highlight is a web appliction that displays a selected news sources from around the globe and goes ahead to re-link them to their respective sites.
With this application, one will be able to:

* See listed news sources and make a selection.
* See description and time the article was posted.
* Click on an article and read it fully from the news source

## Specifications

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources |
| Display articles from a selected news source | **Click a news source** | Redirected to a page with a list of articles from that source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click 'Read more'** | Redirected to the news home page to read the entire article |

### Prerequisites

You need the following installation to run the application localy on your machine:


```

-Python version 3.6
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Getting Started

* Clone `git clone https://github.com/Murathe/NewsHiglight.git`.
* Insatll python3.6.
* Create a virtual environment, open using code
* Visit https://newsapi.org/ and register for an API key and edit app.py with your own api_key.
* 

```

 export NEWS_API_KEY='<Your-Api-Key>'

 python3.6 run.py server

```

* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.


## Technologies Used

* Python 3.6
* Boostrap
* Flask

## License

MIT License

Copyright (c) murathe 2020


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. Copyright (c) 2020 Gitongamiriam
