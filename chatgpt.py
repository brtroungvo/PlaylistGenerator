import os
from openai import *
from dotenv import load_dotenv

# Loads and overrides system variables with .env variables
load_dotenv(override=True)

# Gets user input for genre of songs
genre = input("What genre of music do you want in your playlist?\n")

# Prompt that goes into chat gpt
prompt = "List of 10 " + genre + " songs with the artist name. No note at the end."

client = OpenAI(api_key=os.getenv('CHATGPT_API_KEY'))

# DOES NOT USE PREVIOUS MESSAGES AS CONTEXT (NO CONVERSATION)
response = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {"role": "user", "content": prompt}
    ],
)
assistantResponse = response.choices[0].message.content
result = assistantResponse
print(f"ChatGPT:\n{result}")

print("\n----------------------------------------\n")

# Instantiate set of strings which will contain song and artist name
songList = result.split("\n")

# Loop to get rid of numbers
for x in range(len(songList)):
    songList[x] = songList[x].split('. ')[1]