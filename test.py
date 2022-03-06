from izzy_ckis import izzy_ckis
from delsarte_pkis import delsarte_pkis
from sympy import *

n=3
izzy = izzy_ckis(n)
delsarte = delsarte_pkis(n)


i = 0

while i < len(izzy):
    j = 0
    while j < len(izzy[0]):
        print(simplify((izzy[i][j] - delsarte[i][j])))
        j+=1
    i+=1