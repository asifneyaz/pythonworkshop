def binary_search(array, num):
    low = 0
    high = len(array) - 1
    found = False
    while(low <= high and not found):
        mid = (low + high)//2
        if num == array[mid]:
            found = True
        else:
            if num > array[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return found

print(binary_search([2, 4, 5, 8, 13, 15], 13))