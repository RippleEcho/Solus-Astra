import random
import math
from star import star

#Run this file to gen solar systems

def Mass (x):
    a = 2.3
    b = 1.4
    ia = (1.0/(1-a))
    ib = (1.0/(1-b))
    u=0.2
    Gmu=0.9999
    Gml=0.5289
    m=u*(((((x*(Gmu-Gml))+Gml)**ib)-1)**ia)
    return m #in Solar mass



#s.printout()

hab=0
tot=100000
#How many to gen
Sca=["M","K","G","F","A","B","O"]
ScH=[0,0,0,0,0,0,0]
ScC=[0,0,0,0,0,0,0]
ScP=[0,0,0,0,0,0,0]
for i in range (tot):

    x=random.random()
    #x=random.uniform(0.75,1.0)      #Range 0.0 to 0.7 returns only M, naturally
    #s=star(Mass(0.9036))           #shortcut for Sol
    s=star(Mass(x))
    hb=s.check_hab()
    if(s.h and False):
        print("")
        print("Mass " + str(round(s.m,3))+" "+s.sc)
        print("Age: " + str(s.a) + " Gy")
        print("Temp " + str(s.t) +" K")
        #print("Dist(AU),Lumin(~E)")
        for j in s.p:
            if(j.h):
                print(round(j.a,3), "AU  " , round(j.p,3),"Yr  ",j.pt,round(j.hs,1))
            else:
                print(round(j.a,3), "AU  " , round(j.p,3),"Yr  ",j.pt)

    hs=s.sc[0]
    hi=Sca.index(hs)
    if(hb):
        ScH[hi]+=1
        hab+=1
    ScC[hi]+=1
for i in range(len(ScC)):
    if(ScC[i]==0):
        ScP[i]=0
    else:
        ScP[i]=round(float(100*ScH[i]/ScC[i]),2)
fra=float(hab/tot)
for u in range(len(Sca)):
    print(Sca[u] +": "+ str(ScH[u])+'/'+str(ScC[u]) +' = '+str(ScP[u])+'%')
#print(Sca)
#print(ScH)
#print(ScC)
#print(ScP)
#print(fra)


