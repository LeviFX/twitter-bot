import tweepy
import time

consumer_key = '# api key'
consumer_secret = '# api key secret' 

key = '# acces token'
secret = '# acces token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

def reply():
    for tweet in tweepy.Cursor(api.search, q='#hashtag').items(1):
        print(str(tweet.id) + ' - ' + tweet.text)
        api.update_status("@" + tweet.user.screen_name + " Response text", tweet.id)


result = None
while result is None:
    try:
        reply()
        time.sleep(30)
        result = None
    except:
        pass

    if ValueError:
        time.sleep(30)
    else:
        break
