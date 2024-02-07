#defining merge sort function
def merge_sort(array, p, r):
    if p >= r:
        return p
    q = (p + r) // 2  # calculating mid point

    #divide the array from mid point into two parts and reccursively do merge sort
    merge_sort(array, p, q)
    merge_sort(array, q + 1, r)

    # in the end merge the two arrays
    merge(array, p, q, r)

# defining function of merging
def merge(array, p, q, r):
    # calculating sizes of two subarrayays to be merged
    nL = q - p + 1
    nR = r - q

    # creating two temporary arrays of sizes calculated above and initiate all elements as zero
    L = [0] * nL
    R = [0] * nR

    # copy data in array A[p:q] to temporary arrays L[]
    for i in range(nL):
        L[i] = array[p + i]

    # copy data in array A[p:q] to temporary arrays R[]
    for j in range(nR):
        R[j] = array[q + 1 + j]

    # Following steps to merge the two subarrays back into the original array
    i = 0  # index of left array, i indexes the smallest remaining element in L[]
    j = 0  # index of right array, j indexes the smallest remaining element in R[]
    k = p  # index of merge array

    #This part for when there are unmerged elements in both the arrays L and R
    while i < nL and j < nR: # copy smallest unmerged element back into array A[p:r]
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # this part for, when there no unmerged elements in R[] array and copy the remaining elements of L[]
    while i < nL:
        array[k] = L[i]
        i += 1
        k += 1

    # this part for, when there no unmerged elements in L[] array and copy the remaining elements of R[]
    while j < nR:
        array[k] = R[j]
        j += 1
        k += 1

# example of using merge sort
array_to_sort = [12, 11, 13, 5, 6, 7]
print("array before sorting:", array_to_sort)
merge_sort(array_to_sort, 0, len(array_to_sort) - 1)
print("array after sorting:", array_to_sort)
