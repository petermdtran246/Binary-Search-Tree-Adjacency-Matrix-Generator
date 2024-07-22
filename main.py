from binary_tree import Node,  insert_preorder
from adjacency_matrix import create_adjacency_matrix, print_adjacency_matrix

def read_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

if __name__ == "__main__":
    filename = 'numbers.txt'
    numbers = read_file(filename)

    root = None
    for number in numbers:
        root = insert_preorder(root, number) # Build the binary search tree

    n = len(numbers)
    # Initialize adjacency matrix
    adjacency_matrix = [[0] * n for _ in range(n)]
    # Populate adjacency matrix
    create_adjacency_matrix(root, numbers, adjacency_matrix)
    # Print the adjacency matrix
    print_adjacency_matrix(adjacency_matrix)



