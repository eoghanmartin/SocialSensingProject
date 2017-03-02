# Kurt Davis
# kdavis23
# See Comment below to enter keys/tokens

import tweepy
import sys
import json
from tweepy.streaming import StreamListener
from tweepy import Stream
import pdb

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
				#print data.text.encode('ascii', 'ignore').lower()
				for word in self.keywords: 
					if not data.text.encode('ascii', 'ignore').lower().find(word) == -1:
						#print(data.text)
						print json.dumps(data._json)
						self.tweet_count = self.tweet_count + 1
						return True
			except Exception:
				#print 'Exception occurred'
				pass

			return True
	
	def on_error(self, status):
		print(status)

output_file_name = "results.txt"

#import config file, not included in git repo. Layout is in git README
config_file=open('config.txt','r')
keys=config_file.readlines()
config_file.close()

# Taking keys from config.txt file
#------------------------------------------------------------------------
consumer_key =  str(keys[1].replace('\n', ' ').replace('\r', '').replace(' ', ''))
consumer_secret = str(keys[3].replace('\n', ' ').replace('\r', '').replace(' ', ''))

access_token = str(keys[5].replace('\n', ' ').replace('\r', '').replace(' ', ''))
access_token_secret = str(keys[7].replace('\n', ' ').replace('\r', '').replace(' ', ''))
#------------------------------------------------------------------------

# Open Data file to collect output
sys.stdout = open(output_file_name, 'w')

# Initialize listener. NOTE: arg1 = number of tweets before terminating, arg2 = list of substrings to select
<<<<<<< HEAD
listener1 = textListener(1000, ['trump', 'clinton', 'election', 'potus', 'president', 'white house', 'whitehouse'])
=======
listener1 = textListener(1, ['trump', 'clinton'])
>>>>>>> 37a072ae9c9276a2e04a876c559ee7e28ef1c9c3
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Start listener. NOTE: Hard code desired location here
stream1 = Stream(auth, listener1)
<<<<<<< HEAD
stream1.filter(locations=[-85.7867431641, 42.7696989802, -85.3143310547, 43.292700534])
#stream1.filter(locations=[-86.33,41.63,-86.20, 41.74])
=======
stream1.filter(locations=[-86.33,41.63,-86.20, 41.74])
>>>>>>> 37a072ae9c9276a2e04a876c559ee7e28ef1c9c3
