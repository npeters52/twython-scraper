#!/usr/bin/env python
import sys
from twython import Twython
from bs4 import BeautifulSoup
import requests

#web scraping
page_link = 'https://thoughtcosmonaut.com/'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

new_article = page_content.find("a", {"class": "blog-new-article-parse"})

new_article_image = page_content.find("img", {"class": "preview-image"})

print(new_article)

#twitter posting
tweetStr = str(new_article)

# twitter consumer and access information
apiKey = 'HT1H1WkUhl27GQR73ZMGqTZZ6'
apiSecret = 'lSKbBiDu9THEXIrZJvCpcUTIg3Am0TEZb3rPyWGitj4xI3hT29'
accessToken = '1023648868276162560-7o2uHYhafWz4I6lYWqLmz5DeBPPllc'
accessTokenSecret = '5TLFlMWTENccbxd2EgiV0qCODK4CmWNbeRRb7m2SuRXhD'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

photo = api.upload_media(media=new_article_image)

api.update_status(status="Check out this new article!  " + tweetStr, media_ids=[photo['media_id']])

print("Tweet sent!")
