ac = open(r"clean data\answers_clean.txt", "r", encoding="utf-8")
qc = open(r"clean data\questions_clean.txt", "r", encoding="utf-8")

fa = open(r"final data\answers_final.txt", "w", encoding="utf-8")
fq = open(r"final data\questions_final.txt", "w", encoding="utf-8")

Title = open(r"clean data\title.txt", "r", encoding="utf-8")
fTitle = open(r"final data\titles_final.txt", "w", encoding="utf-8")

# opens files

line_number = 1
dead_line = []
for line in ac:
    if not line.strip().endswith(
        "click to expand..."
    ):  # there was a problem where sometimes the question was too long and it would overwrite the answer. These answers would end with "click to continue" and this program just removes them from the file
        if "click to expand..." in line:
            parts = line.split(
                "expand...", 1
            )  # sometimes there would be an issue where the question was long enough to interupt the answer and appear inside the answer, so this just removes anything before the "click to expand"
            line = parts[1]
        fa.write(f"{line.strip()}\n")
    else:
        dead_line.append(line_number)
    line_number += 1

line_number = 1

for line in qc:
    if line_number not in dead_line:
        fq.write(f"{line.strip()}\n")  # only writes the approved lines
    line_number += 1

line_number = 1

for line in Title:
    if line_number not in dead_line:
        fTitle.write(f"{line.strip()}\n")
    line_number += 1
