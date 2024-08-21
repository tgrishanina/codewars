def lottery(ticket,win):
    #initialize mini-win counter
    mini_win_ct = 0
    #loop through each subarray
    for sub_array in ticket:
        # break each subarray down into a string and number
        string, num = sub_array
        if any(ord(char) == num for char in string):
            mini_win_ct += 1
    #compare the mini-win count to the win input        
    if mini_win_ct >= win:
        return "Winner!"
    else:
        return "Loser!"