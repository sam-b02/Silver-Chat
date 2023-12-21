from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open(r"C:\Users\samar\Visual Studio Projects\json data\revise1.jsonl", "rb"),
  purpose="fine-tune"
)

print("upload complete")