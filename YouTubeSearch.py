# importing
import os
from googleapiclient.discovery import build

# Creating YouTube Data api cleint

youtube = build('youtube', 'v3', devlopeKey=api.key)


# Stores results for YouTubeSet Searches
youtubeLinks = set()

# Search Request
youtubeSet = {"song1", "song2", "song3"} #placeholder
for x in youtubeSet:
    search_question = x
    search



search_reponse = youtube.search()

# Adding Videos to Playlist

