class Memory:
    def __init__(self, n):
        self.bits = [0] * (n + 1)

    def flip_bit(self, k):
        self.bits[k] = 1 - self.bits[k]

    def count_ones(self, l, r):
        return sum(self.bits[l:r+1])

def main():
    n, k = map(int, input().split())
    memory = Memory(n)

    for _ in range(k):
        query = input().split()
        if query[0] == 'F':
            memory.flip_bit(int(query[1]))
        elif query[0] == 'C':
            l, r = map(int, query[1:])
            print(memory.count_ones(l, r))

if __name__ == "__main__":
    main()
