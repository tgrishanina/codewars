def parse_int(string):
        # Define the mapping of words to numbers
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
        'seventy': 70, 'eighty': 80, 'ninety': 90
    }

    # Define the scale mappings
    scale_map = {
        'hundred': 100, 
        'thousand': 1000, 
        'million': 1000000, 
    }

    # Normalize input
    words = string.lower().replace('-', ' ').split()
    total = 0
    factor = 0
    last_scale = 1

    for word in words:
        if word in number_map:
            factor += number_map[word]
        elif word in scale_map:
            scale = scale_map[word]
            if scale == 100:
                factor *= scale
            else:
                total += factor * scale
                factor = 0


    total += factor
    return total