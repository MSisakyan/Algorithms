def insert_sort(arr):
    for i in range(1, len(arr)):
        index = i - 1
        num = arr[i]
        
        while index >= 0 and arr[index] > num:
            arr[index+1] = arr[index]
            index -= 1
        arr[index+1] = num
    return arr

a = [2, 6, 0, 2, -5, 5.2, 1]
a = insert_sort(a)
print(a)