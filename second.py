def write_into_file_User(user_name, user_info, flag):

	myfile.write("\n--> "+str(user_name)+"\n")
	myfile.write(str("Name : "+str(user_info.name)+"\n"))	
	myfile.write(str("User Id : "+user_info.id_str+"\n"))
	myfile.write(str("User Name : "+str(user_info.screen_name)+"\n"))
	
	if flag:
		
		myfile.write(str("Created at : +"+str(user_info.created_at)+"\n"))
		myfile.write(str("No of Followers : "+str(user_info.followers_count)+"\n"))
		myfile.write(str("No of Following : "+str(user_info.friends_count)+"\n"))
		myfile.write(str("Description : "+str(user_info.description)+"\n"))
		

def write_into_file_func(func):

	myfile.write("\n\n\n")
	myfile.write("##################-----"+func+"------------##################")
	myfile.write("\n\n\n")


def write_into_file_DirectMessage(direct_message, flag):

	myfile.write("\nMessage : \n")
	
	if flag:
		myfile.write("\n--> Sender :")
		write_into_file_User(str((direct_message.sender).name), direct_message.sender, False)
	
	if flag is False:
		myfile.write("\n--> Recipient : ")
		write_into_file_User(str(direct_message.recipient.name), direct_message.recipient, False)	
	
	myfile.write(str("\n--> Message Id : "+direct_message.id_str+"\n"))
	myfile.write(str("Time : "+str(direct_message.created_at)+"\n"))
	myfile.write(str("Message : +"+direct_message.text+"\n"))
	


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

