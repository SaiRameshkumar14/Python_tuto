class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

def traverse_tree(root, choice):
    if choice == 1:
        print("Inorder Traversal:")
        inorder(root)
    elif choice == 2:
        print("Preorder Traversal:")
        preorder(root)
    elif choice == 3:
        print("Postorder Traversal:")
        postorder(root)
    else:
        print("Invalid choice!")

# Input elements of the tree
def input_tree():
    root = None
    n = int(input("Enter the number of elements: "))
    print("Enter the elements")
    for i in range(n):
        key = int(input(f"Enter the key {i} : "))
        root = insert(root, key)
    return root

# Main function
def main():
    root = input_tree()
    choice = int(input("Enter your choice (1 for Inorder, 2 for Preorder, 3 for Postorder): "))
    traverse_tree(root, choice)

main()