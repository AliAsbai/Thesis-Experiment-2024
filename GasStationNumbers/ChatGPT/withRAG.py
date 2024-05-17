import sys

def next_highest_price(price):
    digits = list(price)
    decimal_index = digits.index('.')
    
    # Reverse digits before the decimal point
    digits[:decimal_index] = reversed(digits[:decimal_index])
    
    # Mapping for digits that can be flipped
    flip_map = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '9': '6', '.': '.'}
    
    # Check if the price can be increased
    if all(digit == '9' for digit in digits):
        return "The price cannot be raised"
    
    # Find the rightmost digit that can be incremented
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != '9':
            if digits[i] == '5' and i != decimal_index - 1:
                digits[i] = '2'
                # Increment the digit on the left of '5'
                for j in range(i-1, -1, -1):
                    if digits[j] != '9':
                        digits[j] = str(int(digits[j]) + 1)
                        break
            else:
                digits[i] = str(int(digits[i]) + 1)
            break
    
    # Revert digits before the decimal point to their original order
    digits[:decimal_index] = reversed(digits[:decimal_index])
    
    # Flip digits if needed
    for i in range(len(digits)):
        digits[i] = flip_map[digits[i]]
    
    # Join digits and return the result
    return ''.join(digits)

for line in sys.stdin:
    price = line.strip()
    if price == '.':
        break
    print(next_highest_price(price))
