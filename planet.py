import random
import math

class planet:
    def __init__(self, smaj, ecc, SL, SM, PB):
        
        self.a=smaj
        #Distance from star in AU

        self.e=ecc
        #orbital eccentricity

        self.pb=PB
        self.pt='N'
        self.planet_type()
        #Planetary type pair

        self.sm=SM
        #Stellar Mass in Msol

        self.sl=SL
        #Stellar Luminosity in Lsol

        self.p=math.sqrt(pow(self.a,3)/self.sm)
        #Orbital Period in Year
        
        self.pl=self.sl/pow(self.a,2)
        #Planetary Luminosity at SMaj, in Lsol
        

        self.fl=math.sqrt(self.sl)*4.85
        #Stellar frostline in AU

        self.f=False
        if(self.a>self.fl):
            self.f=True
        #Boolean. True if dist>frostline

        self.h=False
        self.hs=0
        if(self.pt=='E'):
            #0.95<self.pl<=1.37 and 
            Lp=self.pl
            if(1>self.pl):
                Lp=1.0/self.pl
            #Normalize Planet Lum to less than 1
            #Score against PL=1.0
            self.hs=10-(20*(Lp-1))
            if(self.a<0.5):
                self.hs-=1.0
                self.hs*=0.5
            #Penalty for close-orbit planets due to Tidal Lock
                
            if(self.sl>1 and self.hs>1):
                #self.hs-=1.0
                self.hs/=(math.log(self.sl))

            #Penalty for higher mass stars due to UV output
                
            if(self.hs>1):
                self.h=True
        #Habitability Score: 10 is perfect Lower is worse
            #print(self.pt[1],round(self.pl,3))
        
    def planet_type(self):
        cat=['H','S','J','I','D','E','L','A']
        PCG=[[4, 0, 0, 0, 0],     #H
             [3, 5, 5, 1, 0],     #S
             [1, 3, 3, 1, 0],     #J
             [0, 0, 0, 6, 8],     #I
             [4, 3, 3, 2, 0],     #D
             [4, 4, 3, 3, 0],     #E
             [0, 1, 1, 2, 0],     #A
             [0, 0, 1, 1, 8]]     #L
        #Type weights in arbitrary units
        ColSum = 0
        CatArr = []
        for e in range(len(PCG)):
            ColSum+=PCG[e][self.pb]
            #sum prob weights by distance band
            for f in range(PCG[e][self.pb]):
                CatArr.append(cat[e])
            #produce a str list, each type counted by weight in PCG
        self.pt=random.choice(CatArr)
            #pick randomly from list 


#TODO orbital parameters
#TODO planet parameters
