#! /usr/bin/python3

def main():
  """Reads input, transforms long variation to short and prints the result."""
  # Read input line
  line = input().strip()

  # Split names separated by hyphens
  names = line.split("-")

  # Extract first letter from each name
  short_name = "".join([name[0].upper() for name in names])

  # Print the short variation
  print(short_name)

if __name__ == "__main__":
  main()
