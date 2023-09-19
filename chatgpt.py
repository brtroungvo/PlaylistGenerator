import os
import openai
from dotenv import load_dotenv

# Loads and overrides system variables with .env variables
load_dotenv(override=True)

# Get API key from environment variable
openai.api_key = os.getenv("CHATGPT_API_KEY")

# Gets user input for genre of songs
genre = input("What genre of music do you want in your playlist?\n")

# Prompt that goes into chat gpt
prompt = "List of 10" + genre + "songs with the artist name. No note at the end."


# DOES NOT USE PREVIOUS MESSAGES AS CONTEXT (NO CONVERSATION)
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": prompt}
    ]
)
assistantResponse = response['choices'][0]['message']['content']
result = assistantResponse.strip(".")
print(f"ChatGPT:\n{result}")

print("\n----------------------------------------\n")

# Instantiate set of strings which will contain song and artist name
songList = result.split("\n")

# Loop to get rid of numbers
for x in range(len(songList)):
    songList[x] = songList[x].split('. ')[1]