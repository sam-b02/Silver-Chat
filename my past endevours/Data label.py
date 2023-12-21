# File paths
data_file_path = r'C:\Users\samar\Visual Studio Projects\Data Interpretation\relevant_questions.txt'  # Update to your data file path
tech_file_path = 'tech_questions.txt'
non_tech_file_path = 'non_tech_questions.txt'
progress_file_path = 'progress.txt'

# Function to get the last processed line number
def get_last_processed_line_number():
    try:
        with open(progress_file_path, 'r') as progress_file:
            return int(progress_file.read().strip())
    except FileNotFoundError:
        return 0  # Start from the beginning if progress file doesn't exist

# Function to save the current progress
def save_progress(line_number):
    with open(progress_file_path, 'w') as progress_file:
        progress_file.write(str(line_number))

# Load your data
with open(data_file_path, 'r') as file:
    lines = file.readlines()

# Open output files
tech_file = open(tech_file_path, 'a')
non_tech_file = open(non_tech_file_path, 'a')

# Start from the last processed line
current_line_number = get_last_processed_line_number()

try:
    while current_line_number < len(lines):
        question = lines[current_line_number].strip()

        print(f"\nQuestion {current_line_number + 1}/{len(lines)}: {question}")
        label = input("Label (Tech/Non-Tech/Back/Save): ").lower()

        if label == 'y':
            tech_file.write(question + '\n')
            current_line_number += 1
        elif label == 'n':
            non_tech_file.write(question + '\n')
            current_line_number += 1
        elif label == 'back' and current_line_number > 0:
            current_line_number -= 1
        elif label == 'save':
            save_progress(current_line_number)
            print("Progress saved.")
        else:
            print("Invalid input. Please enter 'Tech', 'Non-Tech', 'Back', or 'Save'.")

finally:
    tech_file.close()
    non_tech_file.close()

print("Labeling complete.")
