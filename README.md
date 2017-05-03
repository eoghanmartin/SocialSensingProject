# A Presidential Campaign Analysis Tool

#### Requirements
* Python 2.7
	* TextBlob
	* Tweepy
* Tableau is used for visualizations.

## Features
1. Twitter Crawler
2. Influence Builder
3. Sentiment Analysis
4. Results Output

![alt tag](https://raw.githubusercontent.com/eoghanmartin/SocialSensingProject/master/images/pipeline.png)

## 1. Twitter Crawler

* Data is collected at city-level granularity for the following locations:
	* San Francisco, CA, New York, NY, Oklahoma City, OK, Erie, PA, and Chicago, IL
* Other datasets can also be filtered with the same method as Twitter streams- location, then keyword.

###Config Keys
Keys are listed in a config.txt file. The file is structured as follows:
```
CONSUMER_KEY
key
CONSUMER_SECRET
key
ACCESS_KEY
key
ACCESS_SECRET
key
```

## 2. Influence Builder

* An influence rating is built for each side using a follower to following ratio.
	* Influential users tend to have a following following count than followers count.
* This is incorporated into results so as to load balance the influence weight that each tweet carries.

## 3. Sentiment Analysis

* Textblob's Naive Bayes Model is used for sentiment analysis.
* Accounts for higher number of Trump tweets but with lower average sentiment polarity compared to Clinton.
	* Consider tweets as favorable for a candidate if polarity > .3
	* Consider tweets unfavorable if polarity < 0

## 4. Results Output

According to the RCP average, Trump favirability ratings are as follows:
* 42.8% Favorable
* 53.5% Unfavorable
![alt tag](https://raw.githubusercontent.com/eoghanmartin/SocialSensingProject/master/images/favorability_trump.png)

Results from debate data:
1. Debate 1:
	* 58.38% Clinton
	* 41.62% Trump
2. Debate 2:
	* 56.69% Clinton
	* 43.31% Trump
3. Debate 3:
	* 60% Clinton
	* 40% Trump

This can be compared with NBC polls:
![alt tag](https://raw.githubusercontent.com/eoghanmartin/SocialSensingProject/master/images/NBC_polls.png)

Debate 1 influence visualization:
![alt tag](https://raw.githubusercontent.com/eoghanmartin/SocialSensingProject/master/images/D1_influence.png)

Debate 2 influence visualization:
![alt tag](https://raw.githubusercontent.com/eoghanmartin/SocialSensingProject/master/images/D2_influence.png)