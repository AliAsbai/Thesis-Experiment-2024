def above_average(grades):
  """
  Calculates the percentage of students with grades above the average.

  Args:
      grades: A list of integers representing student grades.

  Returns:
      A string with the percentage rounded to 3 decimal places, followed by "%".
  """
  average = sum(grades) / len(grades)
  above_count = sum(grade > average for grade in grades)
  return f"{above_count / len(grades) * 100:.3f}%"

def main():
  """
  Reads input, calculates percentages for each case, and prints the results.
  """
  cases = int(input())
  for _ in range(cases):
    num_students = int(input())
    grades = list(map(int, input().split()))  # Handles spaces and newlines
    print(above_average(grades))

if __name__ == "__main__":
  main()
