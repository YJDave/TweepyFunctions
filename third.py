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


def write_into_file_DirectMessage(direct_message):

	myfile.write("\nMessage : \n")
	
	
	myfile.write("\n--> Sender :")
	write_into_file_User(str((direct_message.sender).name), direct_message.sender, False)
	
	
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

###############---------direct_messages-------#####################
#Returns direct messages sent to the authenticating user.
#returns list of direct message object

	direct_messages_of_me = api.direct_messages()

	write_into_file_func("direct_messages")
	

	for i in direct_messages_of_me:
		write_into_file_DirectMessage(i)

	print("Successfully implemented direct_messages")



###############---------sent_direct_messages-------#####################
#Returns direct messages sent by the authenticating user.
#returns list of direct message object

	sent_direct_messages_of_me = api.sent_direct_messages()

	write_into_file_func("sent_direct_messages")


	for i in sent_direct_messages_of_me:
		write_into_file_DirectMessage(i)


	print("Successfully implemented sent_direct_messages")


###############---------send_direct_message-------#####################
#sent direct message to specific user from authenticating user


#@@@@@@@@@@@try user which is not friend
#@@@@@@@@@@@code:150 You can't send the message to users who are not following you

	user = "thehdrug"
	sent_direct_message_to = api.send_direct_message(user,text="Hello..")

	write_into_file_func("send_direct_message")

	
	myfile.write("Message Send to User.. Message Info : \n")
	write_into_file_DirectMessage(sent_direct_message_to)


	print("Successfully implemented send_direct_message")


###############---------destroy_direct_message-------#####################
#Destroy a direct message. Authenticating user must be the recipient of the direct message.


	# message_id = ''
	# destroy_direct_message_to = api.destroy_direct_message(message_id)

	# write_into_file_func("destroy_direct_message")

	
	# myfile.write("Message Sent to User.. Message Info : \n")
	# write_into_file_DirectMessage(destroy_direct_message_to)


	# print("Successfully implemented destroy_direct_message")




	myfile.close()
except Exception as e:

	print("Error Occured. "+ str(e) +  " Try Again. ")
