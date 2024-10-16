# moving through the alphabet
def move_ten(st):
    result = []
    for char in st:
        result.append(chr((ord(char) - ord('a') + 10) % 26 + ord('a')))
    return ''.join(result)