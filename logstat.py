import math
import random
class logstat:
    def __init__(self):
        self.a=0

    def L_K(L):
        return round(1000*L)

    def K_L(K):
        return K/1000.0

    def L_E(L):
        return math.power(2,L)

    def E_L(E):
        return math.log(E,2)

    def E_S(E):
        if(E>1):
            return 1.0-(1.0/E)
        else:
            return E-1.0

    def S_P(S):
        return (S+1.0)/2.0

    def E_P(E):
        return S_P(E_S(E))

    
