# Basic bot created using the Bot Framework provided by Molly White
# Bot code: https://github.com/molly/twitterbot_framework
# Website: http://blog.mollywhite.net

from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

