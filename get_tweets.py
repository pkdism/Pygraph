import tweepy
from textblob import TextBlob

consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

word = input("Enter search term: ")

tweets = api.search(word)

lines = []
c = 1
for tweet in tweets:
	lines.append((str(c)+'. '+tweet.text+'\n').encode('utf-8'))
	c += 1

for i in lines:
	print(i)
	print('\n')