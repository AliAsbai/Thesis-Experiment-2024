import sys

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def findMinDistance(m, x, y):
    z = 0
    lcm = m[0]
    for i in range(1, 3):
        gcd, xDiff, _ = gcdExtended(lcm, m[i])
        lcm *= m[i] // gcd
        zDiff = (x[i] - x[0] + m[i]) % m[i]
        _, inverse, _ = gcdExtended(lcm // m[i], m[i])
        z += zDiff * (lcm // m[i]) * inverse
    minDistance = x[0] + z
    for i in range(lcm):
        valid = True
        for j in range(3):
            if abs(x[j] - minDistance) % m[j] > y[j]:
                valid = False
                break
        if valid:
            return minDistance
        minDistance += lcm
    return -1

def main():
    m = list(map(int, input().split()))
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    result = findMinDistance(m, x, y)
    print(result)

if __name__ == "__main__":
    main()
