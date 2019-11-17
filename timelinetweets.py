# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:45:14 2019

@author: MOUNIKA
"""

import tweepy
consumer_key = "Q74bgNye4vyH55YGCwR98IGcy"
consumer_secret = "FDyfzpNSYCztOOEp6O3tBNIhqBzn9zr9HAIzl Wxcl SXaNtIPHT"
access_token = "117571199488573O3O4gPPOh7jrgvNeflPk2Ma71FCfQ884yg"
access_token_secret = "icZLkEIYXNZDjfZWBy51 WJcKGQ4mA6gAhDFaazIByuLzh"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print(tweet.text)