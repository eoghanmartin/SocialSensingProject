import json
import sys
import pdb
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

json_file = 'tweet_selection.json'

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

	hillary_tweets = []
	donald_tweets = []

	hillary_score = 0
	donald_score = 0

	tweets_object = open(json_file)
	tweets_by_line = tweets_object.readlines()
	hillary_file = open('hillary_tweets.txt', 'w+')
	donald_file = open('donald_tweets.txt', 'w+')

	for line in tweets_by_line:
		tweet = json.loads(line)
		tweet_text = tweet['text'].encode('ascii','ignore')
		sentiment = SentimentAnalysis(tweet_text)

		if tweet_text.find("donald") or tweet_text.find("trump"):
			if sentiment == 1:
				donald_file.write(str(tweet))
				donald_tweets.append(tweet)
				donald_score += 1
			elif sentiment == -1:
				hillary_file.write(str(tweet))
				hillary_tweets.append(tweet)
				donald_score -= 1
		elif tweet_text.find("hillary") or tweet_text.find("clinton"):
			if sentiment:
				hillary_file.write(str(tweet))
				hillary_tweets.append(tweet)
				hillary_score += 1
			elif sentiment == -1:
				donald_file.write(str(tweet))
				donald_tweets.append(tweet)
				hillary_score -= 1
	hillary_file.close()
	donald_file.write(str(tweet))

print "There are " + str(len(donald_tweets)) + " tweets for Donald Trump."
print "There are " + str(len(hillary_tweets)) + " tweets for Hillary Clinton."

print "Score for Hillary: " + str(hillary_score)
print "Score for Donald: " + str(donald_score)