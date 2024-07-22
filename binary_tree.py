class Node:
    """
    Represents a node in a binary search

    Attributes:
        left (Node): A reference to the left child node.
        right (Node): A reference to the right child node.
        data (int): The data value stored in the node.
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert_preorder(root, data):
    """
    Inserts a new node with the given data value into a binary search tree
    using a preorder insertion.

    Args:
        root (Node): The current root node of the binary search tree.
        data (int): The data value to be inserted.

    Returns:
        Node: The root node of the modified binary search tree after insertion.
    """
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_preorder(root.left, data)
    else:
        root.right = insert_preorder(root.right, data)
    return root
