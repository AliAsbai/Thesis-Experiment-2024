import sys

def above_average_percentage(grades):
    total_students = len(grades)
    average_grade = sum(grades) / total_students
    above_average_count = sum(1 for grade in grades if grade > average_grade)
    return (above_average_count / total_students) * 100

def main():
    for line in sys.stdin:
        test_cases = int(line)
        for _ in range(test_cases):
            data = input().split()
            n = int(data[0])
            grades = list(map(int, data[1:]))
            percentage = above_average_percentage(grades)
            print("{:.3f}%".format(percentage))

if __name__ == "__main__":
    main()
