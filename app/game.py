from random import choice

def determine_winner(user_choice, computer_choice):
    """
    This function determines the winning choice between a user choice and computer choice in rock, paper, scissors.
    
    Parameters:
        user_choice (str): A string of the user's choice ("rock", "paper", or "scissors")
        computer_choice (str): A string of the computer's choice ("rock", "paper", or "scissors")

    Returns:
        winning_choice (str): A string of the winning choice between user_choice and computer_choice
    
    Invoke like this: determine_winner("rock", "paper")
    Example return value: "paper"
    """
    #return "paper"
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice


if __name__ == "__main__":

    valid_selections = ["rock", "paper", "scissors"] # only have to update in one place

    #USER SELECTION

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_selections:
        print("OOPS, TRY AGAIN")
        exit()

    #COMPUTER SELECTION

    c = choice(valid_selections)
    print("COMPUTER CHOICE:", c)

    #DETERMINE WINNER

    winner = determine_winner(u,c)
    if winner == u:
        print("YOU WON")
    elif winner == c:
        print("COMPUTER WON")
    else:
        print("TIE")

