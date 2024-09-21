def operation(a, b):
    count = 0
    while a != b:
        if a > b and a % 2 == 1:
            a  = (a-1)//2
            count +=1
        elif b > a and a & (a - 1) != 0:
            a //=2
            count +=1
        elif b > a and a % 2 == 1 and a > 1:
            a  = (a-1)//2
            count +=1
        elif b > a and a & (a - 1) == 0:
                a *= 2
                count +=1
        else:
            a //=2
            count +=1

    return count 