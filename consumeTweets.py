#!/usr/bin/env python
#
#
# @author John Van Note <johnlvannote@protonmail.com>
#
#

import tweepy
import json
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('twitter_keys.properties')

consumer_key = config.get('Keys', 'consumer_key')
consumer_secret = config.get('Keys', 'consumer_secret')
access_token = config.get('Keys', 'access_token')
access_token_secret = config.get('Keys', 'access_token_secret')

print consumer_key
print consumer_secret
print access_token
print access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

#for tweet in public_tweets:
#  print tweet.text

user = api.get_user("TheApexJVN")
#for friend in user.friends():
#  print friend.screen_name

for tweet in tweepy.Cursor(api.user_timeline,id='TheApexJVN').items():
  #print tweet._json
  print tweet._json["text"]

#def parseJson(jsonRaw):
#  jsonData = json.loads(jsonRaw)
#  ret


