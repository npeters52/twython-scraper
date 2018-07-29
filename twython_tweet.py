#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = raw_input("Input Tweet: ")

# your twitter consumer and access information goes here
apiKey = 'HT1H1WkUhl27GQR73ZMGqTZZ6'
apiSecret = 'lSKbBiDu9THEXIrZJvCpcUTIg3Am0TEZb3rPyWGitj4xI3hT29'
accessToken = '1023648868276162560-7o2uHYhafWz4I6lYWqLmz5DeBPPllc'
accessTokenSecret = '5TLFlMWTENccbxd2EgiV0qCODK4CmWNbeRRb7m2SuRXhD'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print("Tweeted: " + tweetStr)
