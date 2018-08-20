# Import the necessary methods from tweepy library
import json
import geocoder
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from pymongo import MongoClient

# Variables that contains the user credentials to access Twitter API
access_token = "2269054406-xUCcCovCyIb8eeHAkZtz2eBokLSR7DploKhhFIY"
access_token_secret = "ao6uLZmcquPY4Yqx7hXbtRHdcisXBsCtTt52yXRSEaMiu"
consumer_key = "IoNRdUlZUUS68Zxl3WqE10FhW"
consumer_secret = "dbadr2QuRCEDxtk1pSy8Df1QJ7fnNrTFivbdkOR1G6p2DuI6na"

#access_token = "1511039792-eHEksdDglZWQ7r6ZvwZyxs0AL7oG1x2LdMYv0IJ"
#access_token_secret = "6shQMRMA6xSWLh4V41wN7y30ArLtwMejadxRNsaq4qsrZ"
#consumer_key = "OrQtLv2NhBQYYFhGYYdFqKLnU"
#consumer_secret = "ihAyBN7dM2Q0UBvXO3y8WVDJz3RUhwogMGSEfPYoXjaaTXBFV1"


# This is a basic listener that just prints received tweets to stdout.
client = MongoClient("localhost:27017")
client.drop_database('twitter')

class StdOutListener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)

        # print(all_data['user']['geo_enabled'])
        try:
            if all_data['user']['location'] is not None and all_data['lang'] == "en":
                g = geocoder.google(all_data['user']['location'])
                h = geocoder.google(g.latlng,method="reverse")
                if h.country_long is not None:
                    print(g.latlng)
                    print(h.country_long)
                    db = client.twitter
                    twt = all_data["text"]
                    db.twitterdata.insert_one({"tweet": twt, "country": h.country_long, "location": [g.lat, g.lng]})
                    print(all_data["user"]["location"])
                    print("----------------------")
                    #twt = re.sub(r'https?:\/\/.*[\r\n]*', '', all_data["text"], flags=re.MULTILINE)
            return (True)
        except Exception:
                pass

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    input_var = raw_input("Enter product/company name : ")
    print ("you entered " + input_var)
    stream.filter(track=[input_var])
    # This line filter Twitter Streams to capture data by the keywords: 'Enem','JustinBieberIsComingToBrazil','BuenViernes'
    #stream.filter(track=['amazon', 'AM4','Ryzen'])
