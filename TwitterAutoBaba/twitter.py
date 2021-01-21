import tweepy
import time
auth = tweepy.OAuthHandler('ypjbVYGsEaCnAY33MSjVunBct','XRQkdPL6Jc8Cr1JrfWsP1lNtcQlUTDbtgV1n5rG22oz1di0aYA') //Old tokens
auth.set_access_token('3457319180-B67mrUicV3Bto1uc8lvOEYChHbkv0S5hORMSAj2','9NwG2aYWAJN9JAWTZ7ToZYoMM0BDignzuFkoUi7UtkH7y')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

search = 'Football' //Football can be replaced with the keyboard we want to look for in a tweet 
nrTweets = 200 //Limit to look for tweets 
for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(5) //A pause period provided in between liking of tweets
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
    break



