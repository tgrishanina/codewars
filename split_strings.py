def solution(s):
    output = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(s) % 2 == 0:
        return output
    else:
        output[-1] = output[-1] + '_'
        return output