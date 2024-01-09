import re



a = open("answers.txt", "r", encoding = "utf-8")
q = open("questions.txt", "r", encoding = "utf-8")

ac = open(r"clean data\answers_clean.txt", "w", encoding= "utf-8")
qc = open(r"clean data\questions_clean.txt", "w", encoding= "utf-8")

title = open(r"clean data\title.txt", "w", encoding= "utf-8")

#open files

stor = ""

TitleBool = True

for line in a:
    if TitleBool == False: #if line is not a Title 
        if "------------------------------------------------count is " in line:
            stor = re.sub(r"SOLVED","",stor) #Removes the "solved" from the start of each answer
            stor = stor.lower() 
            stor = re.sub(r"[“”]", '"', stor) # standarizes quotes
            stor = re.sub(r"[‘’]", "'", stor) 
            stor = re.sub(r"[^\w\s.,?!';:]", '', stor) #removes nonstandard punctuation
            stor = re.sub(r"\s+", " ", stor).strip() #cleans up double spaces and strips
            ac.write(f"{stor}\n") #writes clean answers to file
            stor = ""
            TitleBool = True
        else:
            stor = stor + line
    else:
        temp = re.sub(r"SOLVED","",line) #same as before
        temp = temp.lower()
        temp = re.sub(r"[“”]", '"', temp)
        temp = re.sub(r"[‘’]", "'", temp)
        temp = re.sub(r"[^\w\s.,?!';:]", '', temp)
        temp = re.sub(r"\s+", " ", temp).strip()
        title.write(f"{temp}\n") #writes title to file
        TitleBool = False

a.close()
ac.close()

stor = ""

TitleBool = True

for line in q:
    if TitleBool == False: #same for questions
        if "------------------------------------------------count is " in line:
            stor = re.sub(r"SOLVED","",stor) 
            stor = stor.lower()
            stor = re.sub(r"[“”]", '"', stor)
            stor = re.sub(r"[‘’]", "'", stor)
            stor = re.sub(r"[^\w\s.,?!';:]", '', stor)
            stor = re.sub(r"\s+", " ", stor).strip()
            qc.write(f"{stor}\n")
            stor = ""
            TitleBool = True
        else:
            stor = stor + line
    else:
        TitleBool = False
q.close()
qc.close()