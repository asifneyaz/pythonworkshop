def bubble_sort(arr):
    temp = 0
    steps = 0
    for j in range(len(arr)-1):
        for i in range(0, len(arr)-j-1):
            steps += 1
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    print(steps)
    return arr


print(bubble_sort([4,2,3,1,5,3,8,9,0,3,8,16,21]))


