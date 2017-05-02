#Iterate through broken up tweet files and run a sentiment analysis on each tweet.
#Rewrite to the sentiment_data folder.

import json
import sys
import pdb
import os, re
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# Returns 1 for positive, -1 for neg and 0 for neutral
def SentimentAnalysis(tweet_text):
	TextBlob_text = TextBlob(tweet_text)
	sentiment = TextBlob_text.sentiment.polarity
	print tweet_text, str(sentiment)
	if sentiment < 0:
		return -1
	elif sentiment > .3:
		return 1
	return 0

def HashtagClassify(tweet_text):
	donald_hashtags = "#donaldtrump2016|#trump2016|#makeamericasafeagain|#trump2016|#trumptrain|#makeamericagreatagain|#draintheswamp|#hillaryemails|#neverhillary|#republicans|#hillaryforprison2016|#crookedhillary|#hillaryforprison|#alllivesmatter"
	hillary_hashtags = "#notmypresident|#dumptrump|#democrat|#imwithher|#nevertrump|#feminism|#studentloandebt|#studentloanforgiveness|#climatechange|#globalwarming|#istandwithpp|#BlackLivesMatter|#campaignzero|#stopgunviolence"
	
	hillary = 0
	donald = 1
	other = 2

	if re.search(hillary_hashtags, tweet["text"]):
		return hillary
	if re.search(donald_hashtags, tweet["text"]):
		return donald
	if re.search("onald|rump", tweet["text"]) and re.search("illary|linton", tweet["text"]):
		return other
	if re.search("rt @hillaryclinton", tweet["text"]):
		return hillary
	if re.search("rt @realdonaldtrump", tweet["text"]):
		return donald
	if re.search("onald|rump", tweet["text"]):
		return donald
	if re.search("illary|linton", tweet["text"]):
		return hillary
	else:
		return other

def CleanTweet(tweet_text):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet_text).lower().split())

if __name__ == '__main__':

	counter_hillary = 0
	counter_donald = 0

	debate_number = 1
	source_file_path = "data/debate_1"
	result_file_path = "sentiment_data/debate_1"

	path_to_influene_scores = "users_data/users_influence_score.json"

	influence_values = {}

	with open(path_to_influene_scores) as influence_file:
		for i, influence_by_line in enumerate(influence_file):
			influence_info = json.loads(influence_by_line)
			user = influence_info['user_id']
			influence = influence_info['influence']
			influence_values[str(user)] = influence

	file_names = os.listdir(source_file_path)

	for file_name in file_names:
		#file_name = "debate_1_1.json"
		json_file = source_file_path + "/" + file_name
		sentiment_file_path = result_file_path + "/" + file_name
		sentiment_file = open(sentiment_file_path, 'w')

		with open(json_file) as tweet_file:
			for i, tweet_by_line in enumerate(tweet_file):
				tweet = json.loads(tweet_by_line)
				tweet['trump_sentiment'] = 0
				tweet['clinton_sentiment'] = 0
				tweet['other_sentiment'] = 0

				tweet_text_unclean = tweet['text'].encode('ascii','ignore')
				candidate = HashtagClassify(tweet_text_unclean.lower())
				tweet_text = CleanTweet(tweet_text_unclean)
				tweet_user = tweet['user']['id_str']

				if tweet_user in influence_values:
					tweet['influence'] = influence_values[tweet_user]
				else:
					tweet['influence'] = 0
				
				sentiment = SentimentAnalysis(tweet_text)

				if candidate == 1: #for trump tweets
					counter_donald += 1
					if sentiment < 0:
						tweet['clinton_sentiment'] = abs(sentiment)
					else:
						tweet['trump_sentiment'] = sentiment
				if candidate == 0: #for clinton tweets
					counter_hillary += 1
					if sentiment < 0:
						tweet['trump_sentiment'] = abs(sentiment)
					else:
						tweet['clinton_sentiment'] = sentiment
				else:
					tweet['other_sentiment'] = 1
				if tweet['clinton_sentiment'] == tweet['trump_sentiment']:
					tweet['other_sentiment'] = 1
					tweet['trump_sentiment'] = 0
					tweet['clinton_sentiment']  = 0

				if tweet['other_sentiment'] == 0:
					sentiment_file.write(str(json.dumps(tweet)) + '\n')
			sentiment_file.close()

	print '\nHillary Tweets: ', counter_hillary
	print '\nDonald Tweets: ', counter_donald