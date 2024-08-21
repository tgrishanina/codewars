def to_weird_case(words):
    
    return ' '.join(
        ''.join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(word))
        for word in words.split()
    )

# using lambda function:
to_weird_case = lambda words: ' '.join(
        ''.join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(word))
        for word in words.split()
    )