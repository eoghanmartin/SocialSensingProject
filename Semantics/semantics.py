import json
import sys
import pdb
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

json_file = '.\data\debate_1\debate_1_1.json' #tweet_selection.json'

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

	#reseting files
	hillary_file = open('hillary_tweets.json', 'w')
	donald_file = open('donald_tweets.json', 'w')
	other_file = open('other_tweets.json', 'w')
	hillary_file.close()
	donald_file.close()
	other_file.close()

	counter_hillary = 0
	counter_donald = 0

	with open(json_file) as tweet_file:
		hillary_file = open('hillary_tweets.json', 'a')
		donald_file = open('donald_tweets.json', 'a')
		other_file = open('other_tweets.json', 'a')
		for i, tweet_by_line in enumerate(tweet_file):
			tweet = json.loads(tweet_by_line)
			tweet['trump_sentiment'] = 0
			tweet['clinton_sentiment'] = 0
			tweet['other_sentiment'] = 0
			tweet_text = tweet['text'].encode('ascii','ignore')
			sentiment = SentimentAnalysis(tweet_text)

			if (tweet_text.lower().find("donald") > 0) or (tweet_text.lower().find("trump") > 0):
				counter_donald += 1
				tweet['trump_sentiment'] = sentiment
				donald_file.write(str(json.dumps(tweet)) + '\n')
			if (tweet_text.lower().find("hillary") > 0) or (tweet_text.lower().find("clinton") > 0):
				counter_hillary += 1
				tweet['clinton_sentiment'] = sentiment
				hillary_file.write(str(json.dumps(tweet)) + '\n')
			else:
				tweet['other_sentiment'] = sentiment
				other_file.write(str(json.dumps(tweet)) + '\n')
		hillary_file.close()
		donald_file.close()
		other_file.close()

	print '\nHillary Tweets: ', counter_hillary
	print '\nDonald Tweets: ', counter_donald