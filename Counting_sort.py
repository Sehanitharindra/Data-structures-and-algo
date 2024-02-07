#defining counting sort function
def counting_sort(array, k):
    n = len(array)

    # initializing new arrays B and C
    B = [0] * n
    C = [0] * (k + 1)

    # counting occurance of elements in A = array
    for j in range(n):
        C[array[j]] += 1

   
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    # copy elements from A to the array B starting from end of A
    for j in range(n - 1, -1, -1):
        B[C[array[j]] - 1] = array[j]
        C[array[j]] -= 1

    return B

# example use of counting sort
array = [4, 2, 0, 1, 3, 4, 6, 5, 2]
print("array before sorting:", array)
k = max(array)  # k is the maximum value in the array
sorted_array = counting_sort(array, k)
print("array after sorting:", sorted_array)
