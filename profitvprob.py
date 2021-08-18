import matplotlib.pyplot as plt
import UpperSection as US
import fiveOFaKind as fvok
import fourOFaKind as frok
import threeOFaKind as tok

#gives appropriate US target score based of roll, r, and its probability of being achieved
def USScores(r):
    scores=[0,0,0,0,0,0]
    pscores=[0,0,0,0,0,0]
    for j in range (len(scores)):
        for i in range (len(r)):
            #adds up each number, j+1, of r into the j+1th element of scores
            if j+1==r[i]:
                scores[j]+=r[i]
    for k in range (len(scores)):
        #if less than 3OK of number, goal score is 3OK
        if scores[k]<=3*k+3 and scores[k]!=0:
            pscores[k]=3*(k+1)
            pscores[k]+=((3*(k+1))/63)*35
        #if greater than 3OK of number, goal score is however many of a kind there already are
        elif scores[k]>3*(k+1):
            pscores[k]=scores[k]
            pscores[k]+=((scores[k]/63)*35)
            
    probs=[0,0,0,0,0,0];          
    for x in range (len(pscores)):
        if pscores[x]!=0:
            #if more than 3OK
            if r.count(x+1)>3:
                for y in range (r.count(x+1),6):
                    for z in range (0,6):
                        for a in range (0,6):
                            if (scores[x]/(x+1))+z+a==y:
                                #takes possible other 2 number matching dice (always zero in this case) to achieve desired number of matching dice and finds the associated prob
                                probs[x]+= US.p12((scores[x]/(x+1)), z, a)
            #if less than 3OK
            elif r.count(x+1)<=3:
                for y in range (3,6):
                    for z in range (0,6):
                        for a in range (0,6):
                            if (scores[x]/(x+1))+z+a==y:
                                #takes possible other 2 number matching dice to achieve 3 matching dice and finds the associated prob
                                probs[x]+= US.p12((scores[x]/(x+1)), z, a)
    return (pscores, probs);

def yahtzeeScore(a,r):
    score=0
    if a=='y':
        #if Yahtzee previously scored, this Yahtzee will be worth bonus
        score=100
    elif a=='n':
        #if Yahtzee not previously score, Yahtzee worth 50 pts
        score=50
    
    #counting up number of matching values
    tally=[0]*6
    for i in range (len(tally)):
        tally[i]=r.count(i+1)
    
    #takes the largest number of matching dice values and finds the prob a getting Yahtzee from the number of matching dice
    y=max(tally)
    prob=fvok.FiveOfAKind1(y, 1)[0]
    return (score,prob)

#counts up number of matching dice per value and gives weighted EV for the value and prob of achieving weighted EV given that number of matching dice
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
    



