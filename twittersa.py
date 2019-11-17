# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 22:05:07 2019

@author: MOUNIKA
"""

import tweepy


import time


# input your credentials here
CONSUMER_KEY = "Q74bgNye4vyH55YGCwR98IGcy" 
CONSUMER_SECRET = "FDyfzpNSYCztOOEp6O3tBNIhqBzn9zr9HAIzlWxclSXaNtIPHT"
ACCESS_TOKEN = "117571199488573O3O4gPPOh7jrgvNeflPk2Ma71FCfQ884yg"
ACCESS_TOKEN_SECRET = "icZLkEIYXNZDjfZWBy51 WJcKGQ4mA6gAhDFaazIByuLzh"
time.sleep(100)  

#Authorization
auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

fout=open('Tweets.txt','w')

for tweet in public_tweets:
    print(tweet.text)
    
    fout.write(tweet.text)
    
fout.close()
    
    