def insertion_sort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while(i>=0 and arr[i] > key):
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
    return arr

A = [7, 2, 3, 1, 5, 4]
print(insertion_sort(A))
B = [80, 38, 27, 9, 1, 102, 78]
print(insertion_sort(B))
