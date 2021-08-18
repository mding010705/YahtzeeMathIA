import fourOFaKind
import threeOFaKind
import fiveOFaKind
  


results3=[]
results4=[]
results5=[]
ind=2
for c in range (1,7):
    for a in range (1, 4):
        results3.append([a,c, threeOFaKind.ThreeOfAKind1(a,c)[ind]+fourOFaKind.FourOfAKind1(a,c)[ind]+fiveOFaKind.FiveOfAKind1(a,c)[ind]])
            
    for y in range (1,5):
        results4.append([y,c, fourOFaKind.FourOfAKind1(y,c)[ind]+fiveOFaKind.FiveOfAKind1(y,c)[ind]])
        
    for x in range (1,6):
        results5.append([x,c, fiveOFaKind.FiveOfAKind1(x,c)[ind]])
        
if __name__ == '__main__':        
    print (results3)
    print (results4)
    print (results5)
    exVal3=threeOFaKind.ThreeOfAKind()[2]+fourOFaKind.FourOfAKind()[2]+fiveOFaKind.Yahtzee()[1]
    prob3=threeOFaKind.ThreeOfAKind()[0]+fourOFaKind.FourOfAKind()[0]+fiveOFaKind.Yahtzee()[0]
    exVal4=fourOFaKind.FourOfAKind()[2]+fiveOFaKind.Yahtzee()[1]
    prob4=fourOFaKind.FourOfAKind()[0]+fiveOFaKind.Yahtzee()[0]
    print(exVal3, exVal3/prob3)
    print(exVal4, exVal4/prob4)
