import os
import openai
from dotenv import load_dotenv

# Loads and overrides system variables with .env variables
load_dotenv(override=True)

# Get API key from environment variable
openai.api_key = os.getenv("CHATGPT_API_KEY")
