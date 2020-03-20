import random
import math
from planet import planet
class star:
    def __init__(self,mass):
        
        self.m = mass
        #mass in Msol
        
        self.r = mass**(0.740)*random.gauss(1.0,0.01)
        #radius in Rsol
        
        self.t = round(mass**(0.505)*random.gauss(1.0,0.01)*5780)
        #temperature in K
        
        self.l = mass**(3.500)*random.gauss(1.0,0.01)
        #Luminosity in Lsol

        self.s = mass**(-2.50)*random.gauss(1.0,0.01)*10
        #Lifespan in Gy

        self.a=0
        self.star_age()
        #Age in Gy

        self.h = False
        #Habitability

        self.fl=math.sqrt(self.l)*4.85
        #Frostline in AU
      
        self.rhi = round(math.sqrt(self.l)*0.95,3)
        #Inner habitable radius in AU
        
        self.rho = round(math.sqrt(self.l)*1.37,3)
        #Outer habitable radius in AU

        self.rpi = round(self.m*0.1,3)
        #Inner orbital radius in AU
        
        self.rpo = round(self.m*60,3)
        #Outer orbital radius in AU

        self.p=[]
        #Planets array

        self.cr=[("M",0.07,0.45),
                 ("K",0.45,0.80),
                 ("G",0.80,1.04),
                 ("F",1.04,1.40),
                 ("A",1.40,2.10),
                 ("B",2.10,16.0),
                 ("O",16.0,160)]
        #Stellar class bins by mass in Msol
        
        self.stellar_class()
        self.fill_planets()

    def star_age(self):
        while(self.a>13.5 or (self.a<1.0 and self.a<self.s/10)):
            #Less than the age of the universe
            #Either greater than 10% of its lifespan
            #Or greather than 1 Gy (because M-types)
            self.a = random.random()*(self.s/2)
        self.a=round(self.a,3)
        #age in Gy

    def add_planet(self,smaj):
        #orbital eccentricity
        ecc=abs(random.gauss(0.0,0.01))
        PC="T"
        #'terrrestrial' type"
        PB,GP = 0, 0.3
        if(0.5*self.m<smaj<=self.fl):
            PB,GP = 1, 0.2
        elif(self.fl<smaj<=self.fl+1.2):
            PB,GP = 2, 0.3
        elif(self.fl+1.2<smaj<=self.rpo):
            PB,GP = 3, 0.5
        elif(self.rpo<smaj):
            PB,GP = 4, 0.5
        #Above determines bin for G/T types based on smaj
        #Super Hacky
            
        if(random.random()<GP):
            PC="G"
        #'Gas' type
        PT=[PB,PC]
        p=planet(smaj,ecc,self.l,self.m,PT)
        self.p.append(p)

    def fill_planets(self):
        self.p=[] 
        d_0 = self.rpi*random.uniform(0.25,0.75)
        #start too close to star for planets
        d = d_0
        f=False
        while (d<self.rpo):            
            if(d<self.rpo and d>self.rpi):
                self.add_planet(d)
            m = random.uniform(1.41,2.82)
            d*=m
        #move outward by multiplying radius
            
    def printout(self):
        print('M: ' + str(round(self.m,3)))
        print('L: ' + str(round(self.l,3)))
        print('T: ' + str(round(self.t)))
        for i in self.p:
            print((round(i.a,3),round(i.pl,4),i.f))

    def check_hab(self):
        h=False
        for i in self.p:
            if (i.h):
                h=True
        #Does this star have at least 1 habitable planet?
        return h

    def stellar_class(self):
        self.sc=self.cr[0][0]
        for i in range(len(self.cr)):
            L=self.cr[i][1]
            U=self.cr[i][2]
            #upper and lower mass limits for category
            if(L<self.m<=U):
                self.sc=self.cr[i][0]
                R=(U-L)/10
                D=self.m-L
                C=9
                while(D>(10-C)*R and C!=0):
                    C-=1
                #rough numerical (9-0) determination
                #Currently linear. Should be geometric, I think.
                #Outputs 1 Msol as G1, so meh.
                self.sc += str(C)
            

