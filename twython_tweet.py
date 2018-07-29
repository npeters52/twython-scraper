#!/usr/bin/env python
import sys
from twython import Twython
from bs4 import BeautifulSoup
import requests

#web scraping
page_link = 'https://thoughtcosmonaut.com/'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

new_article = page_content.findAll("a", {"class": "top-article-title"})

#twitter posting
tweetStr = new_article

# twitter consumer and access information
apiKey = 'HT1H1WkUhl27GQR73ZMGqTZZ6'
apiSecret = 'lSKbBiDu9THEXIrZJvCpcUTIg3Am0TEZb3rPyWGitj4xI3hT29'
accessToken = '1023648868276162560-7o2uHYhafWz4I6lYWqLmz5DeBPPllc'
accessTokenSecret = '5TLFlMWTENccbxd2EgiV0qCODK4CmWNbeRRb7m2SuRXhD'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print("Tweeted: " + tweetStr)
