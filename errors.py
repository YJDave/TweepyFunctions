#code 8
#####################-----get_status---------##################
#returns a single status 

	user = "vijaysharma007"

	user_status = api.get_status(id=user)

	myfile.write("\n\n\n")
	myfile.write("##################------get_status------------##############")
	myfile.write("\n\n\n")


	myfile.write("\n-->  ")
	myfile.write(user_status.text)
        
	print("Successfully implemented get_status")

#empty list
############---------statuses_lookup----------##########################
#returns up to 100 tweet per request 

#############working properly but didn't appending anything................................

    list_of_tweet = api.statuses_lookup(['makeinindia','Valireddy1','unngls'])

    myfile.write("\n\n\n")
    myfile.write("##################------statuses_lookups------------##################")
    myfile.write("\n\n\n")

    for i in list_of_tweet:
        myfile.write(str(i['id'])+str(i['text']))

    print("Successfully implemented statuses_lookup")


#code 88
##################-----------followers------------##################

#returns followers of specific user in order they are added 100 at a time
#if not specified then returns followers of authenticated user
#list of User

	user = "makeinindia"

	write_into_file_func("followers")
	
	list_of_followers = []
	
#using cursor

	for i in range(0, 1):
		list_of_followers.append(api.followers(id=user, cursor=i))
		
	myfile.write("\n\n******************\n\n")	
	myfile.write(list_of_followers)

	list_of_my_followers = api.followers()

	myfile.write("\nFollowers of Authenticated User\n")

	for i in list_of_my_followers:
		write_into_file_user(str(i.name), user_info)
		
	myfile.write("\nFollowers of "+user+"\n")


	for i in list_of_followers:
		write_into_file_user(str(i.name), user_info)
	
	

	print("Successfully implemented followers")

	myfile.close()


#??????????????????????????????SOLVED
#code 93
###############---------direct_messages-------#####################
#Returns direct messages sent to the authenticating user.
#returns list of direct message object

	direct_messages_of_me = api.direct_messages()

	write_into_file_func("direct_messages")

	for i in direct_messages_of_me:
		myfile.write("\n"+str(i)+"\n")

	print("Successfully implemented direct_messages")


#not returning anything 
#@@@@@@@@@@@@@@@@@@@@@@@@
#how to pass more than one lang to search method in tweepy

	query = "ગુજરાતી"

	search_result_lang = api.search(q=query, lang="Gujarati", local="Gujarati", rpp=50)

	write_into_file_func("search(by query lang)")

	for i in search_result_lang:
		write_into_file_Status(i)


	print("Successfully implemented search by query(lang)")


#?????????
#@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Note that you cannot use the near operator via the API to geocode arbitrary locations; 
#however you can use this geocode parameter to search near geocodes directly.