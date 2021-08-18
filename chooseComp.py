import fourOFaKind
import threeOFaKind
import fiveOFaKind
  
#stores 3OK data
results3=[]
#stores 4OK data
results4=[]
#stores 5OK data
results5=[]
#choses whether I want to see the prob, weighted EV, or unweighted EV
ind=2

#going through all 6 die values
for c in range (1,7):
    #going though the number of matching dice values in first roll to get 3OK
    for a in range (1, 4):
        #adding up results for 3,4 and 5OK, since all three results can be scored in 3OK category
        results3.append([a,c, threeOFaKind.ThreeOfAKind1(a,c)[ind]+fourOFaKind.FourOfAKind1(a,c)[ind]+fiveOFaKind.FiveOfAKind1(a,c)[ind]])
    #going though the number of matching dice values in first roll to get 4OK       
    for y in range (1,5):
        #adding up results for 4 and 5OK, since both results can be scored in 4OK category
        results4.append([y,c, fourOFaKind.FourOfAKind1(y,c)[ind]+fiveOFaKind.FiveOfAKind1(y,c)[ind]])
    #going though the number of matching dice values in first roll to get 5OK    
    for x in range (1,6):
        results5.append([x,c, fiveOFaKind.FiveOfAKind1(x,c)[ind]])
        
if __name__ == '__main__':        
    print (results3)
    print (results4)
    print (results5)
    #total unweighted EV of 3OK
    exVal3=threeOFaKind.ThreeOfAKind()[2]+fourOFaKind.FourOfAKind()[2]+fiveOFaKind.Yahtzee()[1]
    #total prob of scoring 3OK
    prob3=threeOFaKind.ThreeOfAKind()[0]+fourOFaKind.FourOfAKind()[0]+fiveOFaKind.Yahtzee()[0]
    #total unweighted EV of 4OK
    exVal4=fourOFaKind.FourOfAKind()[2]+fiveOFaKind.Yahtzee()[1]
    #total prob of scoring 4OK
    prob4=fourOFaKind.FourOfAKind()[0]+fiveOFaKind.Yahtzee()[0]
    print(exVal3, exVal3/prob3)
    print(exVal4, exVal4/prob4)
