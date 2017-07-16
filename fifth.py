def write_into_file_Status(status):

	myfile.write("\n--> Status ::")
	myfile.write("\nMessage ID : "+str(status.id))
	myfile.write("\nMessage : "+status.text)
	myfile.write("\nWritten By : "+status._json['user']['name'])
	myfile.write("\nWritter's Username : "+status._json['user']['screen_name'])
	myfile.write("\nWritter's ID : "+str(status._json['user']['id']))




def write_into_file_func(func):

	myfile.write("\n\n\n")
	myfile.write("##################-----"+func+"------------##################")
	myfile.write("\n\n\n")



from tweepy import (
	OAuthHandler,
	API
)

consumer_key = '461XyHMzRdFHY8ZxN8XArPkoG'
consumer_secret = 'CFMsYLcFOUCEvJ6f9wtAmGjSoivtU5Dqt2NHn8ZfdRKu3fhWh3'

access_token = '794909294168854528-Gx1rbjo7iCGIQ5tGslCPuyCbDEhmD9h'
access_secret = 'jvtsr4l755InF67FIdrcOGPO1rez2xLWQ0OYkpzsoJtAW'

callback_url = "http://google.com"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#tweeter.api take arguments like auth_handler, host, search_host,..
api = API(auth)

myfile = open('twetdata.csv', 'a')

try:

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


