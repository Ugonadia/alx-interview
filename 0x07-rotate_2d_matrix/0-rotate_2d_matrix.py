#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The 2D matrix to rotate. The matrix must be square.

    Returns:
        None: The matrix is edited in-place.

    Raises:
        ValueError: If the matrix is not square (number of rows != number of columns).
    """

    n = len(matrix)

    if n != len(matrix[0]):
        raise ValueError("Matrix must be square")

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
