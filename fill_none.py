def fill(arr, method=0):
    if arr == []:
        return []
    elif method == -1:
        next_value = None
        # Iterate through the list backwards
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] is None:
                arr[i] = next_value
            else:
                next_value = arr[i]
        return arr
    elif method == 1:
        prev_value = None
        # Iterate through the list from left to right
        for i in range(len(arr)):
            if arr[i] is None:
                arr[i] = prev_value
            else:
                prev_value = arr[i]
        return arr
    else:
        
        n = len(arr)
        def find_left(i):
            return next(((arr[j], i - j) for j in range(i - 1, -1, -1) if arr[j] is not None), (None, float('inf')))
        def find_right(i):
            return next(((arr[j], j - i) for j in range(i + 1, n) if arr[j] is not None), (None, float('inf')))
        result = arr[:]
        
        for i in range(n):
            if result[i] is None:
                left_val, left_dist = find_left(i)
                right_val, right_dist = find_right(i)
                if left_dist < right_dist:
                    result[i] = left_val
                elif right_dist < left_dist:
                    result[i] = right_val
                else:
                    result[i] = min(left_val, right_val) if left_val is not None and right_val is not None else (left_val or right_val)
    return result