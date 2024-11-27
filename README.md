# PlaylistGenerator
Creates an AI Generated YouTube playlist based on user inputted genre. \
This is a showcase only.

## Showcase


https://github.com/brtroungvo/PlaylistGenerator/assets/66912783/1d553ab5-d181-457b-a6b5-d101510a90ca



#### Breakdown
Program is run through YouTubePlaylist.py and creates a list of 10 songs based on the genre the user inputs. \
This is done by using the OpenAI API to integrate ChatGPT, and then asking it to generate a reponse based on the appropriate prompt. \
It prints the list into the terminal and then provides a link for signing into YouTube. \
This is needed in order to put the playlist into the user's account.\
After signing in, it will place the private playlist into the user's account.

## Issues/Notes
In order to use this program, 3 API keys are needed. Those being for OpenAI, your Google Cloud project, and the OAuth 2.0 token associated with the Google Cloud project.\
Additionally a json file containing the client information (various urls and ids) for OAuth 2.0 is required.
