from preloaded import animals, elements

def chinese_zodiac(year):
    count = year - 1924
    
    return f"{elements[int((count/2))%5]} {animals[count%12]}"