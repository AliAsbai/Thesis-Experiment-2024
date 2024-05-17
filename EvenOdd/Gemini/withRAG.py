#! /usr/bin/python3

MOD = 10**9 + 7


def f(x):
  iterations = 0
  while x != 1:
    iterations = (iterations + 1) % MOD  # Update modulo prime
    x = x // 2 if x % 2 == 0 else (x + 1) % MOD
  return iterations


def main():
  L, R = map(int, input().split())
  # No precomputation needed for single value range
  total_sum = f(L)
  # Handle single value case separately
  if L == R:
    print(total_sum)
    return
  # Calculate sum from L+1 to R (exclusive)
  for i in range(L + 1, R + 1):
    total_sum = (total_sum + f(i)) % MOD
  print(total_sum)


if __name__ == "__main__":
  main()
