def is_prime(num):
  """
  This function checks if a number is prime with optimization.
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

def count_primes(a, b):
  """
  This function counts the number of prime numbers between a and b (inclusive).
  """
  if a < 1 or b < a:
    raise ValueError("Invalid input: Lower limit (a) must be >= 1 and upper limit (b) must be >= a")
  count = 0
  # Only check for even numbers greater than 2
  if a <= 2 and b >= 2:
    count += 1  # Count 2 if it's in the range
  # Start loop from the next odd number after a (inclusive)
  start = 3 if a % 2 == 0 else a
  for num in range(start, b + 1, 2):
    if is_prime(num):
      count += 1
  return count

# Get input with error handling
while True:
  try:
    a = int(input("Enter lower limit (a): "))
    b = int(input("Enter upper limit (b): "))
    if a < 1 or b < a:
      raise ValueError
    break
  except ValueError:
    print("Invalid input. Please enter integers such that a >= 1 and b >= a.")

# Count primes
prime_count = count_primes(a, b)

# Print output
print(f"Number of primes between {a} and {b}: {prime_count}")
