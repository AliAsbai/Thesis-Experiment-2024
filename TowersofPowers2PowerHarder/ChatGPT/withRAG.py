import sys

def parse_integer(integer_str):
    powers = list(map(int, integer_str.split('^')))
    return tuple(powers)

def format_integer(integer_tuple):
    return '^'.join(map(str, integer_tuple))

def main():
    case_number = 1
    for line in sys.stdin:
        n = int(line.strip())
        integers = []
        for _ in range(n):
            integer_str = sys.stdin.readline().strip()
            integer_tuple = parse_integer(integer_str)
            integers.append((integer_tuple, integer_str))
        
        # Sort integers while preserving original order
        integers.sort()
        
        # Output sorted integers
        print(f"Case {case_number}:")
        for _, integer_str in integers:
            print(integer_str)
        
        case_number += 1

if __name__ == "__main__":
    main()
