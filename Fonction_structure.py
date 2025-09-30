import numpy as np

def structure_f(a,n, maxlag) : 
    # Calcule la fonction structure d'ordre n pour le vecteur 1D appelÃ© a.
    # maxlag = espacement maximum entre deux points
    nn = len(a)
    s = np.zeros(maxlag)
    for i in range(1,maxlag):
        b1 = a[0:nn-i]
        b2 = a[i:nn]
        s[i] = np.mean((b1-b2)**n)
    return s
