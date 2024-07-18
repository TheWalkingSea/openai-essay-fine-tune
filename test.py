from openai import OpenAI
from dotenv import load_dotenv
import os
import sys
import pyperclip

load_dotenv()
client = OpenAI()

model = os.environ.get('OPENAI_MODEL_NAME')
if not model:
    print(client.fine_tuning.jobs.list(limit=10))
    raise Exception("OPENAI_MODEL_NAME environmental variable not set")

prompt = ""
while True:
    inp = input("Enter prompt (! to exit): ")
    if inp == "!": break
    prompt += inp + "\n"

completion = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "user", "content": prompt},
  ]
)

print(completion.choices[0].message.content)
pyperclip.copy(completion.choices[0].message.content)