#Takes original huge dataset and splits it into sections of 5000 tweets. Then writes each section to a new file.
#Now the smaller files can be read indivisually and less memory is required for computation.

import json
import sys
import pdb
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import time

json_file = 'C:\Users\Eoghan\Desktop\PresidentialDebate2(DonaldTrump-HillaryClinton)Oct_19_2016.json'

if __name__ == '__main__':

	sliding_window = 5000
	max_line = 500000
	current_line = 0
	finish_line = current_line + sliding_window

	file_number = 1
	debate_number = 2

	iterator = 0

	election_file = open('data/debate_'+str(debate_number)+'/debate_'+str(debate_number)+'_'+str(file_number)+'.json', 'w')
	start_time = time.time()

	with open(json_file) as tweet_file:
		for iterator, tweet_by_line in enumerate(tweet_file):
			if iterator >= current_line and iterator <= finish_line:
				tweet = json.loads(tweet_by_line)
				tweet_text = tweet['text'].encode('ascii','ignore')
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