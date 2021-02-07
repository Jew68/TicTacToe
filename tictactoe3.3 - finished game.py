def print_board():
    print("---------")
    print("|", x[0], x[1], x[2], "|")
    print("|", x[3], x[4], x[5], "|")
    print("|", x[6], x[7], x[8], "|")
    print("---------")

def index_finder(a, b):
    if a == 1:
        return int(b) - 1
    if a == 2:
        return int(b) + 2
    if a == 3:
        return int(b) + 5

def victory():
    for n in range(3):
        if x[n] == x[n + 3] == x[n + 6] and x[n] in list("XO"):
            return True
    for n in range(0, 7, 3):
        if x[n] == x[n + 1] == x[n + 2] and x[n] in list("XO"):
            return True
    for n in range(2, 5, 2):
        if x[4 - n] == x[4] == x[4 + n] and x[n] in list("XO"):
            return True
    return False

numbers = list("1234567890")
x = list('         ')
turn = True

print_board()
while True:
    while True:
        move = input("Enter the coordinates: ")
        if move.split()[0] not in numbers or move.split()[1] not in numbers:
            print("You should enter numbers!")
        elif move.split()[0] not in list("123") or move.split()[1] not in list("123"):
            print("Coordinates should be from 1 to 3!")
        elif x[index_finder(int(move.split()[0]), int(move.split()[1]))] in list("XO"):
            print("This cell is occupied! Choose another one!")
        else:
            break
    if turn == True:
        x[index_finder(int(move.split()[0]), int(move.split()[1]))] = "X"
    else:
        x[index_finder(int(move.split()[0]), int(move.split()[1]))] = "O"
    print_board()
    if victory():
        if turn == True:
            print("X wins")
        else:
            print("O wins")
        break
    if not victory() and " " not in x:
        print("Draw")
        break
    turn = not turn