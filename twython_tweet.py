#!/usr/bin/env python
import sys
from twython import Twython
from bs4 import BeautifulSoup
import requests

#web scraping
page_link = 'https://thoughtcosmonaut.com/'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

new_article = page_content.findAll("href", {"class": "blog-new-article-parse"})

response = twitter.upload_media(media=new_article)

print(new_article)

#twitter posting
tweetStr = "Check out this new article!"

# twitter consumer and access information
apiKey = 'HT1H1WkUhl27GQR73ZMGqTZZ6'
apiSecret = 'lSKbBiDu9THEXIrZJvCpcUTIg3Am0TEZb3rPyWGitj4xI3hT29'
accessToken = '1023648868276162560-7o2uHYhafWz4I6lYWqLmz5DeBPPllc'
accessTokenSecret = '5TLFlMWTENccbxd2EgiV0qCODK4CmWNbeRRb7m2SuRXhD'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr, media_ids=[response['media_id']])

print("Tweeted: " + tweetStr)
