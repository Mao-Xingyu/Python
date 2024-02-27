import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 12,
    "B": 9,
    "C": 6,
    "D": 3      
}

symbol_value = {
    "A": 1,
    "B": 2,
    "C": 4,
    "D": 6      
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#append all key-value pair in symbol_count dictionary into all_symbols list
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #make sure slotmachine follows the symbol_count dictionary correctly
    columns = []
    for _ in range(cols):
        column = []
        #do a copy of all_symbols into current_symbols
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#printing the slot machine with pipes to segment the columns and rows
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


#get user input of a valid amount of deposit to play
def deposit():
    while True:
        amount = input("How much would you like to deposit? \n$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Pleast enter a valid amount.")

    return amount

#get user input of number of lines to play
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}) \n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be greater than 0.")
        else:
            print("Pleast enter a valid number.")

    return lines

#get user input of number of bet to play
def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? \n$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Pleast enter a valid bet.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough deposit, your current balance is: ${balance}")
        else:
            break
    
    print(f"you are betting ${bet} on {lines} lines. \nTotal bet is equal to : ${total_bet}")
    balance -= total_bet 

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You've won ${winnings}!")
    if winnings != 0:
        print(f"You won on lines: ", *winning_lines)
        balance += winnings
    else:
        print("Good luck next time!")

    return balance

#main function to execute all other functions
def main():
    balance = deposit()
    while True:
        print(f"Current blanace is ${balance}")
        play = input("Press enter to play(q to quit)")
        if play == "q":
            break
        balance = spin(balance)
    print(f"Current credit ${balance}") 

main()