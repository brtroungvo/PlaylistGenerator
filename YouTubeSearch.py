# importing
import os
import googleapiclient.discovery
from dotenv import load_dotenv
from chatgpt import songList

# Load YouTube apikey
load_dotenv(override=True)

# Creating YouTube Data api cleint
apikey = os.getenv("YOUTUBE_API_KEY")
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=apikey)


# Stores results for YouTubeSet Searches
youtubeIds = []

youtubeList = songList
for x in youtubeList:
    try:
        search_response = youtube.search().list(
            q = x,
            type = 'video',
            part = 'id',
            maxResults = 1
        ).execute()
        templist = []
        for search_result in search_response.get('items'):
            temp = search_result['id']['videoId']
            templist += temp
            templist = "".join([s for s in templist])
        print (templist)
        youtubeIds.append(templist)
    except Exception as e:
        print (f"An error occured: {e}")

print (youtubeIds)
print ("\n----------------------------------------\n")


# Adding Videos to Playlist