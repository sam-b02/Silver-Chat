f = open(r"C:\Users\samar\Visual Studio Projects\base data\data.txt", "r", encoding= "utf-8")

question = open (r"C:\Users\samar\Visual Studio Projects\base data\questions.txt", "w")
answer = open (r"C:\Users\samar\Visual Studio Projects\base data\answers.txt", "w")

count = 1
for line in f:
    if count % 2 == 0:
        answer.write(line)
    else:
        question.write(line)
    count = count + 1

print("done!")