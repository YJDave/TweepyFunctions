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


try:

	myfile = open('tweetdata.txt', 'a')

###############---------favorites-------#####################
#Returns the favorite statuses for the authenticating user 
#or user specified by the ID parameter.
#return list of Status Object

#800405530401353728
	user = "yashashvi_dave"
	user_favorites = api.favorites(user)

	write_into_file_func("favorites")

	myfile.write("\nList of All Favorites of User "+user)

	for i in user_favorites:
		write_into_file_Status(i)


	print("Successfully implemented favorites")

###############---------create_favorite-------#####################
#Favorites the status specified in the ID parameter as the authenticating user.
#return Status Object

#code 139 you have already favorite the status
	status_id = "800405530401353728"

	status_of_favorite = api.create_favorite(status_id)

	write_into_file_func("create_favorite")
	myfile.write("\nGiven Message is add to Favorite of Authenticated User")
	write_into_file_Status(status_of_favorite)


	print("Successfully implemented create_favorite")


###############---------destroy_favorite-------#####################
#UnFavorites the status specified in the ID parameter as the authenticating user.
#return Status Object

	status_id = "860791905831006208"

	status_of_unfavorite = api.destroy_favorite(status_id)

	write_into_file_func("destroy_favorite")
	myfile.write("\nGiven Message is add to UnFavorite of Authenticated User")
	write_into_file_Status(status_of_unfavorite)	


	print("Successfully implemented destroy_favorite")


	myfile.close()
except Exception as e:

	print("Error Occured. "+ str(e) +  " Try Again. ")


