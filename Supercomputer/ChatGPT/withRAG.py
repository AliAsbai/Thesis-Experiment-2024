import sys

def flip_bit(memory, bit_count, i):
    memory[i] = 1 - memory[i]
    if memory[i] == 1:
        bit_count[i] += 1
    else:
        bit_count[i] -= 1

def count_bits(bit_count, l, r):
    if l == 0:
        return bit_count[r]
    else:
        return bit_count[r] - bit_count[l - 1]

def main():
    for line in sys.stdin:
        n, k = map(int, line.split())
        memory = [0] * n
        bit_count = [0] * n
        
        for _ in range(k):
            query = input().split()
            if query[0] == 'F':
                i = int(query[1]) - 1
                flip_bit(memory, bit_count, i)
            elif query[0] == 'C':
                l = int(query[1]) - 1
                r = int(query[2]) - 1
                print(count_bits(bit_count, l, r))

if __name__ == "__main__":
    main()
