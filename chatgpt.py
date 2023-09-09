import os
import openai
from dotenv import load_dotenv

# Overrides system variables with .env variables
load_dotenv(override=True)

# Load API key from environment variable
openai.api_key = os.getenv("CHATGPT_API_KEY")
