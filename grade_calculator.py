student_grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [75, 80, 82],
    "David": [68, 72, 70],
    "Emily": [95, 91, 94]
}

# Dictionary to store each student's average
student_averages = {}

# Calculate the average grade for each student
for student_name, grade_list in student_grades.items():
    total_score = sum(grade_list)
    average_score = total_score / len(grade_list)
    student_averages[student_name] = average_score

# Dictionary to store each student's letter grade
student_letter_grades = {}

# Determine each student's letter grade
for student_name, average_score in student_averages.items():

    if average_score >= 90:
        letter_grade = "A"
    elif average_score >= 80:
        letter_grade = "B"
    elif average_score >= 70:
        letter_grade = "C"
    elif average_score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    student_letter_grades[student_name] = letter_grade

# Display each student's results
print("STUDENT GRADE REPORT")
print("--------------------")

for student_name in student_grades:
    print(
        f"{student_name}: "
        f"Average = {student_averages[student_name]:.2f}, "
        f"Letter Grade = {student_letter_grades[student_name]}"
    )

# Find the top-performing student using a loop
top_student = ""
highest_average = 0

for student_name, average_score in student_averages.items():
    if average_score > highest_average:
        highest_average = average_score
        top_student = student_name

# Calculate the overall class average
total_class_average = 0

for average_score in student_averages.values():
    total_class_average += average_score

class_average = total_class_average / len(student_averages)

# Count how many students passed with a C or better
passing_count = 0

for letter_grade in student_letter_grades.values():
    if letter_grade == "A" or letter_grade == "B" or letter_grade == "C":
        passing_count += 1

# Display class statistics
print("\nCLASS STATISTICS")
print("----------------")
print(f"Top Performer: {top_student}")
print(f"Top Average: {highest_average:.2f}")
print(f"Overall Class Average: {class_average:.2f}")
print(f"Number of Students Who Passed: {passing_count}")
