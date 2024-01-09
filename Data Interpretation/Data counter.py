import json

q = open("questions.txt", "r", encoding = "utf-8")
a = open("answers.txt", "r", encoding = "utf-8")

count, count1 = 0, 0
for line in q:
    if "------------------------------------------------count is " in line:
        count = count + 1
        if count % 1000 == 0:
            print(count)

for line in a:
    if "------------------------------------------------count is " in line:
        count1 = count1 + 1
        if count1 % 1000 == 0:
            print(count1)

print(f"questions are {count} and answers are {count1}")

q.close()
a.close()


#17318 questions and answers
#counts number of questions and answers
