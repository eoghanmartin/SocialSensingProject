import json
import sys
import pdb
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

json_file = 'results/results_d1_CH.txt'

# Returns 1 for positive, -1 for neg and 0 for neutral
def SentimentAnalysis(tweet_text):
	####Using NaiveBayesAnalyzer is slow
	#TextBlob_text = TextBlob(tweet_text, analyzer=NaiveBayesAnalyzer())
	#sentiment = TextBlob_text.sentiment.p_pos
	#sentiment_neg = TextBlob_text.sentiment.p_neg
	####
	TextBlob_text = TextBlob(tweet_text)
	sentiment = TextBlob_text.sentiment.polarity
	print tweet_text, str(sentiment)
	if sentiment < 0:
		return -1
	elif sentiment > .3:
		return 1
	return 0

hillary_tweets = []
donald_tweets = []

hillary_score = 0
donald_score = 0

with open(json_file) as TweetsFileObj:
	for line in TweetsFileObj:
		tweet = json.loads(line)
		tweet_text = tweet['text'].encode('ascii','ignore')
		sentiment = SentimentAnalysis(tweet_text)
		if tweet_text.find("onald") or tweet_text.find("rump"):
			if sentiment == 1:
				donald_tweets.append(tweet)
				donald_score += 1
			elif sentiment == -1:
				hillary_tweets.append(tweet)
				donald_score -= 1
		elif tweet_text.find("illary") or tweet_text.find("linton"):
			if sentiment:
				hillary_tweets.append(tweet)
				hillary_score += 1
			elif sentiment == -1:
				donald_tweets.append(tweet)
				hillary_score -= 1

print "There are " + str(len(donald_tweets)) + " tweets for Donald Trump."
print "There are " + str(len(hillary_tweets)) + " tweets for Hillary Clinton."
htweets = len(hillary_tweets)
dtweets = len(donald_tweets)
print "Percentage in favor for Hillary: " + str(float(htweets) / float(dtweets + htweets))
print "Percentage in favor for Donald: " + str(float(dtweets) / float(dtweets + htweets))
