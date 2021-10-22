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
def getWalls(x,y,nX,nY):
    walls = []
    walls.append(x + y * nX)
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



def laby(nX, nY, largeurCase):
    front = iota(nX*nY )
    cave = []
    horizontalWalls = iota(nX * nY -1)
    verticalWalls = iota(nY * nX -1)
    horizontalWalls.pop(0) # setting the entrance of the laby
    horizontalWalls.pop(-1) # setting the exit of the laby
    currentCase = getRandomCase(front)
    x, y = getCoords(currentCase[1], nX, nY)
    currentCaseWalls = getWalls(x,y,nX,nY)
    nextRemove = voisins(x, y, nX, nY)
    wallToRemove = getRandomCase(currentCaseWalls)
    if wallToRemove[0] < 2:
        verticalWalls = retirer(verticalWalls, wallToRemove[1])
    else:
        horizontalWalls = retirer(horizontalWalls, wallToRemove[1])
        
        
    cave = ajouter(cave, currentCase[1])
    front = retirer(front, currentCase[1])

    # getting the new case that is a part of the cave
    for candidat in nextRemove:
        tmpx, tmpy = getCoords(candidat, nX, nY)
        tmpWalls = getWalls(tmpx, tmpy, nX, nY)
        if wallToRemove[1]  in tmpWalls:
            print(front.index(candidat))
            currentCase[0] = front.index(candidat)
            currentCase[1] = candidat
            currentCaseWalls = tmpWalls
            currentCaseWalls = retirer(currentCaseWalls , wallToRemove[1])
            front = retirer(front, candidat)
            cave = ajouter(cave, candidat)
            break

    
    while len(front) > 0:
        # print("la cave vaux : ", cave)
        # print("la front vaux : ", front)
        # print("la case courrante est : ", currentCase)
        x, y = getCoords(currentCase[1],nX, nY)
        # print("les coordonée de cette case sont : ", [x,y])
        nextRemove = voisins(x, y, nX, nY)
        # print("les candidats potentiels sont : ", nextRemove)
        findCandidat = False
        while not findCandidat and len(nextRemove) > 0:
            candidat = getRandomCase(nextRemove)
            # print("la liste de candidat à une taille de :", len(nextRemove))
            # print("le candidat courrant est : ", candidat)

            # checking if the potential candidat is not already in the cave
            if not candidat[1] in cave and candidat[1] in front:
                # print("le candidat n'est pas dans la cave")
                tmpx, tmpy = getCoords(candidat[1], nX, nY)
                # print("les coords du candidats sont : ", [x,y])



                # getting the wall to remove
                candidatWalls= getWalls(tmpx, tmpy, nX, nY)
                wallToRemove = -1
                for wallIndex in range(len(candidatWalls)):
                    if candidatWalls[wallIndex] in currentCaseWalls:
                        wallToRemove = [wallIndex, candidatWalls[wallIndex]]
                        break

                if wallToRemove != -1:
                    # print("test passé")
                    if wallToRemove[0] < 2:
                        # print("supression du mure verticale")
                        verticalWalls =retirer(verticalWalls, wallToRemove[1])
                    else:
                        # print("supression du mure horizontale")
                        horizontalWall = retirer(horizontalWalls,wallToRemove[1])



                    currentCase[0] = front.index(candidat[1])
                    currentCase[1] = candidat[1]
                    currentCaseWalls = candidatWalls
                    # print("retirer walls")
                    currentCaseWalls= retirer(currentCaseWalls, wallToRemove[1])
                    cave = ajouter(cave, candidat[1])
                    # print("retirer front")
                    front = retirer(front, candidat[1])
                    findCandidat = True
                else:
                    # print("aucun mure en commun")
                    nextRemove = retirer(nextRemove, candidat[1])
                    

            # if the candidat is already in the cave, go to the next one
            else:
                # print("retirer pas deja dans cave")
                nextRemove = retirer(nextRemove, candidat[1])










    print("have to draw now")
    print(cave.sort())
    print(len(cave))
    print(front)
    print(verticalWalls)
    print(horizontalWalls)



laby(3,4,20)