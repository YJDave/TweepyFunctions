from MyData import (

	write_into_file_func,
	get_tokens,
	write_into_file_Status,

	)


from tweepy import (
	OAuthHandler,
	API
)

consumer_key, consumer_secret, access_token, access_secret = get_tokens()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#tweeter.api take arguments like auth_handler, host, search_host,..
api = API(auth)

myfile = open('twetdata.csv', 'a')

try:

	myfile = open('tweetdata.txt', 'a')

##########################retweet given tweet##############################
#Retweets a tweet. Requires the id of the tweet you are retweeting.
#returns status object

	
	retweet_this_tweet_id = '860791905831006208'

	retweet_object = api.retweet(retweet_this_tweet_id)

	write_into_file_func("retweet")
	write_into_file_Status(retweet_object)

	print("Successfully implemented retweet function")

	myfile.close()
except Exception as e:

	print("Error Occured. "+ str(e) +  " Try Again. ")
	

