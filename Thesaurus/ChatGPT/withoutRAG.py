from collections import defaultdict

def find_shortest_synonym(word, synonyms):
    shortest = word
    if word in synonyms:
        for syn in synonyms[word]:
            if len(syn) < len(shortest):
                shortest = syn
    return shortest

def minimum_characters(N, essay, M, synonyms):
    synonym_map = defaultdict(list)
    for a, b in synonyms:
        synonym_map[a].append(b)
        synonym_map[b].append(a)
    
    shortest_length = 0
    for word in essay:
        shortest_word = find_shortest_synonym(word, synonym_map)
        shortest_length += len(shortest_word)
    
    return shortest_length

# Reading input
N, M = map(int, input().split())
essay = input().split()
synonyms = [input().split() for _ in range(M)]

# Computing the minimum number of characters
result = minimum_characters(N, essay, M, synonyms)
print(result)
