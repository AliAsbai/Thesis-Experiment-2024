#! /usr/bin/python3

from collections import defaultdict


def solve():
    n, m = map(int, input().split())
    words = input().split()
    word_codes = {word: i for i, word in enumerate(set(words))}
    synonyms = defaultdict(list)
    for _ in range(m):
        a, b = input().split()
        synonyms[word_codes[a]].append(word_codes[b])
        synonyms[word_codes[b]].append(word_codes[a])

    min_lengths = [len(word) for word in words]

    def dfs(word_code, visited, current_length):
        if word_code in visited:
            return
        visited.add(word_code)
        for neighbor in synonyms[word_code]:
            if min_lengths[neighbor] <= current_length:
                continue  # Skip already processed or longer synonyms
            min_lengths[neighbor] = min(min_lengths[neighbor], current_length)
            dfs(neighbor, visited, current_length)

    for word_code in word_codes.values():
        dfs(word_code, set(), min_lengths[word_code])  # Use initial word length

    return sum(min_lengths)


result = solve()
print(result)


if __name__ == "__main__":
    solve()
