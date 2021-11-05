# https://docs.tweepy.org/en/stable/api.html?highlight=search_tweets#tweepy.API.search_tweets

import tweepy
import pandas as pd
from openpyxl import Workbook

# Auth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
kata_kunci = '#vaksincovid19 -filter:retweets'

tweets = api.search_tweets(q=kata_kunci, result_type='mixed', until='2021-11-05', lang='id', count=100, tweet_mode='extended')

id = []
username = []
text     = []
created_at = []

for tweet in tweets:
    id.append(tweet._json['id'])
    username.append(tweet._json['user']['screen_name'])
    text.append(tweet._json['full_text'])
    created_at.append(tweet._json['created_at'])


dataFrame = pd.DataFrame({
    'id': id,
    'username': username,
    'dibuat_pada': created_at,
    'tweet': text
})

dataFrame.to_excel('hasil-crawling.xlsx', index=False)
