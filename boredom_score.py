def boredom(staff):
    pass #your code here
    dict = {"accounts": 1,
    "finance": 2,
    "canteen": 10,
    "regulation": 3,
    "trading": 6,
    "change": 6,
    "IS": 8,
    "retail": 5,
    "cleaning": 4,
    "pissing about": 25}
    cumulative_score = sum([dict[i] for i in staff.values()])
    if cumulative_score <= 80:
        return "kill me now"
    elif cumulative_score >= 100:
        return "party time!!"
    else:
        return "i can handle this"
