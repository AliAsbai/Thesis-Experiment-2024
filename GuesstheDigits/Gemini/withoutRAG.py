from decimal import Decimal  # Import for handling large numbers

def find_number(m, n, p, q):
  """
  Finds the smallest m-digit number satisfying the given conditions.

  Args:
      m: The number of digits in the original number.
      n: The number of digits to cross out initially.
      p: The number to append after crossing out digits.
      q: The multiplier to get the original number.

  Returns:
      The smallest m-digit number satisfying the conditions, or "IMPOSSIBLE" if none exists.
  """
  # Check if valid input (m >= n and all parameters are positive)
  if m < n or not all(x > 0 for x in (m, n, p, q)):
    return "IMPOSSIBLE"

  # Handle cases where p is a multiple of q (no divisibility check needed)
  if p % q == 0:
    number = Decimal(q) * 10**(m - n - 1) + p
    # Add leading zeros for remaining digits
    for _ in range(n - 1):
      number *= 10
    return str(int(number))  # Convert Decimal to integer

  # Calculate the base number (remaining digits after crossing out)
  base_num = Decimal(q) * 10**(m - n - 1)

  # Get the greatest common divisor (GCD) of q and p (for efficiency)
  gcd = get_gcd(q, p)

  # Check if base number is divisible by GCD (combined divisibility check)
  if base_num % gcd != 0:
    return "IMPOSSIBLE"

  # Construct the number by adding remaining digits of p
  number = base_num + p

  # Check if number is divisible by q (consider divisibility by GCD)
  if number % gcd != 0:
    return "IMPOSSIBLE"

  # Check for integer overflow (if number is very large)
  if number > 10**m - 1:
    return "IMPOSSIBLE"

  # Add leading zeros for remaining digits
  for _ in range(n - 1):
    number *= 10

  return str(int(number))  # Convert Decimal to integer

# Function to calculate greatest common divisor (Euclidean Algorithm)
def get_gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

# Read input from a single line
m, n, p, q = map(int, input().split())

# Find the number or print "IMPOSSIBLE"
result = find_number(m, n, p, q)
print(result)
