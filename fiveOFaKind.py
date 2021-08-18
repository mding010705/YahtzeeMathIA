import math

#binomial distribution approach, not accurate
def Y():
    probs=0;
    for y in range(0,6):
        for z in range (0,6):
            for a in range (0,6):
                if y+z+a==5:
                    probs+= p(y, z, a);
    return probs;


def Yahtzee():
    prob=0;
    exVal=0;
    #going through ways for different numbers of matching dice can accumulate a full matching set of 5
    for y in range(0,6):
        for z in range (0,6):
            for a in range (0,6):
                #for if the dice I keep from my first roll are kept throughout my next 2 rolls
                if y+z+a==5:
                    prob+= probabilityA (y,z,a);
                    exVal+= ExValA(y,z,a);
                #for if the dice I keep from my first roll are discarded on my next roll
                if y+z+a>5 and z>y and z<=5-y and z+a==5:
                    prob+=probabilityB (y,z,a);
                    exVal+= ExValB(y,z,a);
                    
    return (prob,exVal);

#given n matching dice of value, val, on the first roll
def FiveOfAKind1(n, val):
    prob=0;
    exVal=0;
    y=n
    for z in range (0,6):
        for c in range (0,6):
            if y+z+c==5:
                prob+=probabilityA2 (y, z)*probabilityA3(y,z,c);
                exVal+=ExValA1(y,z,c,val)
            if y+z+c>5 and z>y and z<=5-y and z+c==5 and y!=0:
                prob+=probabilityB2 (y, z)*probabilityB3(y,z,c)
                exVal+=ExValB1(y,z,c,val)
    return (prob,exVal/prob, exVal);

#choose function
def ncr(n,r):
    f = math.factorial;
    return f(n) // f(r) // f(n-r);

#permutation function
def npr(n,r):
    f = math.factorial
    return f(n) / f(n-r);
 
#for if the dice I keep from my first roll are kept throughout my next 2 rolls
def probabilityA (i, j, k):
    events=[];
    #first roll
    events.append((1/6)**5);
    events.append(ncr(5,i));
    events.append(ncr(6,1));
    if i==1 or i==4 or i==0 or i==5:
        events.append(npr(5,5-i));
    if i==0:
        events.append(6);
    elif i==2:
        events.append(npr(5,5-i)+ncr(5,1)*ncr(4,1));
    elif i==3:
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    #second roll
    if i<5:
        events.append((1/6)**(5-i));
        events.append(ncr(5-i,j));
        if i+j==1 or i+j==4 or i+j==0 or i+j==5:
            events.append(ncr(5,5-i-j));
        if i+j==0:
            events.append(6);
        elif i+j==2:
            events.append(npr(5,5-i-j)+ncr(5,1)*ncr(4,1));
        elif i+j==3:
            events.append(ncr(5,5-i-j-1)+npr(5,5-i-j));
    #third roll
    if i+j<5:
        events.append((1/6)**(5-i-j));
        events.append(ncr(5-i-j,k));
        
    return math.prod(events);

#probabilityA separated into parts for the 3 individual rolls
def probabilityA1 (i):
    events=[];
    events.append((1/6)**5);
    events.append(ncr(5,i));
    events.append(ncr(6,1));
    if i==1 or i==4 or i==0 or i==5:
        events.append(npr(5,5-i));
    elif i==2:
        events.append(npr(5,5-i)+ncr(5,1)*ncr(4,1))
    elif i==3:
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    
    return math.prod(events);
def probabilityA2 (i, j):
    events=[];
    if i<5:
        events.append((1/6)**(5-i));
        events.append(ncr(5-i,j));
        if i+j==1 or i+j==4 or i+j==0 or i+j==5:
            events.append(npr(5,5-i-j));
        if i+j==0:
            events.append(6);
        elif i+j==2:
            events.append(npr(5,5-i-j)+ncr(5,1)*ncr(4,1))
        elif i+j==3:
            events.append(ncr(5,5-i-j-1)+npr(5,5-i-j));
    else:
        events.append(1);

    return math.prod(events);
def probabilityA3 (i, j, k):
    events=[];
    
    if i+j<5:
        events.append((1/6)**(5-i-j));
        events.append(ncr(5-i-j,k));
        events.append(npr(5,5-i-j-k));
        if i+j==0:
            events.append(6);
    else:
        events.append(1);
    
    return math.prod(events);
 
#for if the dice I keep from my first roll are discarded on my next roll    
def probabilityB (i, j, k):
    events=[];
    #first roll
    events.append((1/6)**5);
    events.append(ncr(5,i));
    if i!=0:
        events.append(ncr(6,1));
    if i==1 or i==4 or i==0 or i==5:
        events.append(ncr(5,5-i));
    if i==0:
        events.append(6);
    elif i==2:
        events.append(npr(5,5-i)+ncr(5,1)*ncr(4,1));
    elif i==3:
        events.append(ncr(5,5-(i+1))+npr(5,5-i));
    #second roll
    events.append((1/6)**(5-i));
    events.append(ncr(5-i,j)*5);
    if i+j==1 or i+j==4 or i+j==0 or i+j==5:
        events.append(npr(4,5-i-j));
    if i+j==0:
        events.append(5);
    elif i+j==2:
        events.append(npr(4,5-i-j)+ncr(3,1)*ncr(4,1));
    elif i+j==3:
        events.append(ncr(4,5-(i+j+1))+npr(4,5-(i+j)));
    #third roll
    if j<5:
        events.append((1/6)**(5-j));
        events.append(ncr(5-j,k));
    
    return math.prod(events);


#probabilityB separated into parts for the 3 individual rolls
def probabilityB1 (i):
    events=[];
    events.append((1/6)**5);
    events.append(ncr(5,i));
    if i!=0:
        events.append(ncr(6,1));
    if i==1 or i==4 or i==0 or i==5:
        events.append(npr(5,5-i));
    if i==0:
        events.append(6);
    elif i==2:
        events.append(npr(5,5-i)+ncr(5,1)*ncr(4,1))
    elif i==3:
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    return math.prod(events);
def probabilityB2 (i, j):
    events=[];
    events.append((1/6)**(5-i));
    events.append(ncr(5-i,j)*5);
    if i+j==1 or i+j==4 or i+j==0 or i+j==5:
        events.append(npr(4,5-i-j));
    if i+j==0:
        events.append(5);
    elif i+j==2:
        events.append(npr(4,5-i-j)+ncr(3,1)*ncr(4,1))
    elif i+j==3:
        events.append(ncr(4,5-i-j-1)+npr(4,5-i-j));
    
    return math.prod(events);
def probabilityB3 (i, j, k):
    events=[];
    if j<5:
        events.append((1/6)**(5-j));
        events.append(ncr(5-j,k));
        events.append(npr(5,5-j-k));
    else:
        events.append(1);
    return math.prod(events);

#binomial distribution
def p(i, j, k):
    events=[];
    events.append(ncr(5,i)*((1/6)**i)*((5/6)**(5-i)));
    if j<=5:
            events.append(ncr(5-i,j)*((1/6)**j)*((5/6)**(5-i-j)));          
    if k<=5:
        events.append(ncr(5-i-j,k)*((1/6)**k)*((5/6)**(5-i-j-k)));

    return math.prod(events);

#give n Yahtzees, the total score with the all n Yahtzees will be:        
def scoreSeries(n):
    return (50+(n-1)*(100));
#approx. prob of getting n Yahtzees
def probabilitySeries(n):
    return ((Yahtzee()[0]**n));
#summing the unweighted EV from multiplying the scoreSeries and probabilitySeries
def ExVal():
    exVals=0;
    for n in range (1,14):
        exVals+=scoreSeries(n)*probabilitySeries(n);
    return exVals;

#for EV of 3OK and 4OK
#for when kept dice are not rerolled
def ExValA (x,y,z):
    baseProb=probabilityA(x,y,z);
    subVals=[];
    if x==1 and y==0:
        for a in range (1,7):
            for b in range (1,7):
                if a!=b:
                    if a>b:
                        subVals.append(a*5*baseProb*(1/5)*(1/6));
                    elif a<b:
                        subVals.append(b*5*baseProb*(1/5)*(1/6));
    elif x+y==2:
        for h in range (1,7):
            for i in range (1,7):  
                if h!=i:
                    #dont switch
                    if h>i:   
                        subVals.append(((h*5)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)));
                    #switch
                    elif i>h:
                        subVals.append(((i*5)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)));
            subVals.append((h*5)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2)))*(1/6));
    else:
        for c in range (1,7):
            subVals.append((c*5)*baseProb*(1/6));
    return sum(subVals);
#for when dice kept at first are rerolled
def ExValB(x,y,z):
    baseProb=probabilityB(x,y,z);
    subVals=[];
    for c in range (1,7):
        subVals.append((c*5)*baseProb*(1/6));
    return sum(subVals);

#same as ExValA, but with the number of matching dice and their value from the first roll being given
def ExValA1 (x,y,z, val):
    baseProb=probabilityA2(x,y)*probabilityA3(x,y,z);
    subVals=[];
    if x==1 and y==0:
        for b in range (1,7):
            if val!=b:
                if val>b:
                    subVals.append(val*5*baseProb*(1/5));
                elif val<b:
                    subVals.append(b*5*baseProb*(1/5));
    elif x+y==2:
        for i in range (1,7):  
            if val!=i:
                #dont switch
                if val>i:   
                    subVals.append(((val*5)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/5)));
                #switch
                elif i>val:
                    subVals.append(((i*5)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/5)));
        subVals.append((val*5)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2))));
    else:
        subVals.append((val*5)*baseProb);
    return sum(subVals);
#same as ExValA, but with the number of matching dice and their value from the first roll being given
def ExValB1(x,y,z, val):
    baseProb=probabilityB2(x,y)*probabilityB3(x,y,z);
    subVals=[];
    subVals.append((val*5)*baseProb);
    return sum(subVals);

if __name__ == '__main__':
    print (Y());
    print (Yahtzee());
    print(ExVal());
    print (FiveOfAKind1(1,6));


    

    

