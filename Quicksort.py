#function to quick sort
def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)# partition subarray around pivot
        quicksort(array, p, q - 1) # reccursively sort low side
        quicksort(array, q + 1, r) # reccursively sort high side

#function to partition, 
def partition(array, p, r):
    x = array[r] #pivot
    i = p - 1

    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i] # exchanging A[i] and A[j] elements

    array[i + 1], array[r] = array[r], array[i + 1] # exchanging A[i + 1] and A[r] elements
    return i + 1

# example use of quick sort
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quicksort(array, 0, len(array) - 1)
print("Sorted array:", array)
