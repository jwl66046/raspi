#!/usr/bin/env python3

from TwitterAPI import TwitterAPI


TWEET_TEXT = input("Submit your tweet: ")


CONSUMER_KEY = 'Hu6wgwxa6OcOS7PG7oZiGWF0W'
CONSUMER_SECRET = 'gTKXflQhj2NOfsJHj1yTDtz8gfO915H11eMZSD2mFC3pjobCek'
ACCESS_TOKEN_KEY = '4254854320-yK5tPMBGkQvB62YT1IDk0GSifBfPQrGcnA1yjQp'
ACCESS_TOKEN_SECRET = 'AoIzozjkSJzYkDQ9m3KpDxHo97JamkHa1vD6TYZMCURFu'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)


r = api.request('statuses/update', {'status': TWEET_TEXT})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')
