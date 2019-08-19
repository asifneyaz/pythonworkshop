#mergesort in python
def mergesort(A):
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        mergesort(L)
        mergesort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            A[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            A[k] = R[j]
            j = j + 1
            k = k + 1
    
arr = [7,6,2,1,9,10,2,5,8,101,-78,-29]        
mergesort(arr)
print(arr)