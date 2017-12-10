# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 00:39:06 2017

"""

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import twitter
import matplotlib.pyplot as plt 

 
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'bp6Hp2FFZkqHY63btFwUJW1Vn'
        consumer_secret = 'mJVrD1fEYCiZ2mxJNm3Syh2w7PoMcgEvdUi6qggZWDRh7odbRQ'
        access_token = '935294696892616710-U5nDorPr4QPYvxkHTkV7loozi23Gd9B'
        access_secret = 'xIlnMGYNBFZwSTGwXfOEoW7wvgeHhn9X9TqUdrYsqXcpm'
 
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 
    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
 
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)
 
            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
 
def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    print("Toyota tweet percentages")
    tweets = api.get_tweets(query = '#Toyota', count = 250)
 
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % ".format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets)))
    tp_tweets = len(ptweets)
    tn_tweets = len(ntweets)
    
    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
       print(tweet['text'])
 
    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
      
    print("\n")
    print("Honda tweet percentages")
    tweets = api.get_tweets(query = '#Honda', count = 250)
 
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % ".format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets)))
    hp_tweets = len(ptweets)
    hn_tweets = len(ntweets)
    
        # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
       print(tweet['text'])
 
    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
      
    print("\n")
    print("Acura tweet percentages")
    tweets = api.get_tweets(query = '#Acura', count = 250)
 
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % ".format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets)))
    ap_tweets = len(ptweets)
    an_tweets = len(ntweets)
    
        # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
       print(tweet['text'])
 
    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
      
    print("\n")
    print("BMW tweet percentages")
    tweets = api.get_tweets(query = '#BMW', count = 250)
 
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % ".format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets)))
    bp_tweets = len(ptweets)
    bn_tweets = len(ntweets)
    
        # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
       print(tweet['text'])
 
    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
    
    print("\n")
    print("Jeep tweet percentages")
    tweets = api.get_tweets(query = '#Jeep', count = 250)
 
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % ".format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets)))
    jp_tweets = len(ptweets)
    jn_tweets = len(ntweets)
    
    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
       print(tweet['text'])
 
    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])

    
    print("\n")
    print("Chevrolet tweet percentages")
    tweets = api.get_tweets(query = '#Chevrolet', count = 250)
 
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % ".format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets)))
    cp_tweets=len(ptweets)
    cn_tweets=len(ntweets)
    
    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
       print(tweet['text'])
 
    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
    
    #creating positive pie chart
    per_psum = tp_tweets+hp_tweets+ap_tweets+bp_tweets+jp_tweets+cp_tweets # the sum of all positive tweets for percentage
    p_labels = 'Toyota', 'Honda', 'Acura', 'BMW', 'Jeep', 'Chevrolet'
    p_sizes = [((tp_tweets/per_psum)*100), ((hp_tweets/per_psum)*100), ((ap_tweets/per_psum)*100),\
               ((bp_tweets/per_psum)*100),((jp_tweets/per_psum)*100), ((cp_tweets/per_psum)*100)] #configuring percents
    #creating negative pie chart
    per_nsum = tn_tweets+hn_tweets+an_tweets+bn_tweets+jn_tweets+cn_tweets # the sum of all negative tweets for percentage
    n_labels = 'Toyota', 'Honda', 'Acura', 'BMW', 'Jeep', 'Chevrolet'
    n_sizes = [((tn_tweets/per_nsum)*100), ((hn_tweets/per_nsum)*100), ((an_tweets/per_nsum)*100),\
               ((bn_tweets/per_nsum)*100),((jn_tweets/per_nsum)*100), ((cn_tweets/per_nsum)*100)] #configuring percents

    #configuring the settings of the positive pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(p_sizes, labels=p_labels, autopct='%1.1f%%', shadow=True, startangle=0)
    ax1.axis('equal')

    #the title of the figure1
    plt.suptitle('Percentage of Overall Positive Tweets')

    #configuring the settings of the positive pie chart
    fig2, ax2 = plt.subplots()
    ax2.pie(n_sizes, labels=n_labels, autopct='%1.1f%%', shadow=True, startangle=0)
    ax2.axis('equal')

    #the title of the figure2
    plt.suptitle('Percentage of Overall Negative Tweets')
    plt.show()

 
 
if __name__ == "__main__":
    # calling main function
    main()
