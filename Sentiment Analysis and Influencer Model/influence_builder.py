#Iterate through each user and one tweet by them. Use tweet details to extract a user influence value.

import json
import sys
import pdb
import os
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

class UserInfluence:
	def __init__(self, user_id, user_tweet):
		self.number_of_tweets = 0
		self.retweets = 0
		self.favorite_count = 0
		self.listed_count = 0
		self.followers = 0
		self.following = 0
		self.user_id = user_id
		self.verified = 0
		self.sample_tweet = user_tweet

	def computeValues(self):
		self.retweets =  self.sample_tweet['retweet_count']
		self.listed_count =  self.sample_tweet['user']['listed_count']
		self.favorite_count =  self.sample_tweet['favorite_count']
		self.number_of_tweets =  self.sample_tweet['user']['statuses_count']
		self.followers =  self.sample_tweet['user']['followers_count']
		self.following =  self.sample_tweet['user']['friends_count']
		self.verified = self.sample_tweet['user']['verified']

	def influenceCalculation(self):
		follower_following_ratio = 0
		influence_discount = 0

		if self.following == 0:
			follower_following_ratio = self.followers
			influence_discount += 2
		else:
			follower_following_ratio = self.followers/self.following #bigger is better
		if self.verified == True:
			influence_discount += 2
		if self.followers < self.following:
			influence_discount = .5
		if follower_following_ratio == 0:
			influence = 0
		else:
			influence = (self.retweets * follower_following_ratio) * influence_discount
		return influence

if __name__ == '__main__':

	total_users = []

	debate_number = 1

	folder_file_path = "users_data/debate_" + str(debate_number)
	users_influence_score = folder_file_path + "/users_influence_score.json"

	#file_names = os.listdir(source_file_path)

	#for file_name in file_names:
	file_name = "debate_1_users.json"

	users_file_path = folder_file_path + "/" + file_name
	users_file = open(users_influence_score, 'w')

	with open(users_file_path) as user_tweets_file:
		for i, user in enumerate(user_tweets_file):
			user_load = json.loads(user)
			user_id  = user_load['user_id'].encode('ascii','ignore')
			user_tweet = user_load['tweet']

			user_influence = UserInfluence(user_id, user_tweet)
			user_influence.computeValues()

			influence_value = user_influence.influenceCalculation()

			user_influence = {}
			user_influence['user_id'] = user_id
			user_influence['influence'] = influence_value

			users_file.write(str(json.dumps(user_influence)) + '\n')
		users_file.close()