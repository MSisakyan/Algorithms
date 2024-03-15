def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    left = list(filter(lambda x: x < arr[0], arr))
    middle = list(filter(lambda x: x == arr[0], arr))
    right = list(filter(lambda x: x > arr[0], arr))
    
    return quick_sort(left) + middle + quick_sort(right)

a = [2, 6, 0, 2, -5, 5.2, 1]
a = quick_sort(a)
print(a)