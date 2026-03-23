import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

Groq()

client = Groq()
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Who is messi?"}],
    temperature=0.3,
    max_completion_tokens=128,
    top_p=0.85,
    stream=False,
    stop=["<end>"]
)

print(response.choices[0].message.content)