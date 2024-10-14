def flip_pancakes(stack):
    if not stack:
        return []
    
    flip_list = []
    n = len(stack)
    
    # Work on smaller and smaller parts of the stack
    while n > 1 and stack != sorted(stack):
        # Find the index of the largest pancake in the unsorted part of the stack
        largest_index = stack.index(max(stack[:n]))
        
        # If the largest pancake isn't already in the correct place
        if largest_index != n - 1:
            # If the largest pancake isn't at the top, bring it to the top with a flip
            if largest_index != 0:
                stack = stack[:largest_index+1][::-1] + stack[largest_index+1:]
                flip_list.append(largest_index)  # Append flip as 1-based index
                
            # Now flip it into its correct position
            stack = stack[:n][::-1]
            flip_list.append(n-1)  # Append flip as 1-based index
        
        # Reduce the size of the stack we're sorting
        n -= 1
    
    return flip_list
