#!/usr/bin/env python3

from TwitterAPI import TwitterAPI


TWEET_TEXT = input("Submit your tweet: ")


CONSUMER_KEY = 'redacted'
CONSUMER_SECRET = 'redacted'
ACCESS_TOKEN_KEY = 'redacted'
ACCESS_TOKEN_SECRET = 'redacted'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)


r = api.request('statuses/update', {'status': TWEET_TEXT})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')
