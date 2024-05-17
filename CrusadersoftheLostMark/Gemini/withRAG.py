import sys
from bisect import bisect_left

def solve():
  """Solves the housing problem for ponies."""
  c, a = map(int, sys.stdin.readline().strip().split())
  budgets = 1500
  affordable_cities = [[] for _ in range(a)]  # Stores affordable cities for each pony (list for binary search)
  costs = [-1] * (c + 1)  # Stores costs of cities (indexed from 1)

  # Read pony incomes
  incomes = list(map(int, sys.stdin.readline().strip().split()))

  # Track queried city costs for budget awareness
  queried_costs = set()

  for _ in range(min(a, budgets)):  # Limit queries based on budget (potentially avoids unnecessary checks)
    line = sys.stdin.readline().strip()
    if line[0] == 'Q':
      # Ask for cost of a city
      city = int(line[2:])
      if city in queried_costs:
        print(f"Error: Already queried city {city}")
        continue
      if budgets <= 0:
        print("Error: Budget exceeded")
        return
      budgets -= 1
      print(f"Q {city}")
      costs[city] = int(sys.stdin.readline().strip())
      queried_costs.add(city)
      
      # Update affordable cities for all ponies with binary search (potentially fewer checks)
      for i in range(a):
        if incomes[i] >= costs[city]:
          index = bisect_left(affordable_cities[i], costs[city])
          affordable_cities[i].insert(index, city)
    else:
      break  # Stop processing lines after exceeding or reaching budget limit

  # Assign cities based on available information (might not be optimal for all ponies)
  for i, assignment in enumerate(map(int, line.split()[1:])):
    if not affordable_cities[i]:
      print(f"Error: Pony {i+1} has no affordable city")
      continue
    city = affordable_cities[i][bisect_left(affordable_cities[i], incomes[i])]
    print(f"A {city} {i+1}")

if __name__ == "__main__":
  solve()
  sys.stdout.flush()
