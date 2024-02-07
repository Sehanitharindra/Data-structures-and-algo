#defining radix sort function
def radix_sort(array):
    # finding maximum number in array. it has the maximum number of digits
    max_num = max(array)
    exponent = 1

    # do counting sort for every digit place (LSD to MSD)
    while max_num // exponent > 0:
        count_arraying_sort(array, exponent)
        exponent *= 10

def count_arraying_sort(array, exponent):
    n = len(array)
    output_array = [0] * n
    count_array = [0] * 10

    # counting occurrences of each digit at the current selected place of value
    for i in range(n):
        index = array[i] // exponent
        count_array[index % 10] += 1

    # updting count_array 
    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    #building the output array by placing elements at their correct place
    i = n - 1
    while i >= 0:
        index = array[i] // exponent
        output_array[count_array[index % 10] - 1] = array[i]
        count_array[index % 10] -= 1
        i -= 1

    # copy the sorted elements back to the array
    for i in range(n):
        array[i] = output_array[i]

# example using of radix sort
array = [170, 145, 175, 190, 802, 124, 211, 366]
print("array before sorting:", array)
radix_sort(array)
print("array after sorting:", array)
