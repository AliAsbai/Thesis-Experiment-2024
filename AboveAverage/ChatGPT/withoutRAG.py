def above_average_percentage(grades):
    avg_grade = sum(grades) / len(grades)
    above_avg_count = sum(1 for grade in grades if grade > avg_grade)
    return (above_avg_count / len(grades)) * 100

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        data = input().split()
        num_students = int(data[0])
        grades = list(map(int, data[1:]))
        percentage = above_average_percentage(grades)
        print("{:.3f}%".format(percentage))

if __name__ == "__main__":
    main()
