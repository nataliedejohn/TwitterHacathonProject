import time

import pandas
import pandas as pd
import tweepy
import configparser
from datetime import datetime
from datetime import timedelta
import requests
import json

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def twitter_api_call(search = "", weird=False):
    type = "popular"
    if(True):
        type = "mixed"
    public_tweets = api.search_tweets(
        q=search+"?",
        locale="en-us",
        result_type=type,
        until=(datetime.today() - timedelta(days = 1)).strftime('%Y-%m-%d'),
        include_entities=True,
        tweet_mode="extended"
    )

    #columns = ["Time\t", 'User\t', 'Tweet\t']
    data = []
    for tweet in public_tweets:
        #if(hasattr(tweet, 'entities')):
           # if(len(tweet.entities['urls']) > 0):
                #print(tweet.entities)
                #url = tweet.entities['urls'][0]['expanded_url']
        data.append([tweet.full_text])

    #print("data: {data}".format(data=data))
    #df = pd.DataFrame(data, columns=columns)
    #print(df)
    #df.to_csv('tweets.csv')

    return data