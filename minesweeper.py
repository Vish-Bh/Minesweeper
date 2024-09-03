import random
totalMinescounter={}
mineLocation = set()
mineLocationList=[]
allnumber=set()
numborad = []
styleBorad = []
mineBorad = []
symbol_map = {
    0: "| 0|",
    1: "| 1|",
    2: "| 2|",
    3: "| 3|",
    4: "| 4|",
    5: "| 5|",
    6: "| 6|",
    7: "| 7|",
    8: "| 8|",
    9: "| 9|",
}
noOfRow=4


def giveBorad():
    global numborad, styleBorad, mineBorad, noOfRow
    if noOfRow%2!=0:
        noOfRow+=1

    # Makes a matrix type of board used for numbering and then used for setting up mines
    numborad = [["00" for _ in range(noOfRow)] for _ in range(int(noOfRow))]
    for i in range(int(noOfRow)):
        for j in range(noOfRow):
            numborad[i][j] = f'{i}{j}'
    mineBorad = [row.copy() for row in numborad]

    # Makes the board better :)
    # Add style to it
    styleBorad = [["⬜ " for _ in range(noOfRow)] for _ in range(int(noOfRow))]

def setMines():
    global mineLocation, mineBorad,allnumber
    while len(mineLocation) < 2*noOfRow:
        y = random.randint(0, noOfRow - 1)
        x = random.randint(0, int(noOfRow) - 1)
        if (x, y) not in mineLocation:  # Avoid setting multiple mines in the same location
            mineBorad[x][y] = "🎇"
            mineLocation.add(tuple([x, y]))
    for (i, j) in mineLocation:
        mineLocationList.append((int(f"{i}{j}")))

def boardPrint(board1, board2=None):
    if board2 is None:
        board2 = styleBorad

    for row1, row2 in zip(board1, board2):
        row_output = "".join(f"{item1:<3}|{item2:<3}|" for item1, item2 in zip(row1, row2))
        print(row_output)
    print()

def noOfMines(mines=mineLocationList):
    global mineLocationList, totalMinescounter
    global allnumber
    allnumber=set(range((int(noOfRow)*int(noOfRow))))
    #this give every title  no of mines around it
    #the second one given them a symbol which is used for style
    for i in range(0, (int(noOfRow)*int(noOfRow))):
        counter=0
        if i%noOfRow!=0 and i%noOfRow!=noOfRow-1 :
            if i-1 in mines:
                counter+=1
            if i+1 in mines:
                counter+=1
            if i-(noOfRow) in mines:
                counter+=1
            if i-(noOfRow-1) in mines:
                counter+=1
            if i-(noOfRow+1) in mines:
                counter+=1
            if i+(noOfRow) in mines:
                counter+=1
            if i+(noOfRow+1) in mines:
                counter+=1
            if i+(noOfRow-1) in mines:
                counter+=1
            totalMinescounter[i]=counter
        elif i%noOfRow==0:
            if i+1 in mines:
                counter+=1
            if i+(noOfRow) in mines:
                counter+=1
            if i+(noOfRow+1) in mines:
                counter+=1
            if i-(noOfRow) in mines:
                counter+=1
            if ((i-noOfRow)+1 in mines):
                counter+=1
            totalMinescounter[i]=counter
        elif i%noOfRow==noOfRow-1:
            counter=0
            if (i-1 in mines):
                counter+=1
            if (i+(noOfRow) in mines):
                counter+=1
            if (((i+noOfRow)-1) in mines):
                counter+=1
            if (i-(noOfRow) in mines):
                counter+=1
            if ((i-noOfRow)-1 in mines):
                counter+=1
        totalMinescounter[i]={
            "counter": counter,
            "symbol" : None}
    for i in totalMinescounter:
        totalMinescounter[i]["symbol"] = symbol_map.get(totalMinescounter[i]["counter"], "")
        if i in mines:
            totalMinescounter[i]["symbol"] = "💥"

def replaceTilteBlank(userInput):
    global mineLocationList, mineBorad, allnumber ,styleBorad, totalMinescounter,alive, noOfRow
    tens=userInput//10
    ones=userInput%10
    if userInput not in mineLocationList :
        styleBorad[tens][ones]=totalMinescounter[userInput]["symbol"]
        difference.remove(userInput)
        mineBorad[tens][ones]=totalMinescounter[userInput]["symbol"]

    if userInput in mineLocationList:
        styleBorad[tens][ones]="💥 "
        alive=False

def startGame():
    global mineLocationList, difference
    print("\033[2J")  
    print("\033[1;1H")  
    giveBorad()
    setMines()
    noOfMines()
    difference = [item for item in allnumber if item not in mineLocationList]
    global noOfRow, mineLocationList, alive
    alive= True
    while alive:
        print("\033[2J")  
        print("\033[1;1H")  
        boardPrint(numborad)
        print(mineLocationList)
        userInput=int(input("Enter the guess block:  " ))
        if len(difference)==0:
            print("\033[2J")
            print("\033[1;1H")
            print("Congratulations you won")
            break
        if userInput not in allnumber:
            print("Invalid input")
        else:
            
            replaceTilteBlank(userInput)
    print("\033[2J")  
    print("\033[1;1H")  
    print("Game Over")
    print("YOu Lost HAHAHAHA")

startGame()
