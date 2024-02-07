#defining function for reccursive matrix multiplication
def matrix_multiply_recursive(A, B, C, n):
    # This is the base case that is when n==1 and perform matrix multiplication 
    if n == 1:
        C[0][0] += A[0][0] * B[0][0]
        return C[0][0]

    # divide matrices A, B, C into sub matrices
    A11, A12, A21, A22 = partition_matrix(A, n)
    B11, B12, B21, B22 = partition_matrix(B, n)
    C11, C12, C21, C22 = partition_matrix(C, n)

    # reccursively multiply submatrices
    matrix_multiply_recursive(A11, B11, C11, n // 2)
    matrix_multiply_recursive(A11, B12, C12, n // 2)
    matrix_multiply_recursive(A21, B11, C21, n // 2)
    matrix_multiply_recursive(A21, B12, C22, n // 2)
    C[0][0] = matrix_multiply_recursive(A12, B21, C11, n // 2)
    C[0][1] = matrix_multiply_recursive(A12, B22, C12, n // 2)
    C[1][0] = matrix_multiply_recursive(A22, B21, C21, n // 2)
    C[1][1] = matrix_multiply_recursive(A22, B22, C22, n // 2)

#defining partitioning of matrix
def partition_matrix(matrix, n):
    # partitioning matrix into four matrices
    # here we assume n is maltiple of 2
    breaking_point = n // 2
    return (
        [row_of_matrix[:breaking_point] for row_of_matrix in matrix[:breaking_point]],  # A11
        [row_of_matrix[breaking_point:] for row_of_matrix in matrix[:breaking_point]],  # A12
        [row_of_matrix[:breaking_point] for row_of_matrix in matrix[breaking_point:]],  # A21
        [row_of_matrix[breaking_point:] for row_of_matrix in matrix[breaking_point:]]   # A22
    )

# example using of above function
#the example is same example in book
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[0, 0], [0, 0]]
matrix_multiply_recursive(A, B, C, 2)
print("result matrix C after multiplication of A and B:", C)
