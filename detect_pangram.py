def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    st = st.replace(" ", "").lower()
    return all(letter in st for letter in alphabet)

# cut down version

is_pangram = lambda st: all(letter in st.replace(" ", "").lower() for letter in "abcdefghijklmnopqrstuvwxyz")