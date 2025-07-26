import random as rd

MAX_LIGNES  = 3
MIN_BET = 1
MAX_BET = 1000
REELS = 3
ROWS = 3

symbols = {
    "\U0001F600": 2, #Grinning Face emoji
    "\U0001F680": 4, #Rocket emoji
    "\U0001F602": 6, #Face with Tears of Joy emoji
    "\U0001F525": 8 #Fire emoji
}
symbols_value = {
    "\U0001F600": 5,  
    "\U0001F680": 4,  
    "\U0001F602": 3,  
    "\U0001F525": 2 
}

def check_winnings(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet 
            winning_lines.append(lines +1)
    return winning, winning_lines
def get_spin(rows, cols, symbol):
    all_symbols = []
    for symbol, occurence in symbols.items():
        for _ in range(occurence):
            all_symbols.append(symbol)
    
    reels = []
    for i in range(cols):
        reel = []
        current_symbols = all_symbols[:]
        for j in range(rows):
            value = rd.choice(current_symbols)
            current_symbols.remove(value)
            reel.append(value)
        reels.append(reel)
    return reels
def print_slot_machine(cols):
    for row in range(len(cols)):
        for i, column in enumerate(cols[row]):
            if i != len(cols[row]) - 1:
                print(cols[i][row], "|", end=" ")
        
            else:
                print(cols[i][row])
            

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

def game(amount):
    
    lignes = GetNumberOfLines()
    bet = GetBet()
    total_bet = lignes * bet
    while True:
        if total_bet>amount:
            print("You don't have much balance for the desired bet.")
        else:
            break
    print(f"you bet {bet}$ on {lignes} lines. Total bet is {total_bet}.")
    slots = get_spin(ROWS, REELS, symbols)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lignes, bet, symbols_value)
    print(f"you won {winnings}")
    print(f"You won on ", *winning_lines)
    return winnings - total_bet
def main():
    amount = Deposit()
    while True:
        print(f"CURRENT BALLENCE ${amount}")
        answer = input("press any key to play (q to quit). ")
        if answer == "q".upper():
            break
        amount += game(amount)
    print(f"You are left with {amount}")


    
main()