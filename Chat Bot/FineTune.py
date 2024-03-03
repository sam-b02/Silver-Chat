from openai import OpenAI

client = OpenAI()

client.fine_tuning.jobs.create(
    training_file="file-8rRp4zKyj6cfhUiIEX88cqsz",
    model="ft:gpt-3.5-turbo-0613:personal::8X8N6Hks",
)

print("job started")
