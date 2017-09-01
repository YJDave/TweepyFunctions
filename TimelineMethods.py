from MyData import (

    get_tokens,

    )

from tweepy import (
    OAuthHandler,
    API
)

consumer_key, consumer_secret, access_token, access_secret = get_tokens()

callback_url = "http://google.com"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#tweeter.api take arguments like auth_handler, host, search_host,..
api = API(auth)

myfile = open('tweetdata.txt', 'a')

try:

##################------home_timeline------------###################
#authenticating user and that user’s friends.
#returns 20 most recent status, as list of "Status" object
#since_id, max_id, page  --other arguments

    public_tweets = api.home_timeline(count=50)

    myfile.write("\n\n\n")
    myfile.write("##################------home_timeline------------##################")
    myfile.write("\n\n\n")

    for tweet in public_tweets:
        myfile.write("\n-->  ")
        myfile.write(tweet.text)
        
    print("Successfully implemented home_timeline")

################-------user_timeline-------------#######################
#returns 20 most recent status of user, if not specified then author's status


    user = 'bhavnanaik15'

    status_of_user = api.user_timeline(id=user,count=50)

    myfile.write("\n\n\n")
    myfile.write("##################------user_timeline------------##################")
    myfile.write("\n\n\n")

    for s in status_of_user:
        myfile.write("\n-->  ")
        myfile.write(s.text)
        
    print("Successfully implemented user_timeline")

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

############---------retweets_of_me----------##########################
#returns 20 most recent tweets of the authenticated user that have been 
#retweeted by others. 
    

    most_retweet_tweet = api.retweets_of_me()
    

    myfile.write("\n\n\n")
    myfile.write("##################------retweets_of_me------------##################")
    myfile.write("\n\n\n")

    for i in most_retweet_tweet:
        myfile.write("\n-->  ")
        myfile.write(i.text)
        
    print("Successfully implemented retweets_of_me")




except Exception as e:

    print("Consumer Key do not match. Try Again. " + str(e))