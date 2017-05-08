# Kurt Davis
# kdavis23

import sys
import json
import pdb

class textFilter():

	def __init__(self, input_file, locations, keywords):
		self.input_file = input_file
		self.locations = locations
		self.keywords = keywords		

	def run(self):
		with open(self.input_file, 'r') as f:
			for json_line in f:		
				data = json.loads(json_line)
				printed = False
				try:
					place = None
					for key, value in dict.items(data['user']):
						if key == 'location':
							place = value
					
					if not place == None:
						for word in self.locations:
							if word in place:
								for keyword in self.keywords: 
									if not data['text'].encode('ascii', 'ignore').lower().find(keyword) == -1:
										if not printed:
											print json.dumps(data)
											printed = True
											break
							if printed:
								break	

				except Exception:
					#print 'Exception occurred'
					pass

input_file_name = "tweetsd3.json"
output_file_name = "results_d3_EP.txt"

# Open Data file to collect output
sys.stdout = open(output_file_name, 'w')

filter1 = textFilter(input_file_name, ["Erie, PA", "Erie USA"], ['donald', 'trump', 'clinton', 'election', 'potus', 'president', 'white house', 'whitehouse'])

filter1.run()
