import re


a = open("answers.txt", "r", encoding = "utf-8")
q = open("questions.txt", "r", encoding = "utf-8")

ac = open(r"C:\Users\samar\Visual Studio Projects\clean data\answers_clean.txt", "w", encoding= "utf-8")
qc = open(r"C:\Users\samar\Visual Studio Projects\clean data\questions_clean.txt", "w", encoding= "utf-8")

title = open(r"C:\Users\samar\Visual Studio Projects\clean data\title.txt", "w", encoding= "utf-8")

stor = ""

TitleBool = True

for line in a:
    if TitleBool == False:
        if "------------------------------------------------count is " in line:
            stor = re.sub(r"SOLVED","",stor)
            stor = stor.lower()
            stor = re.sub(r"[“”]", '"', stor)
            stor = re.sub(r"[‘’]", "'", stor)
            stor = re.sub(r"[^\w\s.,?!';:]", '', stor)
            stor = re.sub(r"\s+", " ", stor).strip()
            ac.write(f"{stor}\n")
            stor = ""
            TitleBool = True
        else:
            stor = stor + line
    else:
        temp = re.sub(r"SOLVED","",line)
        temp = temp.lower()
        temp = re.sub(r"[“”]", '"', temp)
        temp = re.sub(r"[‘’]", "'", temp)
        temp = re.sub(r"[^\w\s.,?!';:]", '', temp)
        temp = re.sub(r"\s+", " ", temp).strip()
        title.write(f"{temp}\n")
        TitleBool = False

a.close()
ac.close()

stor = ""

TitleBool = True

for line in q:
    if TitleBool == False:
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