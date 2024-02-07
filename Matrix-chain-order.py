#defining matrix chain order function
#the implementation has the same notation in algorithm in book
def matrix_chain_order(p):
    n = len(p) - 1
    #initialiazing two new tables m and s, while m[1:n, 1:n], s[1:n-1, 2:n]
    m = [[0] * (n + 1) for _ in range(n + 1)] #initialize all the elemnts at 0
    s = [[0] * n for _ in range(n)]#initialize all the elements at zero, this is because it is easier to implement at begining

    for l in range(2, n + 1): # l is the chain length
        for i in range(1, n - l + 2): #chain begins at Ai
            j = i + l - 1 #chain ends at Aj
            m[i][j] = float('inf')
            for k in range(i, j): # try A(i:k) A(k+1:j)
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q #remember this cost
                    s[i - 1][j - 1] = k #remeber this index

    return m, s

# example use of matrix
matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]
m_output, s_output = matrix_chain_order(matrix_dimensions)

# printing the resulting output m and s tables
print("Matrix m:")
for row in m_output:
    print(row)

print("\nMatrix s:")
for row in s_output:
    print(row)
