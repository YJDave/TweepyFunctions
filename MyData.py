def write_into_file_User(user_name, user_info, flag=True):

	myfile = open('tweetdata.txt', 'a')

	myfile.write("\n--> "+str(user_name)+"\n")
	myfile.write(str("Name : "+str(user_info.name)+"\n"))	
	myfile.write(str("User Id : "+user_info.id_str+"\n"))
	myfile.write(str("User Name : "+str(user_info.screen_name)+"\n"))
	myfile.close()
	
	if flag:
		
		myfile.write(str("Created at : +"+str(user_info.created_at)+"\n"))
		myfile.write(str("No of Followers : "+str(user_info.followers_count)+"\n"))
		myfile.write(str("No of Following : "+str(user_info.friends_count)+"\n"))
		myfile.write(str("Description : "+str(user_info.description)+"\n"))
		myfile.close()
		

def write_into_file_func(func):

	myfile = open('tweetdata.txt', 'a')

	myfile.write("\n\n\n")
	myfile.write("##################-----"+func+"------------##################")
	myfile.write("\n\n\n")
	myfile.close()



def write_into_file_DirectMessage(direct_message, flag=True):

	myfile = open('tweetdata.txt', 'a')

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
	myfile.close()


def write_into_file_Status(status):

	myfile = open('tweetdata.txt', 'a')
	myfile.write("\n--> Status ::")
	myfile.write("\nMessage ID : "+str(status.id))
	myfile.write("\nMessage : "+status.text)
	myfile.write("\nWritten By : "+status._json['user']['name'])
	myfile.write("\nWritter's Username : "+status._json['user']['screen_name'])
	myfile.write("\nWritter's ID : "+str(status._json['user']['id']))
	myfile.close()

def write_into_file_Friendhsip(friendship):

	myfile = open('tweetdata.txt', 'a')
	myfile.write("\n--> Friendhsip")
	myfile.write("\nUser1 Name : "+friendship[0].screen_name)
	myfile.write("\nUser1 ID : "+friendship[0].id_str)
	myfile.write("\nUser2 Name : "+friendship[1].screen_name)
	myfile.write("\nUser2 ID : "+friendship[1].id_str)
	myfile.write("\nIs "+friendship[0].screen_name+" following to "+friendship[1].screen_name+" "+str(friendship[1].followed_by))
	myfile.write("\nIs "+friendship[1].screen_name+" following to "+friendship[0].screen_name+" "+str(friendship[0].followed_by))
	myfile.close()

def get_tokens():

#Enter your tokesn here.......

	consumer_key = 'Q5mD59G1G5GsJ7aEGiLAlrHDh'
	consumer_secret = 'zAHkRVFeaXe19VWhh1QQc1wrrsFJ1YMiCyF5YRtfxmHHbQFmdo'

	access_token = '794909294168854528-Gx1rbjo7iCGIQ5tGslCPuyCbDEhmD9h'
	access_secret = 'jvtsr4l755InF67FIdrcOGPO1rez2xLWQ0OYkpzsoJtAW'

	return consumer_key, consumer_secret, access_token, access_secret