# importing
import os
import googleapiclient.discovery
from dotenv import load_dotenv
#from chatgpt import songList

# Load YouTube apikey
load_dotenv(override=True)

# Creating YouTube Data api cleint
apikey = os.getenv("YOUTUBE_API_KEY")
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=apikey)


# Stores results for YouTubeSet Searches
youtubeLinks = []

# Search Request

'''
youtubeList = songList
for x in youtubeList:
    try:
        search_response = youtube.search().list(
            q = x,
            type = 'video',
            part = 'snippet',
            maxResults = 10
        ).execute()
        print ("\n----------------------------------------\n")
    except Exception as e:
        print (f"An error occured: {e}")
'''

search_query = "mariah carrey"

try:
    print ("\n----------------------------------------\n")
    search_response = youtube.search().list(
        q = search_query,
        type = 'video',
        part = 'snippet',
        maxResults = 3
    ).execute()
    print (search_response)
    print ("\n----------------------------------------\n")
except Exception as e:
    print (f"An error occured: {e}")

# Adding Videos to Playlist

