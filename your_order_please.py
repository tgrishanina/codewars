def order(sentence):
    # 1) split the sentence into words, 2) filter out the digits from each word, 
    # 3) join the filtered digits back together into a string, 4) convert the string of digits into int to use as sorting key
    # 5) sort the list based on the provided key, 6) join the list back together into a sentence
    
    return ' '.join(sorted(sentence.split(), key=lambda word: int(''.join(filter(str.isdigit, word)))))