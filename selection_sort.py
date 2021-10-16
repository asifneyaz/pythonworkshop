# Python program for implementation of Selection
# Sort

A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):
    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j
    A[min_index], A[i] = A[i], A[min_index]



# Driver code to test above
print(A)


