#! /usr/bin/python3

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def insert(root, val):
  if root is None:
    return Node(val)
  if val < root.data:
    root.left = insert(root.left, val)
  else:
    root.right = insert(root.right, val)
  return root

def main():
  n = int(input())
  root = None
  total_depth = 0
  for _ in range(n):
    val = int(input())
    root = insert(root, val)
    total_depth += 1  # Update depth after each insertion
    print(total_depth - 1)

if __name__ == "__main__":
  main()
