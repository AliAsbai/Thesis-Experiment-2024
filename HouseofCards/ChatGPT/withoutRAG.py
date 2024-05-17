import math

def smallest_possible_height(h0):
    # Calculate the smallest triangular number greater than or equal to h0
    height = math.ceil((-1 + math.sqrt(1 + 8 * h0)) / 2)
    # Ensure that the height is divisible by 4
    while height % 4 != 0:
        height += 1
    return height

if __name__ == "__main__":
    h0 = int(input().strip())
    result = smallest_possible_height(h0)
    print(result)
