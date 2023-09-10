# importing
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import chatgpt

# Load YouTube apikey
load_dotenv(override=True)

# Creating YouTube Data api cleint
developerKey = os.getenv("YOUTUBE_API_KEY")
youtube = build('youtube', 'v3', developerKey)


# Stores results for YouTubeSet Searches
youtubeLinks = []

# Search Request

youtubeList = songList
for x in youtubeList:
    search_response = youtube.search().list(
        q = x,
        type = 'video',
        maxResults = 10
     ).execute()
    print ("--------------------")


# Adding Videos to Playlist

