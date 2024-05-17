def find_occurrences(patterns, text):
    occurrences = []
    for pattern in patterns:
        indices = []
        start_index = 0
        while True:
            index = text.find(pattern, start_index)
            if index == -1:
                break
            indices.append(index + 1)
            start_index = index + 1
        occurrences.append(indices)
    return occurrences

def main():
    while True:
        try:
            num_patterns = int(input().strip())
            patterns = [input().strip() for _ in range(num_patterns)]
            text = input().strip()

            occurrences = find_occurrences(patterns, text)

            for pattern_occurrences in occurrences:
                print(" ".join(map(str, pattern_occurrences)))
            print()  # Print an empty line between test cases
        except Exception as e:
            break

if __name__ == "__main__":
    main()
