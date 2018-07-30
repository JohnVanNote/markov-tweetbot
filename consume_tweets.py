#!/usr/bin/env python
#
# @author John Van Note <johnlvannote@protonmail.com>
#

"""Consumes Tweets"""

import ConfigParser
import json
import tweepy

PROP_FILE = 'twitter_keys.properties'
KEYS = 'Keys'
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


def print_tweets(api, user_id):
    """Prints tweets to stdout no RT no @"""

    for tweet in tweepy.Cursor(api.user_timeline, id=user_id).items():
        #tweet_text = tweet._json['text'].encode('utf-8')
        tweet_text = json.dumps(tweet).encode('utf-8')
        if not str.startswith(tweet_text, 'RT') and not str.startswith(tweet_text, '@'):
            print tweet_text


def main():
    """Main function"""

    properties = parse_properties(PROP_FILE, KEYS)
    api = generate_api(properties)
    print_tweets(api, properties[USER_ID])


if __name__ == "__main__":
    main()
