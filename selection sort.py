def sort(arr):
    for i in range(len(arr)):
        mininum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mininum]:
                mininum = j
        arr[i], arr[mininum] = arr[mininum], arr[i]
    return arr

a = [2, 6, 0, 2, -5, 5.2, 1]
a = sort(a)
print(a)