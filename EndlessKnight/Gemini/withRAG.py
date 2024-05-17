#! /usr/bin/python3

MOD = 10007

def solve(H, W, rocks):
  prev_row = [0] * (W + 1)
  # Initialize the first two elements of prev_row for valid knight moves from (1, 1)
  prev_row[1] = 1
  if W >= 3 and (1, 3) not in rocks:
    prev_row[3] = 1

  curr_row = [0] * (W + 1)

  for row in range(1, H + 1):
    # Regular calculations for rows after the first row
    if row > 1:
      for col in range(1, W + 1):
        if (row, col) not in rocks:
          curr_row[col] = (prev_row[col] + prev_row[col - 2]) % MOD
      else:
        curr_row[col] = 0
    prev_row, curr_row = curr_row, [0] * (W + 1)

  return prev_row[W]

def main():
  for _ in range(int(input())):
    H, W, R = map(int, input().split())
    rocks = set(tuple(map(int, input().split())) for _ in range(R))
    answer = solve(H, W, rocks)
    print(f"Case #{_+1}: {answer}")

if __name__ == "__main__":
  main()
