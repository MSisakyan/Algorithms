def bubble_sort(arr):
    swapped = 1
    for i in range(len(arr)):
        if not swapped:
            break
        swapped = 0
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                c = arr[i]
                arr[i] = arr[j]
                arr[j] = c
                swapped = 1
    return arr

a = [2, 6, 0, 2, -5, 5.2, 1]
a = bubble_sort(a)
print(a)