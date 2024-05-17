#! /usr/bin/python3

from decimal import Decimal

def dfs_iterative(node, amount, graph, needs, super_powers):
  """
  Performs an iterative depth-first search to simulate liquid flow.

  Args:
      node: The starting node for exploration.
      amount: The initial amount of liquid (as Decimal).
      graph: A dictionary representing the tree structure.
      needs: A list containing the required amount of liquid for each node (Ki).
      super_powers: A list containing flags indicating super power for each pipe.

  Yields:
      True if all leaves have enough liquid, False otherwise.
  """
  stack = [(node, amount)]
  while stack:
    node, current_amount = stack.pop()
    if not graph.get(node):  # Leaf node reached
      yield abs(current_amount - Decimal(needs[node])) <= Decimal('1e-6')
    else:
      children = graph[node]
      total_flow = Decimal('0.0')
      for child, flow, is_super in zip(children, graph[node][1::2], super_powers[node][1::2]):
        flow = Decimal(str(flow / 100.0))  # Convert flow percentage to Decimal
        total_flow += flow
        child_amount = current_amount * (flow if not is_super else flow**2)
        if child_amount >= Decimal('0.0'):  # Check for negative flow (potential issue)
          stack.append((child, child_amount))

def solve(data):
  """
  Solves the ant feeding problem using binary search.

  Args:
      data: A list containing the parsed input data.

  Returns:
      The minimum amount of liquid needed to feed the ants (as a string).
  """
  n, edges, needs = data
  graph = {}
  super_powers = {}
  for parent, child, flow, is_super in edges:
    graph.setdefault(parent, []).append(child)
    graph.setdefault(child, []).append(parent)
    super_powers.setdefault(parent, []).append(0)
    super_powers.setdefault(child, []).append(0)
    super_powers[parent][-1] = is_super

  low, high = Decimal('0.0'), Decimal('2**31 - 1')  # Search for minimum liquid amount
  while low + Decimal('1e-6') < high:
    mid = (low + high) / 2
    if any(dfs_iterative(1, mid, graph, needs, super_powers)):
      high = mid
    else:
      low = mid
  return str(low)[:11]  # Limit output to 10 decimal places + 1 for integer part

def main():
  """
  Reads input data, parses it, and calls the solve function.
  """
  data = []
  for line in sys.stdin:
    data.append([float(x) if i == len(data) else int(x) for i, x in enumerate(line.strip().split())])
  result = solve(data)
  print(result)

if __name__ == "__main__":
  main()
