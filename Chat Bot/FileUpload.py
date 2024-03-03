from openai import OpenAI

client = OpenAI()

client.files.create(file=open(r"json data\revise1.jsonl", "rb"), purpose="fine-tune")

print("upload complete")
