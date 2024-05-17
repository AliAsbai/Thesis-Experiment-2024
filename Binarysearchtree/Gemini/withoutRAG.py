class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    self.root = self._insert(self.root, data, 0)
    return self.counter

  def _insert(self, node, data, depth):
    if node is None:
      self.counter = depth
      print(f"Inserting {data} at depth {depth}")
      return Node(data)
    if data < node.data:
      node.left = self._insert(node.left, data, depth + 1)
    else:
      node.right = self._insert(node.right, data, depth + 1)
    return node

  counter = 0

def main():
  # Read input
  n = int(input())
  bst = BinarySearchTree()
  for _ in range(n):
    data = int(input())
    depth = bst.insert(data)
    print(depth)

if __name__ == "__main__":
  main()
