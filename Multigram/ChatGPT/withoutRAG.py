from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

def find_multigram_root(word):
    n = len(word)
    for i in range(1, n):
        if n % i == 0:
            substr_len = n // i
            substrs = [word[j:j+substr_len] for j in range(0, n, substr_len)]
            root = substrs[0]
            if all(is_anagram(root, substr) for substr in substrs):
                return root
    return -1

# Taking input
word = input().strip()

# Finding multigram root
result = find_multigram_root(word)

# Printing result
print(result)
