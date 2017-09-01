from MyData import (

	write_into_file_func,
	write_into_file_DirectMessage,
	get_tokens,
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


#Enter specific message id here......
	message_id = ''
	destroy_direct_message_to = api.destroy_direct_message(message_id)

	write_into_file_func("destroy_direct_message")

	
	myfile.write("Message Sent to User.. Message Info : \n")
	write_into_file_DirectMessage(destroy_direct_message_to)


	print("Successfully implemented destroy_direct_message")

	myfile.exit()

except Exception as e:

	print("Error Occured. "+ str(e) +  " Try Again. ")
