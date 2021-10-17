def iota(n):
    if n >= 0:
        return range(n)
    else:
        print("error, n must be a negative Integer")

def contient(tab, x):
    return x in tab

def ajouter(tab, x):
    if x >= 0 and not x in tab:
        tab.append(x)
        return tab
    else:
        print("error, x must be a positive integer and not already included in tab, nothing added")
        return tab

def retirer(tab, x):
    if x in tab:
        del tab[tab.index(x)]
        return tab
    else:
        print("error, x must be in tab, nothing have been deleted")
        return tab

