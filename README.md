# Binary Search Tree Adjacency Matrix Generator
This Python project reads a list of integers from a text file, builds a binary search tree (BST), and creates an adjacency matrix representation of the BST. The adjacency matrix captures the connections between nodes and their weights (absolute difference in data values).

## Output
The script will print the resulting adjacency matrix to the console. Each row and column of the matrix corresponds to a node in the BST, and the value at a specific position represents the weight of the connection between the corresponding nodes.

## Project Structure
The project consists of three Python modules:

  -  binary_tree.py: Defines the Node class for representing nodes in the BST and the insert_preorder function to insert nodes using a preorder insertion strategy.
  -  adjacency_matrix.py: Contains the create_adjacency_matrix function to populate the adjacency matrix based on the BST structure and the print_adjacency_matrix function to print the matrix.
  -  main.py: The main script that reads numbers from a file, builds the BST, creates the adjacency matrix, and prints it.

