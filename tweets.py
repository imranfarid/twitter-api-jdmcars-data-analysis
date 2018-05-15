__author__ = 'Imran Farid'

import tweepy, json
from tw_auth import auth
from st_class import MyStreamListener

l = MyStreamListener()
stream = tweepy.Stream(auth, l)

stream.filter(track=['toyota', 'honda', 'nissan', 'mazda'])

