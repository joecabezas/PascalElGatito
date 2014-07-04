#!/usr/bin/env python

#TODO: USE TWYTHON HERE
import tweepy

CONSUMER_KEY = 'CzxUgBDrcYSfA3vDcwnQtCnPq'
CONSUMER_SECRET = 'UjmpMSRpyWeIA7tqwC63L3LsWKfMvkbLpyBw3xVS9f180MQXpo'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret