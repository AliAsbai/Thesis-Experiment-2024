from collections import defaultdict

def is_prime(n):
  """Checks if a number is prime."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def get_prime_factors(n):
  """
  Gets all prime factors of a number (optimized for efficiency).

  Args:
      n: The number to factorize.

  Returns:
      A set containing the prime factors of n.
  """
  factors = set()
  while n > 1:
    if is_prime(n):
      factors.add(n)
      break
    i = 2
    while n % i != 0:
      i += 1
    n //= i
    factors.add(i)
  return factors

def count_sets(a, b, p):
  """
  Counts the number of sets after merging based on prime factors.

  Args:
      a: Starting integer of the interval.
      b: Ending integer of the interval.
      p: Minimum prime factor for merging sets.

  Returns:
      The number of sets after merging.
  """
  parents = {i: i for i in range(a, b + 1)}

  def find(x):
    if parents[x] != x:
      parents[x] = find(parents[x])
    return parents[x]

  def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
      parents[root_y] = root_x

  for i in range(a, b + 1):
    prime_factors = get_prime_factors(i)  # Precompute prime factors for efficiency
    for factor in prime_factors:
      if factor >= p:
        union(i, i - 1)
        break  # Only need to merge once if a qualifying factor is found

  return len(set(find(x) for x in range(a, b + 1)))

def main():
  """Reads input and prints the number of sets for each test case."""
  num_cases = int(input())
  for case_num in range(1, num_cases + 1):
    a, b, p = map(int, input().split())
    num_sets = count_sets(a, b, p)
    print(f"Case #{case_num}:{num_sets}")

if __name__ == "__main__":
  main()
