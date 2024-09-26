def digital_root(n):
    digits = list(map(int, str(n)))
    if sum(digits) < 10:
        return sum(digits)
    else:
        return digital_root(sum(digits))
    
# matt's solution using divmod
digital_root=lambda n:n if n<10 else digital_root(sum(divmod(n,10)))