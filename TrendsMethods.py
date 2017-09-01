from MyData import (

	write_into_file_func,
	get_tokens,
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


try:

	myfile = open('tweetdata.txt', 'a')

###############------------trends_available-------#####################
#returns json object

	print("43")
	trends = api.trends_available()
	print("32432")

	write_into_file_func("trends_avaliabe")

	for i in trends:
		myfile.write(str(i)+"\n\n")

	print("Successfully implement treands_available")

	myfile.close()
except Exception as e:

	print("Error Occured. "+ str(e) +  " Try Again. ")
