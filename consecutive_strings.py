def longest_consec(strarr, k):
    if k > len(strarr) or len(strarr) == 0 or k <= 0:
        return ""
    else:
        concat_list = []
        for i in range(len(strarr)):
            concat = ''.join(strarr[i:k]) 
            k +=1
            concat_list.append(concat)
        return max(concat_list, key = len)