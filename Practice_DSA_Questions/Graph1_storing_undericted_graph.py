# ------------------------- storing undirected graph in memory using adgency matrix ----------------------------

# def creating_adjacency_matrix(num_vertices, edges):
#     # Initialize a num_vertices x num_vertices matrix with 0s
#     adj_matrix = [[0] * num_vertices for i in range(num_vertices)]

#     # Fill the adjacency matrix based on the given edges
#     for u, v in edges:
#         adj_matrix[u][v] = 1  # Mark the edge from u to v and v to u (in both direction)
#         adj_matrix[v][u] = 1  

#     return adj_matrix

# # Define the number of vertices in the graph
# num_vertices = 4

# # Define the directed edges (from node u to node v)
# edges = [(0, 1), (1, 2), (2, 3), (3, 1), (3, 2)]

# # Create the adjacency matrix
# adj_matrix = creating_adjacency_matrix(num_vertices, edges)
# # print(adj_matrix)

# # Print the adjacency matrix
# for row in adj_matrix:
#     print(row)



# ----------------------------or ------------------------------


def creating_adjacency_matrix(num_vertices, edges):
    # Initialize a num_vertices x num_vertices matrix with 0s
    adj_matrix = []
    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            row.append(0)
        adj_matrix.append(row)

    # Print the matrix
    for row in adj_matrix:
        print(row)
    print()

    # Fill the adjacency matrix based on the given edges
    for u, v in edges:
        adj_matrix[u][v] = 1  # Mark the edge from u to v or u to v (in both direction)
        adj_matrix[v][u] = 1  

    return adj_matrix

# Define the number of vertices in the graph
num_vertices = 4

# Define the directed edges (from node u to node v)
edges = [(0, 1), (1, 2), (2, 3), (3, 1), (3, 2)]

# Create the adjacency matrix
adj_matrix = creating_adjacency_matrix(num_vertices, edges)
# print(adj_matrix)

# Print the adjacency matrix
for row in adj_matrix:
    print(row)