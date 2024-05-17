import sys

def build_suffix_array(s):
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]

def find_occurrences(text, patterns):
    suffix_array = build_suffix_array(text)
    occurrences = []
    for pattern in patterns:
        pattern_occurrences = []
        pattern_len = len(pattern)
        for i in range(len(text)):
            suffix = text[suffix_array[i]:]
            if pattern == suffix[:pattern_len]:
                pattern_occurrences.append(suffix_array[i])
        occurrences.append(pattern_occurrences)
    return occurrences

def main():
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        patterns = [input().strip() for _ in range(n)]
        text = input().strip()
        occurrences = find_occurrences(text, patterns)
        for pattern_occurrences in occurrences:
            if pattern_occurrences:
                print(' '.join(map(str, pattern_occurrences)))
            else:
                print()

if __name__ == "__main__":
    main()
