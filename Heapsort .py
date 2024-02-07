#defining heap sort function
def heap_sort(array):
    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]  # swaping root element with i th element 
        array = array[:-1] # reducing the size of array by one
        max_heapify(array, 0)  # call max heap, because now new array is not a max heap

# defining function to build max heap
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, i)

#defining max heapify funtion
def max_heapify(array, i):
    heap_size = len(array)# finding heap size

    left_child = 2 * i + 1 #finding left child of i
    right_child = 2 * i + 2 #finding right child of i

    if left_child < heap_size and array[left_child] > array[i]:
        largest = left_child
    else :
        largest = i

    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)

# example use of above heapsort functions
array = [4, 10, 3, 5, 1]
print("array before sorting:", array)
heap_sort(array)
print("array after sorting:", array)

