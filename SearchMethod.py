from MyData import (

	write_into_file_func,
	get_tokens,
	write_into_file_Status,
	write_into_file_User,

	)


from tweepy import (
	OAuthHandler,
	API,
	Cursor

)

consumer_key, consumer_secret, access_token, access_secret = get_tokens()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#tweeter.api take arguments like auth_handler, host, search_host,..
api = API(auth)

try:

	myfile = open('tweetdata.txt', 'a')
	
###############---------search(by Query)-------#####################
#Returns tweets that match a specified query.
#returns list of SearchResult object
	

	query = "michael jackson"

	search_result_general = api.search(q=query, lang="", geocode="")
	
	write_into_file_func("search(by query general)")



	for i in search_result_general:
		write_into_file_Status(i)


	print("Successfully implemented search by query(general)")

###############---------search(by Query Language)-------#####################
#Returns tweets that match a specified query, lang="resultant language", local="query language"
#rpp = "maximum return tweet per page into 100"
#returns list of SearchResult object


#@@@@@@@@@@@@@@@@@@@@@@@@
#how to pass more than one lang to search method in tweepy

	query = "ગુજરાતી"

	search_result_lang = api.search(q=query, lang="Gujarati", local="Gujarati", rpp=50)

	write_into_file_func("search(by query lang)")

	for i in search_result_lang:
		write_into_file_Status(i)


	print("Successfully implemented search by query(lang)")


###############---------search(by Location)-------#####################
#Returns tweets by users located within a given radius of the given latitude/longitude.
#parameter value is specified by “latitide,longitude,radius”

	latitude = '21.755264'
	longitude = '72.146380'
	radius = '20km'

	search_result_location = api.search(q="",geocode=latitude+","+longitude+","+radius)
	search_result_location_2 = api.search(geocode=latitude+","+longitude+","+radius)

	
	write_into_file_func("search(by location) with query = ''")

	
	#https://twitter.com/narendramodi/status/891865991503806464
	#https://twitter.com/Devchan39963044
	#myfile.write(str(search_result_location[0]))

	for i in search_result_location:
		write_into_file_Status(i)

	write_into_file_func("search(by location) without query")
	for i in search_result_location_2:
		write_into_file_Status(i)



	print("Successfully implemented search by location")


#########################search_users##############################
# Run a search for users similar to Find People button on Twitter.com; 
# the same results returned by people search on 
# Twitter.com will be returned by using this API (about being listed in the People Search). 
# It is only possible to retrieve the first 1000 matches from this API.

#returns list of users

	searchQuery = "modi"

	possible_users = api.search_users(q=searchQuery)

	write_into_file_func("search_users")

	for i in possible_users:
		write_into_file_User(searchQuery,i,False)


	print("Successfully implemented search_users")

##########################saved_searches##############################
#return SavedSearch object
#automatic returns authenticated user saved search

	saveSearch = api.saved_searches()

	write_into_file_func("saved_searches")

	for i in saveSearch:
		myfile.write(str(i))
		myfile.write("\n\n")


# 	print("Successfully implemented saved_searches")

# ##########################get_saved_searches##############################
# #return SavedSearch object
# # Retrieve the data for a saved search owned by 
# # the authenticating user specified by the given id.

	ResultObjects = []
   
	queryKeyword = 'michael jackson'
	language = ''
	location = None

	write_into_file_func("400 error")

	for StatusObject in Cursor(api.search, q=queryKeyword, lang=language, geocode=location).items(10):

		ResultObjects.append(StatusObject)
		write_into_file_Status(StatusObject)    

	saveDetail = api.get_saved_search('898151880357855233')

	write_into_file_func("get_saved_searches")

	myfile.write(str(saveDetail))

	print("Successfully implemented get_saved_search")



	myfile.close()
except Exception as e:

	print("Error Occured. "+ str(e) +  " Try Again. ")

