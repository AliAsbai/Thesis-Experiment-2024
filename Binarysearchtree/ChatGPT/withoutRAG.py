class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.depth = 0

def insert(root, key, depth):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key, depth + 1)
        else:
            root.left = insert(root.left, key, depth + 1)
    return root, depth

def inorder_traversal(root):
    if root:
        left_depth = inorder_traversal(root.left)
        right_depth = inorder_traversal(root.right)
        root.depth = max(left_depth, right_depth)
        return root.depth + 1
    return 0

def construct_bst(arr):
    if not arr:
        return None
    root = Node(arr[0])
    depth = 0
    for num in arr[1:]:
        root, depth = insert(root, num, depth)
        inorder_traversal(root)
    return root

if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    root = construct_bst(arr)
    inorder_traversal(root)
