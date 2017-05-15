# Siraj Challange
import tweepy
from textblob import TextBlob
import sys
# Step 1 - Authenticate
if len(sys.argv)>=2:
    topic =sys.argv[1]
else:
    topic="india"
print "Topic is "+topic
consumer_key= 'YOUR KEY'
consumer_secret= 'YOUR KEY'

access_token='YOUR KEY'
access_token_secret='YOUR KEY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#Step 3 - Retrieve Tweets
public_tweets = api.search(topic)
f=open("sentiments.txt","w")
for tweet in public_tweets:
    text=tweet.text
    # cleanedtext = ' '.join()
    
    l=[word for word in text.split() if len(word) > 0 and word!="RT" and word[0]!="@" and word[0]!="#" and "https" not in word]
   
    cleanedtext=' '.join(l)
    analysis=TextBlob(cleanedtext)
    cleanedtext=cleanedtext.encode("utf8")
    senti=analysis.sentiment.polarity
    if senti>0:
        f.write(cleanedtext+"-------------->"+"positive\n")
    else:
        f.write(cleanedtext+"-------------->"+"negative\n")