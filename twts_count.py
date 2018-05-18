__author__ = 'Imran Farid'

import re

# Check for word in tweets
def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False
