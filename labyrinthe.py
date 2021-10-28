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
    if x in tab:
        del tab[tab.index(x)]
        return tab
    else:
        print("error, x must be in tab, nothing have been deleted")
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
        if x-1 >= 0 and x-1 < nX and y < nY:
            list.append((x-1) + y*nX)
        
        if y-1 >= 0 and y-1 <nY and x < nX:
            list.append(x + (y - 1) * nX)

        if y+1 < nY and x < nX:
            list.append(x+(y+1)*nX)

        if x+1 < nX and y < nY:
            list.append((x + 1) + y * nX)
    
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
#  this function return a dictionnary containing the number of the wall of a case
#  [north, south, ouest, est]
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

# function getCoords
# this function return the x,y coordinate of a case
# @param,
# @n, the number of the case
# @nX, the width of the laby
# @nY, the hight of the laby
def getCoords(n, nX, nY):
    #  validating the case number
    if n >= 0 and n < nX*nY:
        y=n//nX
        x=n%nX
        return x,y

    else:
        return -1

# function addWallsToCavity
# this function add a walls to the cavity, if they are not already in
# or if they haven't been already removed
# and return the modified list
# @param
# @caseWalls, tha list of wall of our case
# @horizontalWalls, the list of horizontal walls in the cavity 
# @verticalWalls, the list of vertical walls in the cavity 
# @removedHorizontalWalls , the list of already removed horizontal walls in the cavity
# @removedVerticalWalls, the list of already removed verticalwalls in the cavity
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

# function removeRandomWall
# this function remove a random wall to link the case to the cavity
#  this function return the list of wall once modified
# @param
# @caseWalls, tha list of wall of our case
# @horizontalWalls, the list of horizontal walls in the cavity 
# @verticalWalls, the list of vertical walls in the cavity 
# @removedHorizontalWalls , the list of already removed horizontal walls in the cavity
# @removedVerticalWalls, the list of already removed verticalwalls in the cavity
def removeRandomWall(caseWalls, horizontalWalls, verticalWalls, removedHorizontalWalls , removedVerticalWalls):
    hCandidat = []
    vCandidat = []
    # validating the vertical candidat
    if caseWalls["N"] in verticalWalls and not caseWalls["N"] in removedVerticalWalls:
        vCandidat.append(caseWalls["N"])
    if caseWalls["S"] in verticalWalls and not caseWalls["S"] in removedVerticalWalls:
        vCandidat.append(caseWalls["S"])
    # validating the horizontal candidats
    if caseWalls["E"] in horizontalWalls and not caseWalls["E"] in removedHorizontalWalls:
        hCandidat.append(caseWalls["E"])

    if caseWalls["O"] in horizontalWalls and not caseWalls["O"] in removedHorizontalWalls:
        hCandidat.append(caseWalls["O"])
    # checking how many candidat have been found, in order to make the corect selection
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



# def laby
# this function generate and draw a laby of size nX*nY, and where the width of case
# largeurCase
# this laby is sure to have an entrance and an exit
# @param
# @nX, the width (number of case) of our laby
# @nY, the hight (number of case) of our laby
# @largeurCase, the width (in pixel) for a case of our laby 
def laby(nX, nY, largeurCase):
    front = []  # group of neighbour of the cavity
    cave = [] # our cavity

    # generating random coordinate for our initial cavity
    x = random.randint(0, nX-1)
    y = random.randint(0, nY-1)
    case = getCaseNumber(x, y, nX, nY)
    caseWalls = getWalls(case,nX,nY)
    cave = ajouter(cave, case)
    caveHorizontalWalls = []
    caveVerticalWalls = []
    removedHorizontalWalls = []
    removedVerticalWalls = []
    caveHorizontalWalls, caveVerticalWalls = addWallsToCavity(caseWalls, caveHorizontalWalls, caveVerticalWalls, removedHorizontalWalls , removedVerticalWalls)

    #  setting the entrance and exit of the laby
    caveHorizontalWalls = ajouter(caveHorizontalWalls,0)
    caveHorizontalWalls = ajouter(caveHorizontalWalls, (nX*(nY+1) -1))
    removedHorizontalWalls = ajouter(removedHorizontalWalls,0)
    removedHorizontalWalls = ajouter(removedHorizontalWalls,(nX*(nY+1) -1))
    # main loop to built our cavity
    while len(cave) < (nX*nY) :

        #  getting the neighbours of our last member of the cavity
        neighbours = voisins(x,y,nX,nY)
        for voisin in neighbours:
            # checking if the neighbour is a new one and not a part of the cavity
            if not contient(front, voisin) and not contient(cave, voisin) :
                front = ajouter(front, voisin)

        # checking the number of lasting neighbour, to apply the correct operation
        if len(front) > 1:
            case= front[random.randint(0, len(front) - 1)]
        elif len(front) == 1:
            case = front[0]
        # creating our new entrance in the cavity, removing it from the front, and removing the walls to link it to the cavity
        x,y = getCoords(case,nX,nY)
        caseWalls = getWalls(case,nX,nY)
        caveHorizontalWalls, caveVerticalWalls = addWallsToCavity(caseWalls, caveHorizontalWalls, caveVerticalWalls, removedHorizontalWalls, removedVerticalWalls)
        caveHorizontalWalls, caveVerticalWalls, removedHorizontalWalls, removedVerticalWalls = removeRandomWall(caseWalls, caveHorizontalWalls, caveVerticalWalls, removedHorizontalWalls, removedVerticalWalls)
        cave = ajouter(cave, case)
        front = retirer(front, case)

    print("have to draw now")

laby(3, 3, 20)