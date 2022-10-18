import random
import time

def table1():
    cell = []
    rango_de_nums = []
    loteria = []
    status = []
    
    select = range(10,61) #creo un rango de nums para escoger
    rango_de_nums = list(select) #hago lista
    random.shuffle(rango_de_nums) #revolviendo los nums ya escogidos
    
    for cont in range (16): #tomando 16 nums de la lista
        loteria.append(rango_de_nums.pop())
        
    for row in range(4): #creando matrix
        cell.append([]) #[[x],[x],[x],[x]]
        for column in range(4):
            cell[row].append(loteria.pop(0)) #toma un num y lo descarta
    
    for row in range(4):
        status.append([])
        for column in range(4):
            status[row].append(False)
            
    return cell, status


def table2():
    cell = []
    rango_de_nums = []
    loteria = []
    status = []
    
    select = range(10,61) #creo un rango de nums para escoger
    rango_de_nums = list(select) #hago lista
    random.shuffle(rango_de_nums) #revolviendo los nums ya escogidos
    
    for cont in range (16): #tomando 16 nums de la lista
        loteria.append(rango_de_nums.pop())
        
    for row in range(4): #creando matrix
        cell.append([]) #[[x],[x],[x],[x]]
        for column in range(4):
            cell[row].append(loteria.pop(0)) #toma un num y lo descarta
    
    for row in range(4):
        status.append([])
        for column in range(4):
            status[row].append(False)
            
    return cell, status

def randNum():
    nums = range(10, 61)
    selected = list(nums)
    random.shuffle(selected)
    dato = selected.pop()
    return dato

def modoDeJuego():
    """
    Pregunto en que modo de juego quiero jugar. H = horizonatles. V = verticales. F = llena.
    Hago chequear al programa si se llenan los espacios indicados para ganar.
    """
    print("¡Welcome to the one and only game of chance, LOTTERY!\n", "~by Sir Andreas Haidacher~\n")
    
    gamemode1 = None
    while gamemode1 not in ("H", "V", "F"):
        gamemode1 = input("Write 'H', 'V' or 'F' if thee will want to go on playing this game of chance:").upper()
        
        if gamemode1 == "H":
            print("Gamemode set to horizontal playing style.\n")
        elif gamemode1 == "V":
            print("Gamemode set to vertical playing style.\n")
        elif gamemode1 == "F":
            print("Gamemode set to fill-it-all playing style.\n")
        else:
            print("Gamemode statement is non-existent or invalid. Please select the gamemode you want to play.\n")
    return gamemode1

def WinnerWinnerChickenDinner(gamemode, player1, player2):
    """
    Depending on gamemode define winner in each way
    """
    status1 = player1[1]
    status2 = player2[1]
    winner1 = False
    winner2 = False
    nummer = 0
    vdd = True

    #predetermino ganador en diferente modo de juego. Los dos ganadores ganan si tienen el mismo pattern. tonses se repide op
    
    if gamemode == "H": #I check the row so --> [row][column]
        for row in range(4):
            
            if status1[row][0] == vdd and status1[row][1] == vdd and status1[row][2] == vdd and status1[row][3] == vdd:
                winner1 = vdd
                
            elif status2[row][0] == vdd and status2[row][1] == vdd and status2[row][2] == vdd and status2[row][3] == vdd:
                
                winner2 = vdd
                
    if gamemode == "V": #I check the column so --> [column][row]
        for row in range(4):
            if status1[0][row] == vdd and status1[1][row] == vdd and status1[2][row] == vdd and status1[3][row] == vdd:
                winner1 = vdd
                
            elif status2[0][row] == vdd and status2[1][row] == vdd and status2[2][row] == vdd and status2[3][row] == vdd:
                winner2 = vdd
                
    if gamemode == "F":
        for row in range(4): #I check every row and column so --> [row][column] and [column][row] Winner 1
            if status1[row][0] == vdd and status1[row][1] == vdd and status1[row][2] == vdd and status1[row][3] == vdd:
                if status1[0][row] == vdd and status1[1][row] == vdd and status1[2][row] == vdd and status1[3][row] == vdd:
                    nummer =+ 1
            if nummer == 4:
                winner1 = vdd
                
            elif status1[row][0] == vdd and status1[row][1] == vdd and status1[row][2] == vdd and status1[row][3] == vdd:
                if status2[0][row] == vdd and status2[1][row] == vdd and status2[2][row] == vdd and status2[3][row] == vdd:
                    nummer =+ 1
            if nummer == 4:
                winner2 = vdd
    return winner1, winner2
                
                
def doesItExist(picked_num, player1, player2):
    vdd = True
    for row in range(4):
        for column in range(4):
        
            if player1[0][row][column] == picked_num:
                player1[1][row][column] = vdd
            
            if player2[0][row][column] == picked_num:
                player2[1][row][column] = vdd
                
                
                
def printTable(player1, player2):
    """
    Hacer tablero y en caso de que ya haya sido llamado entonces printear '██' en vez del numero
    """
    cells = player1[0]
    status = player1[1]
    cells2 = player2[0]
    status2 = player2[1]
    
    table1 = []
    table2 = []
    
    for row in range(len(status)):
        table1.append([])
        for column in range(4):
            if status[row][column] == True:
                table1[row].append("██")
            else:
                table1[row].append(cells[row][column])
                
    for row in range(len(status2)):
        table2.append([])
        for column in range(4):
            if status2[row][column] == True:
                table2[row].append("██")
            else:
                table2[row].append(cells2[row][column])
                
    print("      PLAYER 1      ||      PLAYER 2")
    print(f" {table1[0][0]}   {table1[0][1]}   {table1[0][2]}   {table1[0][3]}  ||  {table2[0][0]}   {table2[0][1]}   {table2[0][2]}   {table2[0][3]}")
    print(f" {table1[1][0]}   {table1[1][1]}   {table1[1][2]}   {table1[1][3]}  ||  {table2[1][0]}   {table2[1][1]}   {table2[1][2]}   {table2[1][3]}")
    print(f" {table1[2][0]}   {table1[2][1]}   {table1[2][2]}   {table1[2][3]}  ||  {table2[2][0]}   {table2[2][1]}   {table2[2][2]}   {table2[2][3]}")
    print(f" {table1[3][0]}   {table1[3][1]}   {table1[3][2]}   {table1[3][3]}  ||  {table2[3][0]}   {table2[3][1]}   {table2[3][2]}   {table2[3][3]}\n")

def main():
    vdd = True
    partyTime_untz_untz = vdd
    
    player1 = table1()
    player2 = table2()
    gamemode = modoDeJuego()
    
    while partyTime_untz_untz:
        
        
        picked_num = randNum()
        printTable(player1, player2)
        winner = WinnerWinnerChickenDinner(gamemode, player1, player2)
        
        doesItExist(picked_num, player1, player2)
        print('Called number is',picked_num)
        printTable(player1, player2)
        time.sleep(1)
        winner = WinnerWinnerChickenDinner(gamemode, player1, player2)
       
        if winner[0] == True:
            print("¡Player1, thou shall be named WINNER!")
            partyTime_untz_untz = False
        elif winner[1] == True:
            print("¡Player2, thou shall be named WINNER!")
            partyTime_untz_untz = False
        else:
            play_again = input("Press ENTER to roll another number!")
                
main()
