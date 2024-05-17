import sys

def find_word(length, weight):
    if weight < length or weight > 26 * length:
        return "impossible"
    
    remaining_weight = weight - length
    base_letter_weight = min(remaining_weight, 25)
    word = ['a'] * length
    
    for i in range(length):
        if remaining_weight >= base_letter_weight:
            word[i] = chr(ord('a') + base_letter_weight)
            remaining_weight -= base_letter_weight
        else:
            word[i] = chr(ord('a') + remaining_weight)
            remaining_weight = 0
    
    return ''.join(word)

if __name__ == "__main__":
    for line in sys.stdin:
        length, weight = map(int, line.split())
        result = find_word(length, weight)
        print(result)
