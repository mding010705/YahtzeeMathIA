import matplotlib.pyplot as plt
import UpperSection as US
import fiveOFaKind as fvok
import fourOFaKind as frok
import threeOFaKind as tok


def USScores(r):
    scores=[0,0,0,0,0,0]
    pscores=[0,0,0,0,0,0]
    for j in range (len(scores)):
        for i in range (len(r)):
            if j+1==r[i]:
                scores[j]+=r[i]
    for k in range (len(scores)):
        if scores[k]<=3*k+3 and scores[k]!=0:
            pscores[k]=3*(k+1)
            pscores[k]+=((3*(k+1))/63)*35
        elif scores[k]>3*(k+1):
            pscores[k]=scores[k]
            pscores[k]+=((scores[k]/63)*35)
            
    probs=[0,0,0,0,0,0];          
    for x in range (len(pscores)):
        if pscores[x]!=0:
            if r.count(x+1)>3:
                for y in range (r.count(x+1),6):
                    for z in range (0,6):
                        for a in range (0,6):
                            if (scores[x]/(x+1))+z+a==y:
                                probs[x]+= US.p12((scores[x]/(x+1)), z, a)
            elif r.count(x+1)<=3:
                for y in range (3,6):
                    for z in range (0,6):
                        for a in range (0,6):
                            if (scores[x]/(x+1))+z+a==y:
                                probs[x]+= US.p12((scores[x]/(x+1)), z, a)
    return (pscores, probs);

def yahtzeeScore(a,r):
    score=0
    if a=='y':
        score=100
    elif a=='n':
        score=50
    tally=[0]*6
    for i in range (len(tally)):
        tally[i]=r.count(i+1)
        
    y=max(tally)
    prob=fvok.FiveOfAKind1(y, 1)[0]
    return (score,prob)

def TOKscore(r):
    score3=[0]*6
    prob3=[0]*6
    for c in range (1,7):
        if c in r:
            a= r.count(c)
            if a>3:
                a=3
            score3[c-1]=tok.ThreeOfAKind1(a,c)[1]
            prob3[c-1]=tok.ThreeOfAKind1(a,c)[0]+frok.FourOfAKind1(a,c)[0]+fvok.FiveOfAKind1(a,c)[0]
    return (score3,prob3)

def FrOKscore(r):
    score4=[0]*6
    prob4=[0]*6
    for c in range (1,7):
        if c in r:
            a= r.count(c)
            if a>4:
                a=4
            score4[c-1]=frok.FourOfAKind1(a,c)[1]
            prob4[c-1]=frok.FourOfAKind1(a,c)[0]+fvok.FiveOfAKind1(a,c)[0]
    return (score4,prob4)
    



