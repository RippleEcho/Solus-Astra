import random
import math

class planet:
    def __init__(self, smaj, ecc, SL, SM, PT):
        
        self.a=smaj
        #Distance from star in AU

        self.e=ecc
        #orbital eccentricity

        self.pt=PT
        self.planet_type()
        #Planetary type pair

        self.sm=SM
        #Stellar Mass in Msol

        self.sl=SL
        #Stellar Luminance in Lsol

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
        if(self.pt[1]=='E'):
            #0.95<self.pl<=1.37 and 
            Lp=self.pl
            if(1>self.pl):
                Lp=1.0/self.pl
            self.hs=10-(20*(Lp-1))
            if(self.a>0.5):
                self.hs*=0.5
            if(self.hs>-10):
                self.h=True
        #Habitability Score: 10 is perfect Lower is worse
            #print(self.pt[1],round(self.pl,3))
        
    def planet_type(self):
        #Here be monsters
        if(self.pt[1]=='G'):            #Gas
            if(self.pt[0]==0):
                self.pt[1]='S'          #Super Jovian
                if(random.random()<0.5):
                    self.pt[1]='H'      #Hot Jovian
            elif(self.pt[0]==1):
                self.pt[1]='S'          #Super Jovian
            elif(self.pt[0]==2):
                self.pt[1]='S'          #Super Jovian
                if(random.random()<0.6):
                    self.pt[1]='J'      #Classical Jovian
            elif(self.pt[0]==3):
                self.pt[1]='I'          #Ice Giant (Neptunian?)
                if(random.random()<0.2):
                    self.pt[1]='J'      #Classical Jovian
            else:
                self.pt[1]='I'          #Ice Giant 
        if(self.pt[1]=='T'):            #Terrestrial
            if(self.pt[0]==0 or self.pt[0]==1):
                self.pt[1]='E'          #"Earth-like"
                if(random.random()<0.5):
                    self.pt[1]='D'      #Dwarf
            else:
                self.pt[1]='L'          #Low-density AKA mini neptune
                if(random.random()<0.5):
                    self.pt[1]='E'      #"Earth-like"
                    if(random.random()<0.5):
                        self.pt[1]='D'  #Dwarf

            #The whole above mess is to be reworked into a table
#TODO orbital parameters
#TODO planet parameters
