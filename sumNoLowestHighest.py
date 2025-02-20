def sum_array(arr):
    x = 0
    if type(arr) != list or len(arr) < 3:
        return 0
    arr.sort()
    del arr[0]
    del arr[-1]
    for i in arr:
        x += i
        
    return x