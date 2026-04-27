from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a short professional summary about a company that needs document automation."
)

print(response.output_text)

