x = input("Enter cells: ")

print("---------")
print("|", x[0], x[1], x[2], "|")
print("|", x[3], x[4], x[5], "|")
print("|", x[6], x[7], x[8], "|")
print("---------")

#O match detection
VertO = False
for n in range(3):
    if x[n] == "O" and x[n + 3] == "O" and x[n + 6] == "O":  #Vertical "O" match detection 
        VertO = True

HoriO = False
for n in range(0, 7, 3):
    if x[n] == "O" and x[n + 1] == "O" and x[n + 2] == "O":  #Horizontal "O" match detection
        HoriO = True

DiagO = False
if (x[0] == "O" and x[4] == "O" and x[8] == "O") or (x[2] == "O" and x[4] == "O" and x[6] == "O"):  #Diagonal "O" match detection
    DiagO = True

VictO = False
if VertO or HoriO or DiagO:  #O victory detection
    VictO = True


#X match detection
VertX = False
for n in range(3):
    if x[n] == "X" and x[n + 3] == "X" and x[n + 6] == "X":  #Vertical "X" match detection
        VertX = True

HoriX = False
for n in range(0, 7, 3):
    if x[n] == "X" and x[n + 1] == "X" and x[n + 2] == "X":  #Horizontal "X" match detection
        HoriX = True

DiagX = False
if (x[0] == "X" and x[4] == "X" and x[8] == "X") or (x[2] == "X" and x[4] == "X" and x[6] == "X"):  #Diagonal "X" match detection
    DiagX = True
    
VictX = False
if VertX or HoriX or DiagX:  #X victory detection
    VictX = True


#amount of X's and O's
QuantX = 0
QuantO = 0
for n in x:
    if n == "O":
        QuantO += 1
    elif n == "X":
        QuantX += 1


#is the game impossible
if (VictO and VictX) or QuantO > QuantX + 1 or QuantX > QuantO + 1:
    impossible = True
else:
    impossible = False


#empty space detection
if QuantO + QuantX < 9:
    space = True
else:
    space = False


#finish message
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





#X move
y = input("Enter the coordinates: ").split()


#coordinate detection
if y[0] in ["1", "2", "3"] and y[1] in ["1", "2", "3"]:
    coordinate = True
else:
    coordinate = False


#number detection
nums = True

if coordinate == False:
    for n in y[0]:
        if n not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            nums = False

    for n in y[1]:
        if n not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            nums = False


#index finder
def index_finder(a, b):
    if a == 1:
        return int(b) - 1
    if a == 2:
        return int(b) + 2
    if a == 3:
        return int(b) + 5


#position availability detection
availability = True

if x[index_finder(int(y[0]), int(y[1]))] in ["O", "X"]:
    availability = False


#putting move on board
if coordinate == True and availability == True:
    x = list(x)
    x[index_finder(int(y[0]), int(y[1]))] = "X"
    x = "".join(x)




#x move
legal = 0
while legal == 0:
    y = input("Enter the coordinates: ").split()
    legal = 1

#number detector
    if legal == 1:
        def num_detector(x):
            if list(x) in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
