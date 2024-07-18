from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI()

file = client.files.create(
  file=open("payload.jsonl", "rb"),
  purpose="fine-tune"
)

job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
)


print(job.id)