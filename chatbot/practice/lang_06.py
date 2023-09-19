import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

# Load API key from .env file
load_dotenv()
openai_api_key = os.getenv("openai_api_key")

# Initialize OpenAI instance
llm = OpenAI(model_name='text-davinci-003', temperature=0.9)

# Generate text based on the prompt
generated_text = llm('Recommend 5 metal songs from the 1980s.')

# Print the generated text
print(generated_text)


