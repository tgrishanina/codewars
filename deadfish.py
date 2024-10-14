def parse(data):
    val = 0
    result = []
    for x in [*data]:
        if x == 'i':
            val +=1
        elif x == 'd':
            val -=1
        elif x == 's':
            val **= 2
        elif x == 'o':
            result.append(val)