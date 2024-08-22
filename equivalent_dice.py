from itertools import combinations_with_replacement
from functools import reduce
from operator import mul

# def eq_dice(set_):
#     set_ = sorted(set_)
#     result = []
    
#     # Calculate the product of the input set
#     total = reduce(mul, set_, 1)
    
#     # Filter potential factors within the range [3, 21]
#     factors_filtered = [f for f in range(3, 21) if total % f == 0]
    
#     for r in range(1, max(len(set_), len(factors_filtered)) + 1):
#         for c in combinations_with_replacement(factors_filtered, r):
#             sorted_combination = sorted(c)
#             product = reduce(mul, c, 1)
#             # Exclude the original input and single-element lists with the total value
#             if product == total and sorted_combination != set_ and sorted_combination != [total]:
#                      result.append(sorted_combination)
    
    
#     return len(result)

def eq_dice(set_):
    set_ = sorted(set_)
    result = []
    
    # Calculate the product of the input set
    total = reduce(mul, set_, 1)
    
    # Find factors of the total within the range [3, 21]
    factors_filtered = [f for f in range(3, 21) if total % f == 0]
    
    # Generate combinations efficiently
    for r in range(1, max(len(set_), len(factors_filtered)) + 1):
        for c in combinations_with_replacement(factors_filtered, r):
            product = reduce(mul, c, 1)
            # Exclude the original input and single-element lists with the total value
            if product == total and sorted(c) != set_ and sorted(c) != [total]:
                result.append(sorted(c))
    return len(result)