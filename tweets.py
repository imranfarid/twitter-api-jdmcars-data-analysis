__author__ = 'Imran Farid'

import tweepy, json
from tw_auth import auth
from st_class import MyStreamListener

# Initialize Stream Listener
l = MyStreamListener()

# Create Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords
stream.filter(track=['toyota', 'honda', 'nissan', 'mazda'])

