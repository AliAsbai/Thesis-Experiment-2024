import sys

def calculate_expected_remaining_contestants(n, m):
    if n == 0:
        return m
    c = [0]
    for i in range(min(n, m)):
        c.append(c[-1] + (n - i) / (i + 1))
        if c[-1] < -1e-7:
            break
    ans = 0
    for k in range(1, min(m, len(c)) + 1):
        ans += (m - k + 1) * (c[m - k] - c[m - k + 1]) / n
    return ans

if __name__ == "__main__":
    for line in sys.stdin:
        n, m = map(int, line.split())
        result = calculate_expected_remaining_contestants(n, m)
        print(result)
