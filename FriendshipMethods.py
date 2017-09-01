from MyData import (

	write_into_file_func,
	get_tokens,
	write_into_file_User,
	write_into_file_Friendhsip,

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

###############---------followers_ids-------#####################
#returns id of users which are followed by specific user
#return type is list of integer

	user = "thehdrug"

	all_followers_of_user = api.followers_ids(user)

	write_into_file_func("followers_ids")
	myfile.write("\nName & ID of Followers of "+user+" are : \n")

	for i in all_followers_of_user:
		myfile.write(((api.get_user(i)).name)+"\t\t"+str(i)+"\n")

	print("Successfully implemented followers_ids")




###############---------friends_ids-------#####################
#returns id of followers of specific user
#return type is list of integer

	user = "yashashvi_dave"

	all_followers_of_user = api.friends_ids(user)

	write_into_file_func("friends_ids")
	myfile.write("\nName & ID of Users followed by "+user+" are : \n")

	
	for i in all_followers_of_user:
		myfile.write(((api.get_user(i)).name)+"\t\t"+str(i)+"\n")

	print("Successfully implemented friends_ids")


###############---------show_friendship-------#####################
#Returns detailed information about the relationship between two users.
#returns tuple of two Friendship Object

	user1 = 'architad8'
	user2 = 'yashashvi_dave'

	friendship = api.show_friendship(source_id=user1,
									source_screen_name = user1, 
									target_id=user2,
									target_screen_name = user2)

	write_into_file_func("show_friendship")

	write_into_file_Friendhsip(friendship)

	print("Successfully implemented show_friendship")


###############---------create_friendship-------#####################
#Start following specific user
#return User object

	user = 'architad8'

	start_follow = api.create_friendship(user)

	write_into_file_func("create_friendship")

	myfile.write("\nAuthenticated User Start Following to This User :\n")
	
	write_into_file_User(user, start_follow, False)

	print("Successfully implemented create_friendship")


###############---------destroy_friendship-------#####################
#Stop following specific user
#return User object

	user = 'Medium'

	stop_follow = api.destroy_friendship(user)

	write_into_file_func("destroy_friendship")

	myfile.write("\nAuthenticated User Stop Following to This User :\n")
	
	write_into_file_User(user, stop_follow, False)

	print("Successfully implemented destroy_friendship")


# ###############---------exists_friendship-------#####################
# #Check if user1 is followint user2 or not
# #return True or False

	user2 = "Medium"
	user1 = "architad8"

	check_follow = api.exists_friendship(user1, user2)

	write_into_file_func("exists_friendship")

	myfile.write("\nIs "+user1+" is following to "+user2+"  user? : \n")

	myfile.write("\n"+check_follow+"\n")

	print("Successfully implemented exist_friendship")

	myfile.close()
except Exception as e:

	print("Error Occured. "+ str(e) +  " Try Again. ")
	

