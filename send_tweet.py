from TwitterAPI import TwitterAPI


TWEET_TEXT = input("Submit your tweet: ")


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)


r = api.request('statuses/update', {'status': TWEET_TEXT})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')
