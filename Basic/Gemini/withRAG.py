#! /usr/bin/python3

import re

def is_valid_constant(constant):
    """
    Checks if the given string is a valid Ada integer constant.

    Args:
        constant: The string representing the constant.

    Returns:
        "yes" if the constant is valid, "no" otherwise.
    """

    match = re.match(r"^([0-9]+|(?P<base>[2-9A-F]+)#(?P<digits>[0-9A-F]+))$", constant)
    if not match:
        return "no"

    base = int(match.group("base")) if match.group("base") else 10
    digits = match.group("digits")

    # Check for invalid characters or characters exceeding base
    if not all(char in f"0{base-1}" for char in digits):
        return "no"

    # Check for unnecessary trailing characters
    if match.group(2):  # Check if base was specified
        if not match.group(3):  # Check if digits are empty
            return "no"  # Unnecessary trailing #

    return "yes"

# Read input from standard input (STDIN)
for line in sys.stdin:
    constant = line.strip()
    # Call the function to check validity and print the result
    print(is_valid_constant(constant))
