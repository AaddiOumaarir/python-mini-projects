import random as rd
MAX_LIGNES  = 3
MIN_BET = 1
MAX_BET = 1000
def main():
    amount = Deposit() 
    lignes = GetNumberOfLines()
    bet = GetBet()
    total_bet = lignes * bet
    print(f"you bet {bet}$ on {lignes} lines. Total bet is {total_bet}.")

def Deposit():
    valid_amount = True
    while valid_amount:
        amount = input("Please enter the amount to deposit: ")
        if amount.isdigit():
            if int(amount) == 0:
                print("The deposit cannot be 0.")
            else:
                valid_amount = False
        else:
            print("Sorry, the amount should be a positive number.")
    return int(amount)

def GetNumberOfLines():
    while True:
        nol = input(f"Please enter the number of lignes to bet on (1-{MAX_LIGNES}): ") # number of lignes
        if nol.isdigit():
            if 1 <= int(nol) <= MAX_LIGNES:
                break
            else:
                print(f" the number of lignes should be between 1 and {MAX_LIGNES}.")
        else:
            print(f"Sorry, the number of lignes should be between 1 and {MAX_LIGNES}")
    return int(nol)

def GetBet():
    while True:
        bet = input(f"How much do you want to bet on each ligne (min: {MIN_BET} , max : {MAX_BET}) ")
        if bet.isdigit():
            if MIN_BET <= int(bet) <= MAX_BET:
                break
            else:
                print(f" the bet should be between {MIN_BET} and {MAX_BET}.")
        else:
            print(f"Sorry, the bet should be between {MIN_BET} and {MAX_BET}")
    return int(bet)
main()