x = input("Enter cells: ")

print("---------")
print("|", x[0], x[1], x[2], "|")
print("|", x[3], x[4], x[5], "|")
print("|", x[6], x[7], x[8], "|")
print("---------")

# O match detection
VertO = False
for n in range(3):
    if x[n] == "O" and x[n + 3] == "O" and x[n + 6] == "O":  # Vertical "O" match detection
        VertO = True

HoriO = False
for n in range(0, 7, 3):
    if x[n] == "O" and x[n + 1] == "O" and x[n + 2] == "O":  # Horizontal "O" match detection
        HoriO = True

DiagO = False  # Diagonal "O" match detection
if (x[0] == "O" and x[4] == "O" and x[8] == "O") or (x[2] == "O" and x[4] == "O" and x[6] == "O"):
    DiagO = True

VictO = False
if VertO or HoriO or DiagO:  # O victory detection
    VictO = True


# X match detection
VertX = False
for n in range(3):
    if x[n] == "X" and x[n + 3] == "X" and x[n + 6] == "X":  # Vertical "X" match detection
        VertX = True

HoriX = False
for n in range(0, 7, 3):
    if x[n] == "X" and x[n + 1] == "X" and x[n + 2] == "X":  # Horizontal "X" match detection
        HoriX = True

DiagX = False  # Diagonal "X" match detection
if (x[0] == "X" and x[4] == "X" and x[8] == "X") or (x[2] == "X" and x[4] == "X" and x[6] == "X"):
    DiagX = True
    
VictX = False
if VertX or HoriX or DiagX:  # X victory detection
    VictX = True


# amount of X's and O's
QuantX = 0
QuantO = 0
for n in x:
    if n == "O":
        QuantO += 1
    elif n == "X":
        QuantX += 1


# is the game impossible
if (VictO and VictX) or QuantO > QuantX + 1 or QuantX > QuantO + 1:
    impossible = True
else:
    impossible = False


# empty space detection
if QuantO + QuantX < 9:
    space = True
else:
    space = False


# finish message
if impossible:
    print("Impossible")
elif VictX:
    print("X wins")
elif VictO:
    print("O wins")
elif space:
    print("Game not finished")
else:
    print("Draw")

print("VertO: ", VertO)
print("HoriO: ", HoriO)
print("DiagO: ", DiagO)
print("VictO: ", VictO)
print()
print("VertX: ", VertX)
print("HoriX: ", HoriX)
print("DiagX: ", DiagX)
print("VictX: ", VictX)
print()
print("QuantO: ", QuantO)
print("QuantX: ", QuantX)
print()
print("Impossible? ", impossible)
print("Space?", space)