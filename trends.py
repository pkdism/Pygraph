import tweepy

consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

trends_json = api.trends_place(1) #returns a json object. One list object containing a dictionary

data = trends_json[0] #store that dictionary in data

trends = data['trends']
names = []
volume = {}

for trend in trends:
    names.append(trend['name'])
    volume[trend['name']] = trend['tweet_volume']

for name in names:
    print(name, str(volume[name]))