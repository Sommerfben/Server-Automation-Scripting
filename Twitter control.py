import time
import os
from twython import TwythonStreamer, Twython
import urllib.request

# Search terms
TERMS = '#HASHTAG TO MONITOR'

# Twitter application authentication
APP_KEY = '*****************'
APP_SECRET = '***********************************'
OAUTH_TOKEN = '**************************************************'
OAUTH_TOKEN_SECRET = '*********************************************'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        tweet = data['text']
                        tweet = tweet.lower()
                        print(tweet)
                        if 'reboot' in tweet:
                                print('Rebooting')
                                os.system('sudo reboot')                                
                                time.sleep(0.5)
                        elif 'ip address' in tweet:
                                external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
                                print(external_ip)
                                twitter.update_status(status= str(external_ip))
                                time.sleep(0.5)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        pass
