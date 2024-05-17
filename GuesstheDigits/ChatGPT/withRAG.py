import sys

def find_number(m, n, p, q):
    for i in range(10**(m-n), 10**(m-n+1)):
        num = int(str(i) + str(p))
        if num * q == int(str(i).zfill(m-n) + str(p)):
            return num
    return "IMPOSSIBLE"

if __name__ == "__main__":
    for line in sys.stdin:
        m, n, p, q = map(int, line.split())
        result = find_number(m, n, p, q)
        print(result)
