#Iterate through broken up tweet files and run a sentiment analysis on each tweet.
#Rewrite to the sentiment_data folder.

import json
import sys
import pdb
import os
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# Returns 1 for positive, -1 for neg and 0 for neutral
def SentimentAnalysis(tweet_text):
	TextBlob_text = TextBlob(tweet_text)
	sentiment = TextBlob_text.sentiment.polarity
	if sentiment < 0:
		return -1
	elif sentiment > 0:
		return 1
	return 0

if __name__ == '__main__':

	counter_hillary = 0
	counter_donald = 0

	debate_number = 1
	source_file_path = "data/debate_" + str(debate_number)
	result_file_path = "sentiment_data/debate_" + str(debate_number)

	path_to_influene_scores = "users_data/debate_1/users_influence_score.json"

	influence_values = {}

	with open(path_to_influene_scores) as influence_file:
		for i, influence_by_line in enumerate(influence_file):
			influence_info = json.loads(influence_by_line)
			user = influence_info['user_id']
			influence = influence_info['influence']
			influence_values[str(user)] = influence

	#file_names = os.listdir(source_file_path)

	#for file_name in file_names:
	file_name = "debate_1_1.json"
	json_file = source_file_path + "/" + file_name
	sentiment_file_path = result_file_path + "/" + file_name
	sentiment_file = open(sentiment_file_path, 'w')

	with open(json_file) as tweet_file:
		for i, tweet_by_line in enumerate(tweet_file):
			tweet = json.loads(tweet_by_line)
			tweet['trump_sentiment'] = 0
			tweet['clinton_sentiment'] = 0
			tweet['other_sentiment'] = 0

			tweet_text = tweet['text'].encode('ascii','ignore')
			tweet_user = tweet['user']['id_str']
			if tweet_user in influence_values:
				tweet['influence'] = influence_values[tweet_user]
			else:
				tweet['influence'] = 0
			
			sentiment = SentimentAnalysis(tweet_text)

			if (tweet_text.lower().find("donald") > 0) or (tweet_text.lower().find("trump") > 0):
				counter_donald += 1
				tweet['trump_sentiment'] = sentiment
			if (tweet_text.lower().find("hillary") > 0) or (tweet_text.lower().find("clinton") > 0):
				counter_hillary += 1
				tweet['clinton_sentiment'] = sentiment
			else:
				tweet['other_sentiment'] = 1
			
			sentiment_file.write(str(json.dumps(tweet)) + '\n')
		sentiment_file.close()

	print '\nHillary Tweets: ', counter_hillary
	print '\nDonald Tweets: ', counter_donald