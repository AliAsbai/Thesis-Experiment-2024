def parse_tower_of_powers(s):
    powers = list(map(int, s.split('^')))
    result = 1
    for power in reversed(powers):
        result = power ** result
    return result

def main():
    # Read the number of test cases
    num_cases = int(input())

    for case_number in range(1, num_cases + 1):
        # Read the integers for this test case
        num_integers = int(input())
        integers = []
        for _ in range(num_integers):
            integer = input()
            integers.append((integer, parse_tower_of_powers(integer)))

        # Sort the integers while keeping track of their original representation
        integers.sort(key=lambda x: (x[1], x[0]))

        # Output the sorted integers along with their original form and case number
        print(f"Case {case_number}:")
        for integer in integers:
            print(integer[0])

if __name__ == "__main__":
    main()
