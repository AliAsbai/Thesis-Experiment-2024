import sys

# Read the number of test cases
num_cases = int(sys.stdin.readline())

for _ in range(num_cases):
    # Read the number of students
    num_students = int(sys.stdin.readline())

    # Read the grades and calculate their sum
    grades = map(int, sys.stdin.readline().split())
    grade_sum = sum(grades)

    # Calculate the average grade using float division
    average = float(grade_sum) / num_students

    # Count the number of students above average
    above_average_count = 0
    for grade in grades:
        if grade > average:
            above_average_count += 1

    # Calculate the percentage of students above average
    percentage = (above_average_count / num_students) * 100

    # Format the output to 3 decimal places and print it
    print(f"{percentage:.3f}%")
