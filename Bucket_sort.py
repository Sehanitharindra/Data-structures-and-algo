#defining bucket sort function
def bucket_sort(array):
    n = len(array)
    buckets = [[] for _ in range(n)] #initializing new array for buckets

    # put elements into buckets considering on their values
    for number in array:
        index = int(number * n)
        buckets[index].append(number)

    # sort each bucket using insertion sort
    for bucket in buckets:
        insertion_sort(bucket)

    # concatenate the sorted buckets to get the final sorted arrayay
    concatenateList = [element for bucket in buckets for element in bucket]
    return concatenateList

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

# exampe use of bucket sort
array = [0.8, 0.5, 0.2, 0.6, 0.3, 0.1, 0.7, 0.4, 0.9]
print("array before sorting:", array)
sorted_array = bucket_sort(array)
print("array after sorting:", sorted_array)
