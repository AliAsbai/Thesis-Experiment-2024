def next_highest_price(price):
    digits, decimal = price[:-2], price[-2:]
    valid_digits = {'0', '1', '2', '5', '6', '8', '9'}

    # Convert the digits into a list for easier manipulation
    digits_list = list(digits)

    # Replace digits according to the rules
    for i in range(len(digits_list) - 1, -1, -1):
        if digits_list[i] == '6':
            digits_list[i] = '9'
            break
        elif digits_list[i] == '9':
            continue
        elif digits_list[i] == '2':
            digits_list[i] = '5'
            break
        elif digits_list[i] == '5':
            digits_list[i] = '2'
            break
        elif digits_list[i] in valid_digits:
            digits_list[i] = max(valid_digits - {'0', digits_list[i]})
            break

    # If no digit can be replaced, return "The price cannot be raised"
    else:
        return "The price cannot be raised"

    # Sort the remaining digits in non-increasing order
    digits_list.sort(reverse=True)

    # Concatenate the digits and decimal part to form the new price
    new_price = ''.join(digits_list) + decimal
    return new_price


# Read input until a line with only a dot is encountered
while True:
    price = input().strip()
    if price == '.':
        break
    else:
        result = next_highest_price(price)
        print(result)
