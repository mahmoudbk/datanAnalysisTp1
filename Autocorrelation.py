import numpy as np
#from scipy import arange
import math

def autocorr(x):
    "Calcule l'autocorrÃ©lation d'un signal"
    x = x-np.nanmean(x)
    result = np.correlate(x, x, mode='full')/np.sum(x**2)
    result = result[result.size // 2:]
    tau = np.arange(0, len(result), 1)
    return tau, result

def autocorr_lisse(x, Nfft):
    "x est la moyenne de vitesse et Nfft est le nombre de points voulu par Ã©chantillon"
    "Plus stable que autocorr, Ã  privilÃ©gier"
    x = x-np.nanmean(x)
    N = math.floor(len(x)/Nfft)
    R = []
    for k in range(N):
        debut = k*Nfft 
        fin = Nfft*(k+1)
        result = np.correlate(x[debut:fin], x[debut:fin], mode='full')/np.sum(x[debut:fin]**2)
        result = result[int(len(result)/2)::]
        R.append(result)
    result = np.mean(R, axis=0)
    tau = np.arange(0, len(result), 1)
    return tau, result
