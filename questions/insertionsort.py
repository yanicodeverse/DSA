def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):

        j = i - 1
        temp = arr[i]
        print('     temp after every iteration: ', temp)
        while (j >= 0) and (arr[j] > temp):
            arr[j + 1] = arr[j]
            j -= 1
            arr[j+1] = temp
            print('             element after sorting: ', arr)

    return arr


if __name__ == '__main__':
    arr = [7, 13, 3, 4, 1]
    print('before sorted: '.capitalize(), arr)
    print('after sorter: '.capitalize(), insertion_sort(arr))
