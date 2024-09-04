# args allows a function to take any number of positional arguments!
def last(*args):
    # Check if any arguments were passed
    if len(args) == 0:
        return None  # No arguments passed, return None or some default value
    
    # If a single argument is passed (which could be a string, list, tuple, etc.)
    if len(args) == 1:
        item = args[0]
        # If the single argument is a string or a list/tuple, return the last character/item
        if isinstance(item, (str, list, tuple)):
            return item[-1]
        # Otherwise, return the item itself, since it's not iterable
        return item
    
    # If multiple arguments are passed, return the last one
    return args[-1]