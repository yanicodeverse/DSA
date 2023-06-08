A = [6, 5, 3, 4, 2, 7]


def s_sort(arr):
    n = len(arr)
    for i in range(n-1):
        print('iteration no. ', i+1, " = ", arr)
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return arr


print(s_sort(A))
