import random

MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

SYMBOL_COUNT ={
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

SYMBOL_VALUE = {
    "A" : 10,
    "B" : 7,
    "C" : 5,
    "D" : 3
}

def deposit():
    amount = input("How much would you like to deposit (Enter positive integer)? $")
    try:
        amount = int(amount)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        print("You must enter the whole number more than zero. ")
        return deposit()

def get_number_of_lines():
    number_lines = input("On how many lines would you like to bet? Type a number from 1 to 3: ")
    try:
        number_lines = int(number_lines)
        if 3 < number_lines <= 0:
            raise ValueError
        return number_lines
    except ValueError:
        print("You must enter the whole number from 1 to 3. ")
        return get_number_of_lines()

def get_bet(limit, lines):
    amount = input(f"How much would you like to bet (Enter the number from {MIN_BET} to {MAX_BET})? $")
    try:
        amount = int(amount)
        if amount <= 0:
            raise ValueError("You must bet value more than zero. ")
        if amount * lines >= limit:
            raise ValueError("You cannot bet more than number of lines multiply by bet! ")
        return amount
    except ValueError as e:
        print(e)
        print(f"You must enter the whole number from {MIN_BET} to {MAX_BET}. ")
        return get_bet(limit, lines)
    

def get_slot_machine_spin():
    all_symbols = []
    
    for symbol, symbol_count in SYMBOL_COUNT.items():

        for _ in range(symbol_count):

            all_symbols.append(symbol)

    columns = []

    for _ in range(ROWS):
        column = []
        actual_symbols = all_symbols[:]
        for _ in range(COLS):
            random_symbol = random.choice(actual_symbols)
            column.append(random_symbol)
            actual_symbols.remove(random_symbol)
        columns.append(column)
    
    return columns

def print_results(columns):
    for row in range(len(columns)):
        for col in range(len(columns[row])):
            if col != len(columns[row]) - 1:
                print(columns[col][row], end=" | ")
            else:
                print(columns[col][row], end="")
        print()


def check_winnings(columns, lines, bet):
    winnings = 0
    wining_lines = []
    for row in range(lines):
        symbol = columns[0][row]
        for col in columns:
            symbol_to_check = col[row]
            if symbol_to_check != symbol:
                break
        else:
            winnings += SYMBOL_VALUE[symbol] * bet
            wining_lines.append(row)

    return winnings, wining_lines

def main():
    amount = deposit()
    while True:
        print(f"Amount of money: ${amount}")
        if input("Press enter if you want to play. Enter q if you wish to stop. ").lower() == 'q':
            break
        lines = get_number_of_lines()
        bet = get_bet(amount, lines)
        columns = get_slot_machine_spin()
        print_results(columns)
        winnings, winning_lines = check_winnings(columns, lines, bet)
        print(f"You have won: ${winnings}")
        print("You won on lines:", *winning_lines)
        amount += winnings - bet * lines
    
    print(f"You ended the game with ${amount}")


if __name__ =="__main__":
    main()



