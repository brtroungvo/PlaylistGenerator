# importing
import os
import googleapiclient.discovery
from dotenv import load_dotenv
from chatgpt import songList

# Load YouTube apikey
load_dotenv(override=True)

# Creating YouTube Data api client
apikey = os.getenv("YOUTUBE_API_KEY")
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=apikey)


# Stores results for YouTubeSet Searches
youtubeIds = []

# Search for videos and store videoIds in youtubeIds
try:
    youtubeList = songList
    for x in youtubeList:
        try:
            searchResponse = youtube.search().list(
                q = x,
                type = 'video',
                part = 'id',
                maxResults = 1
            ).execute()
            templist = []
            for searchResult in searchResponse.get('items'):
                temp = searchResult['id']['videoId']
                templist += temp
                templist = "".join([s for s in templist])
            youtubeIds.append(templist)
        except Exception as e:
            print (f"An error occured: {e}")
except Exception as e:
    print(f"An error occured: {e}")