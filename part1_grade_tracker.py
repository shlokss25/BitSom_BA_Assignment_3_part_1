# given raw data
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# processing each student one by one
for student in raw_students:

    # cleaning the name i.e remove extra spaces and fixing upper and lower case
    name_clean = student["name"].strip().title()

    # converting roll numbers to integer
    roll = int(student["roll"])

    # converting marks string into list
    marks_list = student["marks_str"].split(",")
    marks = []

    for m in marks_list:
        marks.append(int(m.strip()))   # removing space and converting to int

    # check if name is valid (only alphabets in each word)
    valid = True
    for word in name_clean.split():
        if not word.isalpha():
            valid = False
            break   # added

    if valid:
        print("\n✓ Valid name") 
    else:
        print("\n✗ Invalid name")

    print("=" * 32)
    print(f"Student : {name_clean}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)

    if roll == 103:
        special_name = name_clean

print("\nSpecial Student (Roll 103):")
print(special_name.upper())
print(special_name.lower())  

# task 2 : Marks and Grades Analysis 

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print("\n--- Subject Performance ---")

# printing subject + grade
for i in range(len(subjects)):
    m = marks[i]

    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subjects[i]} : {m} -> {grade}")

# total and average
total = sum(marks)
avg = round(total / len(marks), 2)

print("\nTotal Marks:", total)
print("Average Marks:", avg)

# highest and lowest
max_marks = max(marks)
min_marks = min(marks)

max_sub = subjects[marks.index(max_marks)]
min_sub = subjects[marks.index(min_marks)]

print("Highest:", max_sub, "-", max_marks)
print("Lowest:", min_sub, "-", min_marks)



# While loop for new subjects


print("\n--- Add New Subjects ---")

new_count = 0

while True:
    subject_name = input("Enter subject name (or type 'done'): ")

    if subject_name.lower() == "done":
        break

    mark_input = input("Enter marks (0-100): ")

    # check numeric
    if not mark_input.isdigit():
        print("Please enter valid numeric marks.")
        continue

    mark_val = int(mark_input)

    # check range
    if mark_val < 0 or mark_val > 100:
        print("Marks should be between 0 and 100.")
        continue

    # add to lists
    subjects.append(subject_name)
    marks.append(mark_val)
    new_count += 1

# final output
print("\nNew subjects added:", new_count)

new_avg = round(sum(marks) / len(marks), 2)
print("Updated Average:", new_avg)


# Task 3: Class Performance Summary


class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\nClass Report Card")
print("Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0

topper_name = ""
topper_avg = 0

total_avg_sum = 0

# looping through class data
for name, marks in class_data:

    # calculating average
    avg = round(sum(marks) / len(marks), 2)

    # deciding pass or fail
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    # printing row
    print(f"{name:<18} | {avg:<7} | {status}")

    # checking topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    # adding to class total
    total_avg_sum += avg

# final summary
print("\nSummary:")
print("Passed Students:", pass_count)
print("Failed Students:", fail_count)

print("Class Topper:", topper_name, "-", topper_avg)

class_avg = round(total_avg_sum / len(class_data), 2)
print("Class Average:", class_avg)


# Task 4: String Manipulation


essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# 1. remove leading and trailing spaces
clean_essay = essay.strip()
print("\n1. Clean Essay:")
print(clean_essay)

# 2. convert to title case
title_case = clean_essay.title()
print("\n2. Title Case:")
print(title_case)

# 3. count occurrences of "python"
count_python = clean_essay.count("python")
print("\n3. Count of 'python':", count_python)

# 4. replace "python" with "Python 🐍"
replaced_text = clean_essay.replace("python", "Python 🐍")
print("\n4. Replaced Text:")
print(replaced_text)

# 5. split into sentences
sentences = clean_essay.split(". ")
print("\n5. Sentence List:")
print(sentences)

# 6. print numbered sentences
print("\n6. Numbered Sentences:")
for i in range(len(sentences)):
    sentence = sentences[i]

    # ensure sentence ends with "."
    if not sentence.endswith("."):
        sentence += "."

    print(f"{i+1}. {sentence}")