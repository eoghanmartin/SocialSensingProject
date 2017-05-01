import json
import sys
import pdb
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import re

json_file = 'results/results_d3_CH.txt'

# Returns 1 for positive, -1 for neg and 0 for neutral
def SentimentAnalysis(tweet_text):
	####Using NaiveBayesAnalyzer is slow
	#TextBlob_text = TextBlob(tweet_text, analyzer=NaiveBayesAnalyzer())
	#sentiment = TextBlob_text.sentiment.p_pos
	#sentiment_neg = TextBlob_text.sentiment.p_neg
	####
	TextBlob_text = TextBlob(tweet_text)
	sentiment = TextBlob_text.sentiment.polarity
	#print tweet_text, str(sentiment)
	if sentiment <= 0:
		#print tweet_text
		#print str(sentiment)
		return -1
	elif sentiment > .3:
		#print tweet_text
		#print str(sentiment)
		return 1
	
	return 0

hillary_tweets = []
donald_tweets = []

hillary_score = 0
donald_score = 0
donald_hashtags = "#donaldtrump2016|#trump2016|#makeamericasafeagain|#trump2016|#trumptrain|#makeamericagreatagain|#draintheswamp|#HillaryEmails|#neverhillary|#republicans|#hillaryforprison2016|#crookedhillary|#hillaryforprison|#alllivesmatter"
hillary_hashtags = "#notmypresident|#dumptrump|#democrat|#imwithher|#nevertrump|#feminism|#StudentLoanDebt|#StudentLoanForgiveness|#ClimateChange|#GlobalWarming|#IStandWithPP#BlackLivesMatter|#CampaignZero|#StopGunViolence"

with open(json_file) as TweetsFileObj:
	for line in TweetsFileObj:
		tweet = json.loads(line)
		tweet_text = tweet['text'].encode('ascii','ignore')
		sentiment = SentimentAnalysis(tweet_text)
		if re.search(donald_hashtags, tweet["text"]):
			donald_tweets.append(tweet)
			donald_score += 1
			#print tweet["text"]
			#print str(sentiment)
			continue
		if re.search(hillary_hashtags, tweet["text"]):
			hillary_tweets.append(tweet)
			hillary_score += 1
			#print tweet["text"]
			#print str(sentiment)
			continue
		if re.search("RT @HillaryClinton", tweet["text"]):
			hillary_tweets.append(tweet)
			hillary_score += 1
			#print tweet["text"]
			#print str(sentiment)
			continue
		if re.search("RT @realDonaldTrump", tweet["text"]):
			donald_tweets.append(tweet)
			donald_score += 1
			#print tweet["text"]
			#print str(sentiment)
			continue
		if re.search("onald|rump", tweet["text"]) and re.search("illary|linton", tweet["text"]):
			continue
			if sentiment == 1:
				donald_tweets.append(tweet)
				donald_score += 1
			elif sentiment == -1:
				hillary_tweets.append(tweet)
				donald_score -= 1
			#print tweet["text"]
			#print str(sentiment)
			continue
		if re.search("onald|rump", tweet["text"]):
			if sentiment == 1:
				donald_tweets.append(tweet)
				donald_score += 1
			elif sentiment == -1:
				hillary_tweets.append(tweet)
				donald_score -= 1
			else:
				print tweet["text"]
				print str(sentiment)
		elif re.search("illary|linton", tweet["text"]):
			if sentiment:
				hillary_tweets.append(tweet)
				hillary_score += 1
			elif sentiment == -1:
				donald_tweets.append(tweet)
				hillary_score -= 1

#print "There are " + str(len(donald_tweets)) + " tweets for Donald Trump."
#print "There are " + str(len(hillary_tweets)) + " tweets for Hillary Clinton."
htweets = len(hillary_tweets)
dtweets = len(donald_tweets)
print "Percentage in favor for Hillary: " + str(float(htweets) / float(dtweets + htweets))
print "Percentage in favor for Donald: " + str(float(dtweets) / float(dtweets + htweets))
