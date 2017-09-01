from MyData import (

	write_into_file_func,
	get_tokens,
	write_into_file_Status,
	write_into_file_DirectMessage,
	write_into_file_User,

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

##################------get_user------------##################
#returns all info of specific user
#returns User object

	user = "makeinindia"
	user_info = api.get_user(user)

	write_into_file_func("get_user")
	write_into_file_User(user, user_info, True)
	
	print("Successfully implemented get_user")


##################------me------------##################

#returns all info about authenticated user
#returns User object


#for json data:
#	myfile.write("##########Json##########\n")
#	myfile.write(str(my_info._json))

	my_info = api.me()

	write_into_file_func("me")
	write_into_file_User("Authenticated User", my_info, True)
	
	print("Successfully implemented me")


##################-----------followers------------##################

#returns followers of specific user in order they are added 100 at a time
#if not specified then returns followers of authenticated user
#list of User

	user = "thehdrug"

	write_into_file_func("followers")
	
	list_of_followers = api.followers(id=user)	


#using cursor

	#for i in range(0, 1):
	#	list_of_followers.append(api.followers(id=user, cursor=i))
		
	#myfile.write("\n\n******************\n\n")	
	#myfile.write(list_of_followers)

	list_of_my_followers = api.followers()

	myfile.write("\n##############Followers of Authenticated User##################\n")

	for i in list_of_my_followers:
		write_into_file_User(str(i.name), user_info, False)
		
	myfile.write("\n##################Followers of "+user+"########################\n")


	for i in list_of_followers:
		write_into_file_User(str(i.name), user_info, False)
	
	print("Successfully implemented followers")



##############------------search_users-----------###################
#returns list of all search result
#retrieve first 1000 matches

	user = "yashashvi"

	search_user = api.search_users(user)

	write_into_file_func("search_user")

	for i in search_user:
		write_into_file_User(str(i.name), i, False)
	
	print("Successfully implemented search_user")

	myfile.close()
except Exception as e:

	print("Error Occured. "+ str(e) +  " Try Again. ")

