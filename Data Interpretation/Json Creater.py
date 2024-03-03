import json
import random


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()


def write_to_json(file_path, data):
    with open(file_path, "w") as file:
        for entry in data:
            json_string = json.dumps(entry)
            file.write(json_string + "\n")


# system message for silver

silver_description = """Silver is a friendly, helpful, factual chatbot that's focused on helping older adults with technological problems, both complex and trivial. 
Be patient, understanding, and respectful. 
Take time and guide them through any challenges they may have. 
Work through the challenge step by step with them to resolve it.
Break down the task into manageable steps, and then display the steps and actions they can take. Present these in the first message, instead of a follow up. 
Ask for details and specifics as needed. 
Assume a low level of pre-existing knowledge. 
Encourage and celebrate small successes. """

questions = read_file(r"base data\questions.txt")
answers = read_file(r"base data\answers.txt")


data = []
for question, answer in zip(questions, answers):
    print(answers)
    entry = {
        "messages": [
            {
                "role": "system",
                "content": silver_description,
            },  # writes messages in a way OpenAi's API can understand
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }
    data.append(entry)

random.shuffle(data)

write_to_json(r"json data\revise1.jsonl", data)
