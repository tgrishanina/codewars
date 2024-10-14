def valid_word(seq, word):
    # Create a set for fast lookup of words
    word_set = set(seq)
    # Create a list to track if we can segment the string up to each index
    dp = [False] * (len(word) + 1)
    dp[0] = True  # Empty string can always be segmented

    # Iterate over the string
    for i in range(1, len(word) + 1):
        for j in range(i):
            # If the substring s[j:i] is a word and the string up to j can be segmented
            if dp[j] and word[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(word)]