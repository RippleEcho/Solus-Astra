import random
import math
from star import star

#Run this file to gen solar systems
c=[0.08,  0.45,  0.80,  1.04,  1.40,  2.10,  16.0,  150]
r=[0.0000,0.7656,0.8866,0.9626,0.9926,0.9986,0.9999,1.0000]
m=[0,0,0,0,0,0,0]
b=[0.08,0,0,0,0,0,0]
for i in range (7):
    m[i]=(c[i+1]-c[i])/(r[i+1]-r[i])
for j in range (6):    
    b[j+1]=r[j+1]*(m[j]-m[j+1])+b[j]

def Mass(x):
    s=0
    while(x>=r[s]):
        s+=1
    s-=1
    ms=m[s]
    bs=b[s]
    u=(x*ms)+bs
    return u #in solar masses

hab=0
tot=100

#How many to gen
Sca=["M","K","G","F","A","B","O"]
ScH=[0,0,0,0,0,0,0]
ScC=[0,0,0,0,0,0,0]
ScP=[0,0,0,0,0,0,0]
for i in range (tot):
    Sys=[]
    #x=random.random()
    x=random.uniform(0.75,1.0)      #Range 0.0 to 0.7 returns only M, naturally
    #s=star(Mass(0.9036))           #shortcut for Sol
    s=star(Mass(x))
    Sys.append(s)
    while(len(Sys)<4):
        C=0.03*math.exp(x*3)+0.2
        if(C>random.random()):
            x=random.uniform(0.0,1)
            Sys.append(star(Mass(x)))
        else:
            break
    sar=[]
    for a in Sys:
        sar.append(a.sc)
    print(sar)
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
if(False):
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
