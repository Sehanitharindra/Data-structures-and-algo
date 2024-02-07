#function of insertion sort is being defined
def insertion_sort(array):
    # run the for loop from secend index to last index of array.
    for i in range(1, len(array)):
        key = array[i]  # Assign current element to be the key
        j = i - 1 
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]  # Move elements of array that are greater than the key and position it in one position ahead current position
            j -= 1

        array[j + 1] = key  # Place the key in correct position.

#Example sorting of array using insertion sort
array_to_sort = [12, 11, 13, 5, 6]
print("array before sorting:", array_to_sort) # print array before sorting
insertion_sort(array_to_sort)
print("sorted array:", array_to_sort) # print array after sorting
