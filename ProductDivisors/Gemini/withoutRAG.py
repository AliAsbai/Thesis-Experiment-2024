MOD = 10**9 + 7

def count_divisors(primes):
  """
  Calculates the number of divisors of a product based on its prime factors.

  Args:
      primes: A list containing the prime factors of the product and their exponents.

  Returns:
      The number of divisors of the product modulo MOD.
  """
  count = 1
  for exponent in primes:
    try:
      count *= (exponent + 1)  # Check for potential integer overflow
    except OverflowError:
      print("Error: Integer overflow occurred. Consider using arbitrary-precision arithmetic for very large inputs.")
      return None
  return count % MOD

def is_prime(num):
  """
  Efficiently checks primality of a number.

  Args:
      num: The number to check for primality.

  Returns:
      True if the number is prime, False otherwise.
  """
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def main():
  """
  Reads input, calculates prime factors efficiently, and outputs the number of divisors.
  """
  try:
    n = int(input())
    numbers = list(map(int, input().split()))  # Ensure list type for integer operations
  except ValueError:
    print("Error: Invalid input format. Please provide integers separated by spaces.")
    return

  # Efficiently factorize using a combination of trial division and primality check
  primes = []
  for num in numbers:
    while num % 2 == 0:  # Handle divisibility by 2 efficiently
      primes.append(2)
      num //= 2
    i = 3  # Start checking from 3, skipping even numbers
    while i <= num:
      if is_prime(i):
        while num % i == 0:
          primes.append(i)
          num //= i
      i += 2  # Increment by 2 to check only odd numbers
    if num > 1 and is_prime(num):  # Handle remaining prime factor (if any)
      primes.append(num)

  # Count divisors based on prime factors
  divisors = count_divisors(primes)
  if divisors is not None:  # Check if error occurred in count_divisors
    print(divisors)

if __name__ == "__main__":
  main()
