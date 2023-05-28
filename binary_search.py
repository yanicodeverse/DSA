def Bsearch(arr, size, x):

    low = 0
    high = size-1
    mid = 0

    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] == x):
            return mid
        elif (arr[mid] > x):
            high = mid - 1
        elif (arr[mid] < x):
            low = mid + 1
        else:
            pass
    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 2
    n = len(arr)
    result = Bsearch(arr, n, x)
    if result == -1:
        print("Element is not present in the array")
    else:
        print('Element found at index: ', result)
