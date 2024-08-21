def good_vs_evil(good, evil):
    
    good_points = [1,2,3,3,4,10]
    evil_points = [1,2,2,2,3,5,10]
    
    good_total = sum([int(x)*y for x, y in zip(good.split(), good_points)])
    evil_total = sum([int(x)*y for x, y in zip(evil.split(), evil_points)])
    
    if good_total > evil_total:
        return 'Battle Result: Good triumphs over Evil'
    elif good_total == evil_total:
        return 'Battle Result: No victor on this battle field'
    else:
        return 'Battle Result: Evil eradicates all trace of Good'
