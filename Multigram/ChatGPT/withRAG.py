import sys
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def find_root(word):
    if len(word) < 2:
        return -1

    n = len(word)
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisor = n // i
            substr = [word[j:j+divisor] for j in range(0, n, divisor)]
            if all(is_anagram(substr[0], sub) for sub in substr):
                return substr[0]
    
    return -1 if word != word[0]*len(word) else word[0]

if __name__ == "__main__":
    for line in sys.stdin:
        word = line.strip()
        result = find_root(word)
        print(result)
