def berlin_clock(time):
    top_light = 0
    if int(time[-2:]) % 2 == 1:
        top_light = 'O'
    else:
        top_light = 'Y'
    first_row = 0
    hr = time[:2]
    min = time[3:5]
    first_row = ('R'*(int(hr)//5)).ljust(4,'O')
    second_row = ('R'*(int(hr) % 5)).ljust(4,'O')
    third_row = []
    for i in range(1, 12):
        if i % 3 != 0 and i*5 <= int(min):
            third_row.append('Y')
        elif i % 3 == 0 and i*5 <= int(min):
            third_row.append('R')
        else:
            third_row.append('O')
    third_row = ''.join(third_row)
    fourth_row = ('Y'*(int(min) % 5)).ljust(4,'O')
    return "\n".join([top_light, first_row, second_row, third_row, fourth_row])