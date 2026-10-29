
student_scores = [88, 64, 91, 73, 59, 84]

passing_count = 0

for score in student_scores:
    if score >= 70:
        print(f"Score: {score} - Passing")
        passing_count += 1
    else:
        print(f"Score: {score} - Failing")

print(f"\nTotal passing scores: {passing_count}")
