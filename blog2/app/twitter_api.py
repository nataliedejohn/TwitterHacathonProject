import time

import pandas
import pandas as pd
import tweepy
import configparser
from datetime import datetime

def twitter_api_call(search = ""):

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


    public_tweets = api.search_tweets(q=search+"?", locale="en-us", result_type="popular", until=datetime.today().strftime('%Y-%m-%d'))

    columns = ["Time\t", 'User\t', 'Tweet\t']
    data = []
    for tweet in public_tweets:
        data.append(tweet.text)
        #data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

    #print("data: {data}".format(data=data))

    #df = pd.DataFrame(data, columns=columns)

    #print(df)

    #df.to_csv('tweets.csv')

    return data