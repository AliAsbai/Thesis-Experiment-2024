import sys

from collections import deque

def solve():
  C, A = map(int, input().split())
  incomes = list(map(int, input().split()))
  budget = 1500
  affordable_cities = [None] * A
  queries = deque()
  cost_of_living = [float('inf')] * (C + 1)

  def can_afford(pony_id, city):
    return cost_of_living[city] <= incomes[pony_id]

  # Loop through applications
  for i in range(A):
    # Early check for no affordable city (optional)
    if incomes[i] < 1:
      print(f"Error: No affordable city found for pony {i+1}")
      sys.stdout.flush()
      continue

    # Find the first affordable city (using binary search)
    low, high = 1, C
    while low <= high:
      mid = (low + high) // 2
      if can_afford(i, mid):
        low = mid + 1
      else:
        high = mid - 1

    # Check if a city was found
    if low > C:
      print(f"Error: No affordable city found for pony {i+1}")
      sys.stdout.flush()
      return

    # Suggest the city if already known
    if cost_of_living[low] != float('inf'):
      print(f"A {low} {' '.join(str(affordable_cities[j] if affordable_cities[j] is not None else 0) for j in range(A))}")
      sys.stdout.flush()
      continue

    # Ask for cost of living if needed and budget allows
    if budget > 0:
      budget -= 1
      print(f"Q {mid}")
      sys.stdout.flush()
      queries.append(mid)

    # Read cost of living if asked
    if queries:
      cost = int(input())
      city_id = queries.popleft()
      cost_of_living[city_id] = cost  # Update cost for future references
      # Update affordable cities for future references based on the cost
      for j in range(i + 1, A):
        if incomes[j] >= cost:
          affordable_cities[j] = city_id

  print(f"A {' '.join(str(affordable_cities[j]) for j in range(A))}")
  sys.stdout.flush()  # Flush output after final line

solve()
