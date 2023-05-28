def Bsearch(arr, low, high, x):

    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] == x):
            return mid
        elif (arr[mid] > x):
            return Bsearch(arr, low, mid-1, x)
        elif (arr[mid] < x):
            return Bsearch(arr, mid + 1, high, x)
        else:
            pass
    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 4
    n = len(arr)
    result = Bsearch(arr, 0, n-1, x)
    if result == -1:
        print("Element is not present in the array")
    else:
        print('Element found at index: ', result + 1)
