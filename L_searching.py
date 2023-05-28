def search(arr, size, x):

    for i in range(0, size):
        if arr[i] == x:
            return i
    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 4
    n = len(arr)
    # print(n)
    result = search(arr, n, x)
    if result == -1:
        print("Element is not present in the array")
    else:
        print('Element found at index: ', result)
