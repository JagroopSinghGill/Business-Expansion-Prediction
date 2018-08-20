#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "2269054406-xUCcCovCyIb8eeHAkZtz2eBokLSR7DploKhhFIY"
access_token_secret = "ao6uLZmcquPY4Yqx7hXbtRHdcisXBsCtTt52yXRSEaMiu"
consumer_key = "IoNRdUlZUUS68Zxl3WqE10FhW"
consumer_secret = "dbadr2QuRCEDxtk1pSy8Df1QJ7fnNrTFivbdkOR1G6p2DuI6na"

#access_token = "1511039792-eHEksdDglZWQ7r6ZvwZyxs0AL7oG1x2LdMYv0IJ"
#access_token_secret = "6shQMRMA6xSWLh4V41wN7y30ArLtwMejadxRNsaq4qsrZ"
#consumer_key = "OrQtLv2NhBQYYFhGYYdFqKLnU"
#consumer_secret = "ihAyBN7dM2Q0UBvXO3y8WVDJz3RUhwogMGSEfPYoXjaaTXBFV1"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)


    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
