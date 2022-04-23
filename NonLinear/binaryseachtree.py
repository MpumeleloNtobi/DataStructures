# A class to create a tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A class to create a binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_done = Node(data)
        if self.root is None:
            self.root = new_done
        else:
            current_node = self.root
            while True:
                if new_done.data < current_node.data:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = new_done
                        break
                elif new_done.data > current_node.data:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = new_done
                        break
                else:
                    break

# Print a binary search tree in-order
def print_inorder(root):
    def print_tree_(node):
        if node is None:
            return
        print_tree_(node.left)
        print(node.data, end=" -> ")
        print_tree_(node.right)
    print_tree_(root)
    print("None")

# Print a binary search tree in pre-order
def print_preorder(root):
    def print_tree_(node):
        if node is None:
            return
        print(node.data, end=" -> ")
        print_tree_(node.left)
        print_tree_(node.right)
    print_tree_(root)
    print("None") 

# Print a binary search tree in post-order
def print_postorder(root):
    def print_tree_(node):
        if node is None:
            return
        print_tree_(node.right)
        print(node.data, end=" -> ")
        print_tree_(node.left)
    print_tree_(root)
    print("None")   
