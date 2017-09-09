#!/usr/bin/env python
#
#
# @author John Van Note <johnlvannote@protonmail.com>
#
#

import ConfigParser
import json
import tweepy

config = ConfigParser.RawConfigParser()
config.read('twitter_keys.properties')

consumer_key = config.get('Keys', 'consumer_key')
consumer_secret = config.get('Keys', 'consumer_secret')
access_token = config.get('Keys', 'access_token')
access_token_secret = config.get('Keys', 'access_token_secret')
user_id = config.get('Keys', 'user_id')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline,id=user_id).items():
  tweet_text = tweet._json['text'].encode('utf-8')
  if not str.startswith(tweet_text, 'RT') and not str.startswith(tweet_text, '@'): 
    print tweet_text
