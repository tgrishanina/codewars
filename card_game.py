def card_game(n):
    cards_total = []
    while n != 0:
        if n % 2 == 0 and (n % 4 != 0 or n == 4):
            cards = n//2
            cards_total.append(cards)
            n = n//2
        else: 
            cards = 1
            cards_total.append(cards)
            n = n-1
    return sum(cards_total[c] for c in range(0, len(cards_total), 2))