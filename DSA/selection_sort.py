def selection_sort(A):
    n =len(A)
    for i in range(n-1):
        min =i
        for j in range(i+1,n):
            if A[min]>A[j]:
                min =j

        temp =A[min]
        A[min]=A[i]
        A[i] =temp
        #A[min],A[i] =A[i],A[min]
