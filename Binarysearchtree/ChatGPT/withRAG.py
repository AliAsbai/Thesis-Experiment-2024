class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.left_count = 0

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
            root.left_count += 1
        else:
            root.right = insert(root.right, key)
    return root

def depth(root, key, d=0):
    if root is None:
        return 0
    if root.key == key:
        return d
    if key < root.key:
        return depth(root.left, key, d+1)
    else:
        return depth(root.right, key, d+1)

def main():
    counter = 0
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    root = Node(numbers[0])
    print(0)
    for num in numbers[1:]:
        root = insert(root, num)
        counter += depth(root, num) + root.left_count
        print(counter)

if __name__ == "__main__":
    main()
