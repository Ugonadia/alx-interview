#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Traverse the matrix layer by layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        # Rotate the elements in the current layer
        for i in range(first, last):
            offset = i - first

            # Save the top element
            top = matrix[first][i]

            # Move left element to top
            matrix[first][i] = matrix[last - offset][first]

            # Move bottom element to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move right element to bottom
            matrix[last][last - offset] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = top
