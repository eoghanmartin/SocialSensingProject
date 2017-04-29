#Create a file with each user and a single tweet from them for influence analysis.

import json
import sys
import pdb
import os
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

origin_file = '.\data\debate_1\debate_1_1.json'

if __name__ == '__main__':

	total_users = []

	debate_number = 1
	source_file_path = "data/debate_" + str(debate_number)

	result_file_path = "users_data/debate_" + str(debate_number)


	file_names = os.listdir(source_file_path)

	number_of_users = 0 

	#for file_name in file_names:
	file_name = "debate_1_1.json"
	origin_file = source_file_path + "/" + file_name
	users_file_path = result_file_path + "/debate_1_users.json"
	users_file = open(users_file_path, 'w')
	
	with open(origin_file) as tweet_file:
		for primary_iterator, tweet in enumerate(tweet_file):
			tweet_load = json.loads(tweet)
			user_id = tweet_load['user']['id_str'].encode('ascii','ignore')
			if user_id not in total_users:
				total_users.append(user_id)
				user_tweet = tweet_load
				user_json = {}
				user_json['user_id'] = user_id
				user_json['tweet'] = user_tweet
				number_of_users += 1
				users_file.write(str(json.dumps(user_json)) + '\n')
		users_file.close()

	print number_of_users