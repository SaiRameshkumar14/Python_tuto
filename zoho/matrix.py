def matrix_positions(matrix):
    n = len(matrix)
    positions = {}

    # Store positions of values in the matrix
    for i in range(n):
        for j in range(n):
            positions[matrix[i][j]] = (i, j)

    # Sort the values and print their positions
    sorted_values = sorted(positions.keys())
    for value in sorted_values:
        print(positions[value][0] + 1, positions[value][1] + 1)


# Example input matrix
matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

matrix_positions(matrix)
