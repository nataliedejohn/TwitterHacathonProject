import pandas
import pandas as pd
import tweepy
import configparser


def twitter_api_call(search = "?"):

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

    public_tweets = api.search_tweets(search)
    x = 0

    while x < 100:
        public_tweets + (api.search_tweets("poop"))
        x += 1

    columns = ["Time\t", 'User\t', 'Tweet\t']
    data = []
    for tweet in public_tweets:
        data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

    print(data)

    df = pd.DataFrame(data, columns=columns)

    print(df)

    df.to_csv('tweets.csv')
    return data


public_tweets = twitter_api_call("poop")
