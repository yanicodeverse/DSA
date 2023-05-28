def swap(a, b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def bsort(arr):
    n = len(arr)
    for i in range(0, n):
        print('iteration number: ', i+1)
        for j in range(0, n - i - 1):
            print('    internal iteration number: ', j+1)
            print('         before swapping: ', arr)

            if arr[j] > arr[j + 1]:
                swap(j, j+1, arr)
            print('         after swapping: ', arr)
    return arr


if __name__ == '__main__':
    arr = [4, 2, 10, 1, 7, 5, 9]
    print('before sorting: ', arr)
    print('after sorting: ', bsort(arr))
