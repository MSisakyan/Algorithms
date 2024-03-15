def create(n):
    return [0] * (n+1)

def radix_sort(arr):
    lst = create(max(arr)+1)
    
    for i in arr:
        lst[i] += 1
    
    i = 0
    res = []
    while i < len(lst):
        if lst[i]:
            res.append(i)
            lst[i] -= 1
        else:
            i += 1
    return res

a = [2, 6, 0, 2, 1]
a = radix_sort(a)
print(a)