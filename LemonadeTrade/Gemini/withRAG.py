#! /usr/bin/python3

def max_blue_lemonade(n):
  """
  Calculates the maximum amount of blue lemonade obtainable.

  Args:
      n: The number of children in the class (excluding yourself).

  Returns:
      The maximum amount of blue lemonade obtainable (up to 10 litres).
  """
  # Dictionary to store the maximum amount of each lemonade type obtainable.
  lemonade_amounts = {"blue": 1.0}  # Start with 1 litre of pink lemonade.

  for _ in range(n):
    offered, desired, rate = map(float, input().split())

    # Update the amount of desired lemonade based on the trade, even if initially 0.
    lemonade_amounts[desired] = max(0, lemonade_amounts.get(desired, 0), lemonade_amounts[offered] * rate)

  # Return the maximum amount of blue lemonade, capped at 10 litres.
  return min(10.0, lemonade_amounts.get("blue", 0))

if __name__ == "__main__":
  n = int(input())
  result = max_blue_lemonade(n)
  print(f"{result:.6f}")
