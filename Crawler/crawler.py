# Kurt Davis
# kdavis23
# See Comment below to enter keys/tokens

import tweepy
import sys
import json
from tweepy.streaming import StreamListener
from tweepy import Stream

class textListener(StreamListener):

	def __init__(self, count, keywords=None, api=None):
		super(textListener, self).__init__()
		self.count = count
		self.keywords = keywords
		self.tweet_count = 0

	def on_status(self, data):
		if self.tweet_count >= self.count:
			return False
		else:
			try:
				for word in self.keywords: 
					if not data.text.lower().find(word) == -1:
						#print(data.text)
						print json.dumps(data._json)
						self.tweet_count = self.tweet_count + 1
						return True
			except Exception:
				print("Exception reading data!")
				pass

			return True
	
	def on_error(self, status):
		print(status)

output_file_name = "results.txt"

# Enter keys here
#------------------------------------------------------------------------
consumer_key =  
consumer_secret = 

access_token = 
access_token_secret = 
#------------------------------------------------------------------------

# Open Data file to collect output
sys.stdout = open(output_file_name, 'w')

# Initialize listener. NOTE: arg1 = number of tweets before terminating, arg2 = list of substrings to select
listener1 = textListener(50, ['trump', 'clinton'])
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Start listener. NOTE: Hard code desired location here
stream1 = Stream(auth, listener1)
stream1.filter(locations=[-86.33,41.63,-86.20, 41.74])
