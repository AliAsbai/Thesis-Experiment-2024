def weight_of_words(l, w):
    if l > w or w > 26 * l:
        return "impossible"

    word = ['a'] * l
    remaining_weight = w - l
    i = l - 1

    while remaining_weight > 0:
        add_weight = min(remaining_weight, 25)
        word[i] = chr(ord(word[i]) + add_weight)
        remaining_weight -= add_weight
        i -= 1

    return ''.join(word)

# Reading input
l, w = map(int, input().split())

# Getting result and printing output
result = weight_of_words(l, w)
print(result)
