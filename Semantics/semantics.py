	
import json
import sys
import pdb
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

#import tweets
tweet_file = open('PresidentialDebate(DonaldTrump-HillaryClinton)Sep_26_2016.json','r')
test_tweet_json = tweet_file.readline()
tweet_file.close()

test_tweet = json.loads(test_tweet_json)

#Sentement analysis
NFKD_text = test_tweet['text'].encode('ascii','ignore')
TextBlob_text = TextBlob(NFKD_text)
polarity = TextBlob_text.sentiment.polarity
subjectivity = TextBlob_text.sentiment.subjectivity
TextBlob_text = TextBlob(NFKD_text, analyzer=NaiveBayesAnalyzer())
classification = TextBlob_text.sentiment.classification
p_pos = TextBlob_text.sentiment.p_pos
p_neg = TextBlob_text.sentiment.p_neg

print "Tweet text: " + NFKD_text

print "\nThis tweet is " + str(p_pos) + "% positive."
print "This tweet is " + str(p_neg) + "% negative."