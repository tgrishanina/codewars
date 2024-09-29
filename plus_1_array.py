def up_array(arr):
    if len(arr) == 0:
        return None
    for i in range(len(arr)):
        if arr[i] < 0 or arr[i] > 9:
            return None
    num = int(''.join(map(str, arr)))
    num = num + 1
    new_arr = list(map(int, str(num)))
    if arr[0] == 0 and len(arr) > 1:
        new_arr1 = [0] + new_arr
        return new_arr1
    else:    
        return new_arr
    