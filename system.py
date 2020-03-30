import random
import math
from star import star
class system:
    def __init__(self):
        #generate solar system
        self.STARS=[]
        self.star_gen()
    def star_gen(self):
        
        #generate first, heaviest star
        x=random.uniform(0.75,1.0)
        self.STARS.append(star(self.star_mass(x)))

        #determine stellar multiplicity, and add those stars
        while(len(self.STARS)<4):
            
            C=0.03*math.exp(x*3)+0.2
            if(C>random.random()):
                #next star will be less massive than previous
                x=random.uniform(0,x)
                self.STARS.append(star(self.star_mass(x)))
            else:
                break
        
        #determine stellar orbits
        #determine parameters for planets, etc
        self.a=1
    def star_mass(self,x):
        #input x range (0-1), outputs stellar mass in units of Msol
        #uses piece-wise linear functions instead of continuous power-laws
        #linear because am NOT I going to tune that power function well
        
        #slope estimations for piece-wise initial-mass function
        m= [925/1914, 350/121, 60/19, 12, 5833/50, 139000/13, 1340000]

        #y-int estimations for piece-wise initial-mass function
        b= [2/25, -1941/1100, -9499/4750, -13139/1250, -34321/300, -1387781/130, -1339850]

        #bins for mass function and also later stellar classification
        r=[0.0000, 0.7656, 0.8866, 0.9626, 0.9926, 0.9986, 0.9999, 1.0000]
        
        s=0
        #determine which bin input x falls into
        while(x>=r[s]):
            s+=1
        s-=1
        #retrieve slope and y-int
        ms=m[s]
        bs=b[s]
        
        #calculate stellar mass 
        u=(x*ms)+bs
        return u #in solar masses
