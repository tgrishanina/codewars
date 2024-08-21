def rpsls(pl1, pl2):
    # Your Magnificent Code here
    if (pl1 == "scissors" and pl2 == "paper"):
        return("Player 1 Won!")
    elif (pl1 == "paper" and pl2 == "rock"):
        return("Player 1 Won!")
    elif (pl1 == "rock" and pl2 == "lizard"):
        return("Player 1 Won!")  
    elif (pl1 == "lizard" and pl2 == "spock"):
        return("Player 1 Won!")
    elif (pl1 == "spock" and pl2 == "scissors"):
        return("Player 1 Won!")
    elif (pl1 == "scissors" and pl2 == "lizard"):
        return("Player 1 Won!")
    elif (pl1 == "lizard" and pl2 == "paper"):
        return("Player 1 Won!")
    elif (pl1 == "paper" and pl2 == "spock"):
        return("Player 1 Won!")
    elif (pl1 == "spock" and pl2 == "rock"):
        return("Player 1 Won!")
    elif (pl1 == "rock" and pl2 == "scissors"):
        return("Player 1 Won!")
    elif(pl1 == pl2):
        return("Draw!")
    else:
        return("Player 2 Won!")