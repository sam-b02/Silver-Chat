f = open(r"base data\data.txt", "r", encoding="utf-8")

question = open(r"base data\questions.txt", "w")
answer = open(r"base data\answers.txt", "w")


# adds handwritten prompts to file as well
count = 1
for line in f:
    if count % 2 == 0:
        answer.write(line)
    else:
        question.write(line)
    count = count + 1

print("done!")
