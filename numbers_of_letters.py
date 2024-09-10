def numbers_of_letters(n):
    digits = list(map(int, str(n)))
    number_map = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 
                  7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}
    word = ''.join([number_map[digit] for digit in digits])
    words = [word]
    current = 0
    if n ==4:
        return ['four']
    while len(word) != current: 
        current = len(word)
        digits_current = list(map(int, str(current)))
        word = ''.join([number_map[d] for d in digits_current])
        words.append(word)
    return words
        