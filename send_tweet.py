#!/usr/bin/env python
#
#
# @author John Van Note <johnlvannote@protonmail.com>
#
#

"""Consumes Tweets"""

import ConfigParser
import tweepy
import os
from MarkovChain import MarkovChain


PROP_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'twitter_keys.properties')
KEYS = 'Keys'
CON_KEY = 'consumer_key'
CON_SEC = 'consumer_secret'
TOKEN = 'access_token'
TOKEN_SEC = 'access_token_secret'
SRC_USER_ID = 'src_user_id'


def parse_properties(file_name, header):
    """Parses Properties File"""

    config = ConfigParser.RawConfigParser()
    config.read(file_name)

    keys = dict()
    keys[CON_KEY] = config.get(header, CON_KEY)
    keys[CON_SEC] = config.get(header, CON_SEC)
    keys[TOKEN] = config.get(header, TOKEN)
    keys[TOKEN_SEC] = config.get(header, TOKEN_SEC)
    keys[SRC_USER_ID] = config.get(header, SRC_USER_ID)

    return keys


def generate_api(keys):
    """Users Twitter API to get tweets"""

    auth = tweepy.OAuthHandler(keys[CON_KEY], keys[CON_SEC])
    auth.set_access_token(keys[TOKEN], keys[TOKEN_SEC])
    return tweepy.API(auth)


def generate_dict(api, user_id):
    """Generates Dictionary, no RT no @"""

    tweets = list()
    for tweet in tweepy.Cursor(api.user_timeline, id=user_id).items():
        tweet_text = tweet._json['text'].encode('utf-8')
        #tweet_text = json.dumps(tweet).encode('utf-8')
        if not str.startswith(tweet_text, 'RT') and not str.startswith(tweet_text, '@'):
            tweets.append(tweet_text)

    markov_chain = MarkovChain(tweets)
    return markov_chain


def send_tweet(api, tweet):
    """Sends a Tweet"""

    if not isinstance(tweet, str):
        raise TypeError('Tweet must be a String object')

    if len(tweet) > 140:
        raise Exception('Tweet is over maximum length')


    api.update_status(tweet)


def decode(string):
    """Decodes a String"""
    dec_string = string \
        .replace('&amp;', '&') \
        .replace('&lt;', '<') \
        .replace('&gt;', '>')
    return dec_string


def main():
    """Main function"""

    props = parse_properties(PROP_FILE, KEYS)
    api = generate_api(props)
    markov_chain = generate_dict(api, props[SRC_USER_ID])
    #print markov_chain.get_dictionary()

    tweetable = False
    while not tweetable:
        tweet = markov_chain.generate_line()
        tweet = decode(tweet)
        print tweet
        if len(tweet) < 140:
            tweetable = True

    send_tweet(api, tweet)


if __name__ == "__main__":
    main()
