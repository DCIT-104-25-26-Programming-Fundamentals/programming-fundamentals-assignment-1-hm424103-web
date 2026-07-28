# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def input_positive_int(prompt):
    """Read a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid integer.")


def read_matrix(rows, cols, matrix_name="Matrix"):
    """Read a matrix from the user with the given number of rows and columns."""
    matrix = []
    for i in range(1, rows + 1):
        while True:
            row_input = input(f"Enter row {i} of {matrix_name}: ")
            parts = row_input.strip().split()
            if len(parts) != cols:
                print(f"Error: Please enter exactly {cols} values.")
                continue
            try:
                row = [int(value) for value in parts]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid integer values.")
    return matrix


def transpose_matrix(matrix):
    """Return the transpose of a matrix."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-size matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    return [[matrix_a[r][c] + matrix_b[r][c] for c in range(cols)] for r in range(rows)]


def multiply_matrices(matrix_a, matrix_b):
    """Return the product of matrix_a and matrix_b."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = []
    for r in range(rows_a):
        result_row = []
        for c in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[r][k] * matrix_b[k][c]
            result_row.append(total)
        result.append(result_row)
    return result


def print_matrix(matrix, label=None):
    """Print a matrix in a neat aligned grid."""
    if label:
        print(label)
    if not matrix:
        print("[]")
        return
    width = max(len(str(value)) for row in matrix for value in row) + 1
    for row in matrix:
        print("".join(str(value).rjust(width) for value in row))


def main():
    """Main function to run matrix operations for assignment 4."""
    print("PART A — Transpose a Matrix")
    rows = input_positive_int("Enter number of rows: ")
    cols = input_positive_int("Enter number of columns: ")
    matrix = read_matrix(rows, cols, "Matrix A")
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transpose_matrix(matrix))

    print("\nPART B — Add Two Matrices")
    rows = input_positive_int("Enter number of rows for matrices: ")
    cols = input_positive_int("Enter number of columns for matrices: ")
    matrix_a = read_matrix(rows, cols, "Matrix A")
    matrix_b = read_matrix(rows, cols, "Matrix B")
    print("\nMatrix A + Matrix B:")
    print_matrix(add_matrices(matrix_a, matrix_b))

    print("\nPART C — Multiply Two Matrices")
    rows_a = input_positive_int("Enter number of rows for matrix A: ")
    cols_a = input_positive_int("Enter number of columns for matrix A: ")
    print("For matrix B, the number of rows must equal the number of columns of matrix A.")
    rows_b = cols_a
    cols_b = input_positive_int("Enter number of columns for matrix B: ")
    matrix_a = read_matrix(rows_a, cols_a, "Matrix A")
    matrix_b = read_matrix(rows_b, cols_b, "Matrix B")
    print("\nMatrix A × Matrix B:")
    print_matrix(multiply_matrices(matrix_a, matrix_b))


if __name__ == "__main__":
    main()

