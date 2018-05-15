__author__ = 'Imran Farid'

import json
import pandas as pd
from twts_count import word_in_text
import matplotlib.pyplot as plt
import seaborn as sns

tweets_data_path = 'tweets.txt'

tweets_data = []

tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

tweets_file.close()

df = pd.DataFrame(tweets_data, columns=['text', 'lang'])
print(df.head())

[toyota, honda, nissan, mazda] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    toyota += word_in_text('toyota', row['text'])
    honda += word_in_text('honda', row['text'])
    nissan += word_in_text('nissan', row['text'])
    mazda += word_in_text('mazda', row['text'])


sns.set(color_codes=True)

cd = ['toyota', 'honda', 'nissan', 'mazda']

ax = sns.barplot(cd, [toyota, honda, nissan, mazda])
ax.set(ylabel="count")
plt.show()