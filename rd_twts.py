__author__ = 'Imran Farid'

import json
import pandas as pd
from twts_count import word_in_text
import matplotlib.pyplot as plt
import seaborn as sns

# Path to file
tweets_data_path = 'tweets.txt'

# Empty list to store tweets
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Iterate through tweets and store in list
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection
tweets_file.close()

# Build FataFrame of texts and languages with pandas
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])
print(df.head()) # Look at head of DataFrame

# Initialize list to store tweet counts
[toyota, honda, nissan, mazda] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which each car brand is mentioned
for index, row in df.iterrows():
    toyota += word_in_text('toyota', row['text'])
    honda += word_in_text('honda', row['text'])
    nissan += word_in_text('nissan', row['text'])
    mazda += word_in_text('mazda', row['text'])

# Set seaborn style
sns.set(color_codes=True)

# Create list of labels
cd = ['toyota', 'honda', 'nissan', 'mazda']

# Plot histogram
ax = sns.barplot(cd, [toyota, honda, nissan, mazda])
ax.set(ylabel="count")
plt.show()