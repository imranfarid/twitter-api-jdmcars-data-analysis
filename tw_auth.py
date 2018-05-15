__author__ = 'Imran Farid'

import tweepy, json

access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
