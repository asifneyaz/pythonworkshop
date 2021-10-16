


def insertion_sort(A):
    for index in range(1, len(A)):
        position = index - 1
        temp = A[index]

        while position >= 0:
            if temp < A[position]:
                A[position+1] = A[position]
                position = position - 1
            else:
                break
        A[position+1] = temp
    return A


sol = insertion_sort([4,1,2,6,3,5])
print(sol)










