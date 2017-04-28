import json
import sys
import pdb
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import time

json_file = 'C:\Users\Eoghan\Desktop\PresidentialDebate(DonaldTrump-HillaryClinton)Sep_26_2016.json'#'tweet_selection.json'

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

	sliding_window = 5000
	max_line = 500000
	current_line = 0
	finish_line = current_line + sliding_window

	file_number = 1
	debate_number = 1

	iterator = 0

	election_file = open('data/debate_'+str(debate_number)+'/debate_'+str(debate_number)+'_'+str(file_number)+'.json', 'w')
	start_time = time.time()

	with open(json_file) as tweet_file:
		for iterator, tweet_by_line in enumerate(tweet_file):
			#pdb.set_trace()
			if iterator >= current_line and iterator <= finish_line:
				tweet = json.loads(tweet_by_line)
				tweet_text = tweet['text'].encode('ascii','ignore')
				#sentiment = SentimentAnalysis(tweet_text)
				election_file.write(str(tweet_by_line))
			elif iterator > finish_line:
				election_file.close()
				print str(finish_line)
				current_line = finish_line + 1
				finish_line = finish_line + sliding_window
				file_number += 1
				finish_time = time.time()
				total_time = finish_time - start_time
				print total_time
				if finish_line > max_line:
					break
				else:	
					election_file = open('data/debate_'+str(debate_number)+'/debate_'+str(debate_number)+'_'+str(file_number)+'.json', 'w')
					start_time = time.time()