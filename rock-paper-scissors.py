def rps(p1, p2):
    
    if p1 == "scissors":
        if p2 == "scissors":
            return "Draw!"
        elif p2 == "rock":
            return "Player 2 won!"
        elif p2 == "paper":
            return "Player 1 won!"
    elif p1 == "rock":
        if p2 == "scissors":
            return "Player 1 won!"
        elif p2 == "rock":
            return "Draw!"
        elif p2 == "paper":
            return "Player 2 won!"
    elif p1 == "paper":
        if p2 == "scissors":
            return "Player 2 won!"
        elif p2 == "rock":
            return "Player 1 won!"
        elif p2 == "paper":
            return "Draw!"