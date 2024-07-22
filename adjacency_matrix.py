def create_adjacency_matrix(root, node_list, matrix):
    """
    Creates an adjacency matrix representing the connections
    between nodes in a binary tree.

    Args:
        root (Node): The root node of the binary search tree.
        node_list (list): A list containing the data values of all nodes in the tree (in order).
        matrix (list): A 2D list representing the adjacency matrix to be filled.
    """
    if root is None:
        return

    # Find the index of current node's data in the list
    index = node_list.index(root.data)

    if root.left:
        left_index = node_list.index(root.left.data)
        matrix[index][left_index] = abs(root.data - root.left.data)
        # Recursive call for left subtree
        create_adjacency_matrix(root.left, node_list, matrix)

    if root.right:
        right_index = node_list.index(root.right.data)
        matrix[index][right_index] = abs(root.data - root.right.data)
        # Recursive call for right subtree
        create_adjacency_matrix(root.right, node_list, matrix)

def print_adjacency_matrix(matrix):
    print('Adjacency Matrix: ')
    for row in matrix:
        print(row)


