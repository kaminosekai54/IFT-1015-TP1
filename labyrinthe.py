# @author :
# @ Culpin Alexis
# @ Edwin Ganmavo
# This program is built to be a library that help you building a
# labyrinthes


###############################################################################

# Import
import random



###############################################################################
# functions definition


# function 
def iota(n):
    # this function return a list of lenght n, 
    # containing the int from 0 to n
    # @param,
    # @n, the end born of the range
    if n >= 0:
        return list(range(n))
    else:
        print("error, n must be a negative Integer")



# function contient
# this function return a bool if the the element x 
# is included in the list tab
# @param
# @tab, the list to check
# @ x, the element to search in the list
def contient(tab, x):
    return x in tab





# function ajouter
# this function add the leement x in the list tab
# if x is not already in tab
# @param
# @tab, the list to add the element,
# @x, the element to add in the tab
def ajouter(tab, x):
    if x >= 0 and not x in tab:
        tab.append(x)
        return tab
    else:
        print("error, x must be a positive integer and not already included in tab, nothing added")
        return tab




# function retirer
# this function remove the element x from the list tab and returns it
# @param
# @tab, the list where we will remove an element
# @x, the element to remove
def retirer(tab, x):
    # print("function retirer")
    # print(tab)
    # print(x)
    if x in tab:
        del tab[tab.index(x)]
        return tab
    else:
        # print("error, x must be in tab, nothing have been deleted")
        return tab


# function voisin
# this function return the list of case number that are neighbour
# of the case representing by the x,y coords 
# @param
# @x, the x coords of our case
# @y, the y coords of our case
# @nX, the width of our grid
# @nY, the hight of our grid
def voisins(x,y,nX,nY):
    list=[]

    if x >= 0 and y>=0 and nX >=0 and nY >=0:
        if x>0:
            list.append(x-1+y*nX)
        
        if y>0:
            list.append(x + (y - 1) * nX)

        if y-1 < nY:
            list.append(x+(y+1)*nX)
        if x+1 < nX:
            list.append(x + 1 + y * nX)
    
    return list

# function getCaseNumber
#  this function return the numer of the case defined by our x,y coords
# @param
# @x, the x coords of our case
# @y, the y coords of our case
# @nX, the width of our grid
# @nY, the hight of our grid
def getCaseNumber(x,y,nX,nY):
    return x+(y*nX)



#  function getWalls
#  this function return a list containing the number of the wall of a case
# in the list the walls are orderd as follow,
#  [north, south, est, ouest]
#  if a wall should not exist, is value is -1
# @param
# @x, the x coords of our case
# @y, the y coords of our case
# @nX, the width of our grid
# @nY, the hight of our grid
def getWalls(n, nX,nY):
    walls = {}
    x, y = getCoords(n,nX,nY)

    walls["N"] = append(x + y * nX)
    walls.append(x + (y+1) * nX)
    walls.append(1 + x + y * (nX+1))
    walls.append(x + y * (nX+1))

    return walls


def getRandomCase(tab):
    index = random.randint(0,len(tab) -1 )
    return [index, tab[index]]




def getCoords(N, nX,nY):
    if N >= 0:
        y=N//nX
        x=N%nX
        return x,y



def getNextCandidat(n, front, cave, verticalWalls, horizontalWalls, nX, nY, badVoisin):
    if len(front) <= 0:
        return [-3]

    if 0 in cave and (nX * nY -1) in cave :
        return [-4]

    nextCandidat = -1
    x, y = getCoords(n,nX,nY)
    neibour= voisins(x,y,nX,nY)

    for bad in badVoisin:
        if bad in neibour:
            neibour = retirer(neibour, bad)

    if len(neibour) == 0:
        return [-2]

    candidats = []
    walls = getWalls(x, y, nX, nY)
    walltoRemove = -1
    index = 0
    findValideNeibour = False
    while len(neibour) > 0 and not findValideNeibour:
        currentNeibour = neibour[random.randint(0, len(neibour))]
        if currentNeibour in front and currentNeibour not in cave:

        else:
            neibour = retirer(neibour, currentNeibour)
    
    for candidat in candidats:
        tmpx, tmpy =getCoords(candidat, nX, nY)
        candidatWalls = getWalls(tmpx, tmpy, nX, nY)
        for index  in range(len(candidatWalls)):
            tmpWall = candidatWalls[index]
            if index < 2:
                tmpVerticalwalls = walls[0:2]
                if tmpWall in tmpVerticalwalls  and tmpWall in verticalWalls:
                    walltoRemove = [index, tmpWall]
                    nextCandidat = candidat

            elif index > 2:
                tmpHorizontalWalls = walls[2:]
                if tmpWall in tmpHorizontalWalls and tmpWall in horizontalWalls:
                    walltoRemove = [index, tmpWall]
                    nextCandidat = candidat
    
    
    print(nextCandidat)
    if nextCandidat!= -1:
        return [nextCandidat, walltoRemove[0], walltoRemove[1]]
    else:
        return [-1]




            
def laby(nX, nY, largeurCase):
    front = iota(nX*nY )
    cave = []
    horizontalWalls = iota(nX * nY -1)
    verticalWalls = iota(nY * nX -1)
    horizontalWalls.pop(0) # setting the entrance of the laby
    horizontalWalls.pop(-1) # setting the exit of the laby
    removedHorizontalWalls = []
    removedVerticalWalls = []
    currentCase = getRandomCase(front)
    previousCase = currentCase
    x, y = getCoords(currentCase[1], nX, nY)
    currentCaseWalls = getWalls(x,y,nX,nY)
    nextRemove = voisins(x, y, nX, nY)
    wallToRemove = getRandomCase(currentCaseWalls)
    if wallToRemove[0] < 2:
        verticalWalls = retirer(verticalWalls, wallToRemove[1])
        removedVerticalWalls = ajouter(removedVerticalWalls, wallToRemove[1])
    else:
        horizontalWalls = retirer(horizontalWalls, wallToRemove[1])
        removedHorizontalWalls = ajouter(removedHorizontalWalls, wallToRemove[1])
        
        
    cave = ajouter(cave, currentCase[1])
    front = retirer(front, currentCase[1])

    # getting the new case that is a part of the cave
    for candidat in nextRemove:
        tmpx, tmpy = getCoords(candidat, nX, nY)
        tmpWalls = getWalls(tmpx, tmpy, nX, nY)
        if wallToRemove[1]  in tmpWalls:
            previousCase = currentCase
            currentCase[0] = front.index(candidat)
            currentCase[1] = candidat
            currentCaseWalls = tmpWalls
            currentCaseWalls = retirer(currentCaseWalls , wallToRemove[1])
            front = retirer(front, candidat)
            cave = ajouter(cave, candidat)
            break

    finish = False
    badVoisins = []
    while not finish:
        result = getNextCandidat(currentCase[1],front,cave, verticalWalls, horizontalWalls, nX, nY, badVoisins)
        print(result)

        if result[0] < -2:
            print("soucis ou fin : ", result)
            finish = True

        elif result[0] == -1:
            badVoisins.append(currentCase[1])
            # next()
            # cave = retirer(cave, currentCase[1])
            # front = ajouter()
            # result = getNextCandidat(currentCase[1],front,cave,verticalWalls,horizontalWalls,nX,nY,badVoisin)
            print("aucun voisin trouver")
            # finish = True

        else:
            if result[1] < 2:
                verticalWalls = retirer(verticalWalls, result[2])
            elif result[1] > 2:
                horizontalWalls = retirer(horizontalWalls, result[2])

            previousCase = currentCase
            currentCase[0] = front.index(result[0])
            currentCase[1] = result[0]
            front = retirer(front, result[0])
            cave = ajouter(cave, result[0])
            badVoisins = []














    print("have to draw now")
    print(cave.sort())
    print(len(cave))
    print(front)
    print(verticalWalls)
    print(horizontalWalls)

# laby(3, 3, 20)