# @author :
# @ Culpin Alexis
# @ Edwin Ganmavo
# This program is built to be a library that help you building a
# labyrinthes


###############################################################################

# Import
from math import hypot
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
#  [north, south, ouest, est]
#  if a wall should not exist, is value is -1
# @param
# @x, the x coords of our case
# @y, the y coords of our case
# @nX, the width of our grid
# @nY, the hight of our grid
def getWalls(n, nX,nY):
    walls = {}
    x, y = getCoords(n,nX,nY)

    walls["N"] = x + y * nX
    walls["S"] = x + (y+1) * nX
    walls["E"] = 1 + x + y * (nX+1)
    walls["O"] = x + y * (nX+1)

    return walls


def getRandomCase(tab):
    index = random.randint(0,len(tab) -1 )
    return [index, tab[index]]




def getCoords(N, nX,nY):
    if N >= 0:
        y=N//nX
        x=N%nX
        print("get coords : n = " + str(N) + " x = " + str(x) + " y = " + str(y))
        return x,y


def addWallsToCavity(caseWalls, horizontalWalls, verticalWalls, removedHorizontalWalls , removedVerticalWalls):
    if not caseWalls["N"] in verticalWalls and not caseWalls["N"] in removedVerticalWalls:
        verticalWalls.append(caseWalls["N"])
    if not caseWalls["S"] in verticalWalls and not caseWalls["S"] in removedVerticalWalls:
        verticalWalls.append(caseWalls["S"])

    if not caseWalls["E"] in horizontalWalls and not caseWalls["E"] in removedHorizontalWalls:
        horizontalWalls.append(caseWalls["E"])

    if not caseWalls["O"] in horizontalWalls and not caseWalls["O"] in removedHorizontalWalls:
        horizontalWalls.append(caseWalls["O"])

    return (horizontalWalls,verticalWalls)

def removeRandomWall(caseWalls, horizontalWalls, verticalWalls, removedHorizontalWalls , removedVerticalWalls):
    hCandidat = []
    vCandidat = []
    if caseWalls["N"] in verticalWalls and not caseWalls["N"] in removedVerticalWalls:
        vCandidat.append(caseWalls["N"])
    if caseWalls["S"] in verticalWalls and not caseWalls["S"] in removedVerticalWalls:
        vCandidat.append(caseWalls["S"])

    if caseWalls["E"] in horizontalWalls and not caseWalls["E"] in removedHorizontalWalls:
        hCandidat.append(caseWalls["E"])

    if caseWalls["O"] in horizontalWalls and not caseWalls["O"] in removedHorizontalWalls:
        hCandidat.append(caseWalls["O"])

    if len(hCandidat) > 0 and len(vCandidat) > 0:
        vOrH = random.randint(0,1)
        if vOrH == 0 :
            chosenWall = vCandidat[random.randint(0, len(vCandidat)-1)]
            removedVerticalWalls.append(chosenWall)
            verticalWalls.remove(chosenWall)
        elif vOrH == 1:
            chosenWall = hCandidat[random.randint(0, len(hCandidat)-1)]
            removedHorizontalWalls.append(chosenWall)
            horizontalWalls.remove(chosenWall)

    elif len(vCandidat) > 0 and len(hCandidat) == 0:
        chosenWall = vCandidat[random.randint(0, len(vCandidat)-1)]
        removedVerticalWalls.append(chosenWall)
        verticalWalls.remove(chosenWall)

    elif len(vCandidat) == 0 and len(hCandidat) >0:
        chosenWall = hCandidat[random.randint(0, len(hCandidat)-1)]
        removedHorizontalWalls.append(chosenWall)
        horizontalWalls.remove(chosenWall)

    return (horizontalWalls, verticalWalls, removedHorizontalWalls, removedVerticalWalls)




def laby(nX, nY, largeurCase):
    front = []
    cave = []
    horizontalWalls = iota(nX*(nY+1))
    verticalWalls = iota((nX+1)*nY)
    horizontalWalls.pop(0) # setting the entrance of the laby
    horizontalWalls.pop(-1) # setting the exit of the laby
    x = random.randint(0, nX*nY-1)
    y = random.randint(0, nX*nY-1)
    case = getCaseNumber(x, y, nX, nY)
    caseWalls = getWalls(case,nX,nY)
    cave = ajouter(cave, case)
    caveHorizontalWalls = []
    caveVerticalWalls = []
    removedHorizontalWalls = []
    removedVerticalWalls = []
    caveHorizontalWalls, caveVerticalWalls = addWallsToCavity(caseWalls, caveHorizontalWalls, caveVerticalWalls, removedHorizontalWalls , removedVerticalWalls)
    print(x)
    print(y)
    print(case)

    finish = False
    while not finish:
        neighbours = voisins(x,y,nX,nY)
        for voisin in neighbours:
            if voisin not in cave and voisin not in front:
                front = ajouter(front, voisin)
                # print(front)

        case= front[random.randint(0, len(front) - 1)]
        x,y = getCoords(case,nX,nY)
        caseWalls = getWalls(case,nX,nY)
        caveHorizontalWalls, caveVerticalWalls = addWallsToCavity(caseWalls, caveHorizontalWalls, caveVerticalWalls, removedHorizontalWalls, removedVerticalWalls)
        caveHorizontalWalls, caveVerticalWalls, removedHorizontalWalls, removedVerticalWalls = removeRandomWall(caseWalls, caveHorizontalWalls, caveVerticalWalls, removedHorizontalWalls, removedVerticalWalls)
        cave = ajouter(cave, case)
        front = retirer(front, case)
        # cave = ajouter(cave, case)

        if len(front) == 0:
            print("soucis la je crois")
            print(nX * nY)
            print(cave)
            finish = True




    print("have to draw now")
    # print(cave.sort())
    print(len(cave))
    print(len(front))
    print(cave)
    print(front)
    print(caveVerticalWalls)
    print(caveHorizontalWalls)
    print(removedHorizontalWalls)
    print(removedVerticalWalls)
    # print(verticalWalls)
    # print(horizontalWalls)
    print(getWalls(10,3,3))

laby(3, 3, 20)