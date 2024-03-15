def merge(left, right):
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            arr.append(right[j])
            j += 1
        else:
            arr.append(left[i])
            i += 1
    
    while i < len(left):
        arr.append(left[i])
        i += 1
    
    while j < len(right):
        arr.append(right[j])
        j += 1
    
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    L = merge_sort(arr[:len(arr)//2:])
    R = merge_sort(arr[len(arr)//2::])
    arr = merge(L, R)
    return arr

a = [2, 6, 0, 2, -5, 5.2, 1]
a = merge_sort(a)
print(a)