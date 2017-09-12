#!/usr/bin/env python
#
#
# @author John Van Note <johnlvannote@protonmail.com>
#
#

"""Consumes Tweets"""

import ConfigParser
import tweepy
from MarkovChain import MarkovChain

PROP_FILE = 'twitter_keys.properties'
SKEYS = 'Source_Keys'
DKEYS = 'Destination_Keys'
CON_KEY = 'consumer_key'
CON_SEC = 'consumer_secret'
TOKEN = 'access_token'
TOKEN_SEC = 'access_token_secret'
USER_ID = 'user_id'


def parse_properties(file_name, header):
    """Parses Properties File"""

    config = ConfigParser.RawConfigParser()
    config.read(file_name)

    keys = dict()
    keys[CON_KEY] = config.get(header, CON_KEY)
    keys[CON_SEC] = config.get(header, CON_SEC)
    keys[TOKEN] = config.get(header, TOKEN)
    keys[TOKEN_SEC] = config.get(header, TOKEN_SEC)
    keys[USER_ID] = config.get(header, USER_ID)

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


def main():
    """Main function"""

    src_props = parse_properties(PROP_FILE, SKEYS)
    src_api = generate_api(src_props)
    markov_chain = generate_dict(src_api, src_props[USER_ID])
    #print markov_chain.get_dictionary()

    tweet = markov_chain.generate_line()
    print tweet
    properties = parse_properties(PROP_FILE, DKEYS)
    api = generate_api(properties)
    send_tweet(api, tweet)


if __name__ == "__main__":
    main()
