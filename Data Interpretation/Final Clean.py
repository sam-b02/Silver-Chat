ac = open(r"C:\Users\samar\Visual Studio Projects\clean data\answers_clean.txt", "r", encoding= "utf-8")
qc = open(r"C:\Users\samar\Visual Studio Projects\clean data\questions_clean.txt", "r", encoding= "utf-8")

fa = open(r"C:\Users\samar\Visual Studio Projects\final data\answers_final.txt", "w", encoding= "utf-8")
fq = open(r"C:\Users\samar\Visual Studio Projects\final data\questions_final.txt", "w", encoding= "utf-8")

Title = open(r"C:\Users\samar\Visual Studio Projects\clean data\title.txt", "r", encoding= "utf-8")
fTitle = open(r"C:\Users\samar\Visual Studio Projects\final data\titles_final.txt", "w", encoding= "utf-8")


line_number = 1
dead_line = []
for line in ac:
    if not line.strip().endswith("click to expand..."):
        if "click to expand..." in line:
            parts = line.split("expand...", 1)
            line = parts[1]
        fa.write(f"{line.strip()}\n")
    else:
        dead_line.append(line_number)
    line_number += 1

line_number = 1

for line in qc:
    if line_number not in dead_line:
        fq.write(f"{line.strip()}\n")
    line_number += 1

line_number = 1

for line in Title:
    if line_number not in dead_line:
        fTitle.write(f"{line.strip()}\n")
    line_number += 1


