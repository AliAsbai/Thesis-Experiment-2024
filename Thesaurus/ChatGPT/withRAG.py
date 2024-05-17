import sys

def find_shortest_synonym(word, synonyms):
    shortest = word
    if word in synonyms:
        for synonym in synonyms[word]:
            if len(synonym) < len(shortest):
                shortest = synonym
    return shortest

def main():
    synonyms = {}
    n, m = map(int, input().split())
    essay = input().split()
    for _ in range(m):
        a, b = input().split()
        synonyms.setdefault(a, []).append(b)
        synonyms.setdefault(b, []).append(a)

    total_length = sum(len(find_shortest_synonym(word, synonyms)) for word in essay)
    print(total_length)

if __name__ == "__main__":
    main()
