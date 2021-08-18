import math

def FOK():
    probs=0;
    for y in range(0,5):
        for z in range (0,5):
            for a in range (0,5):
                if y+z+a==4:
                    probs+= p(y, z, a);
    return probs;

def FourOfAKind():
    prob=0;
    exVal=0;
    for y in range(0,5):
        for z in range (0,5):
            for a in range (0,5):
                if y+z+a==4:
                    prob+= probabilityA(y, z, a);
                    exVal+=ExValA(y,z,a);
                if y+z+a>4 and z>y and z<=5-y and z+a==4 and y!=0:
                    prob+= probabilityB(y, z, a);
                    exVal+=ExValB(y,z,a);
                if a+y+z<=5 and y+z+a>4 and a==4 and y+z<=5:
                    prob+= probabilityC(y,z,a);
                    exVal+=ExValC(y,z,a);
    
    return (prob, exVal/prob, exVal);
def FourOfAKind1(n, val):
    prob=0;
    exVal=0;
    y=n
    for z in range (0,5):
        for c in range (0,5):
            if y+z+c==4:
                prob+=probabilityA2 (y, z)*probabilityA3(y,z,c);
                exVal+=ExValA1(y,z,c,val)
            if y+z+c>4 and z>y and z<=5-y and z+c==4 and y!=0:
                prob+=probabilityB2 (y, z)*probabilityB3(y,z,c)
                exVal+=ExValB1(y,z,c,val)
            if c+y+z<=5 and y+z+c>4 and c==4 and y+z<=5:
                prob+=probabilityC2 (y, z)*probabilityC3(y,z,c)
                exVal+=ExValC1(y,z,c,val)
                    
    return (prob,exVal/prob, exVal);


def ncr(n,r):
    f = math.factorial;
    return f(n) // f(r) // f(n-r);

def npr(n,r):
    f = math.factorial
    return f(n) / f(n-r);
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
    if i<4:
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
    elif i==4:
        events.append((1/6)**(5-i));
        events.append(ncr(5,5-i));
    
    return math.prod(events);
def probabilityA3 (i, j, k):
    events=[];
    
    if i+j<4:
        events.append((1/6)**(5-i-j));
        events.append(ncr(5-i-j,k));
        events.append(npr(5,5-i-j-k));
        if i+j==0:
            events.append(6);
    elif i==4: 
        events.append((1/6)**(5-i));
        events.append(npr(5,5-i));
    elif i+j==4:
        events.append((1/6)**(5-i-j));
        events.append(npr(5,5-i-j));
    return math.prod(events);

def probabilityA (i, j, k):
    events=[];
    events.append((1/6)**5);
    events.append(ncr(5,i));
    events.append(ncr(6,1));
    if i==1 or i==4 or i==0 or i==5:
        events.append(npr(5,5-i));
    if i==0:
        events.append(6);
    elif i==2:
        events.append(npr(5,5-i)+ncr(5,1)*ncr(4,1))
    elif i==3:
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    if i<4:
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
    elif i==4:
        events.append((1/6)**(5-i));
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    if i+j<4:
        events.append((1/6)**(5-i-j));
        events.append(ncr(5-i-j,k));
        events.append(npr(5,5-i-j-k));
    elif i==4: 
        events.append((1/6)**(5-i));
        events.append(npr(5,5-i));
    elif i+j==4:
        events.append((1/6)**(5-i-j));
        events.append(npr(5,5-i-j));
    return math.prod(events);
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
    if j<4:
        events.append((1/6)**(5-j));
        events.append(ncr(5-j,k));
        events.append(npr(5,5-j-k));
    elif j==4:
        events.append((1/6)**(5-j));
        events.append(npr(5,5-j));

    return math.prod(events);
def probabilityB (i, j, k):
    f=math.factorial;
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
    if j<4:
        events.append((1/6)**(5-j));
        events.append(ncr(5-j,k));
        events.append(npr(5,5-j-k));
    elif j==4:
        events.append((1/6)**(5-j));
        events.append(npr(5,5-j));

    return math.prod(events);

def probabilityC1 (i):
    events=[];
    events.append((1/6)**5);
    events.append(ncr(5,i));
    if i==1 or i==4 or i==0 or i==5:
        events.append(npr(5,5-i));
    elif i==2:
        events.append(npr(5,5-i)+ncr(5,1)*ncr(4,1))
    elif i==3:
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    return math.prod(events);
def probabilityC2 (i, j):
    events=[];
    events.append((1/6)**(5-i));
    events.append(ncr(5-i,j));
    if i+j==1 or i+j==4 or i+j==0 or i+j==5:
        events.append(npr(5,5-i-j));
    if i+j==0:
        events.append(6);
    elif i+j==2:
        events.append(npr(5,5-i-j)+ncr(5,1)*ncr(4,1))
    elif i+j==3:
        events.append(npr(5,5-(i+j+1))*5);

    return math.prod(events);
def probabilityC3 (i, j, k):
    events=[];
    events.append((1/6)**(5-i-j));
    events.append(npr(5,5-i-j-k));
    events.append(ncr(5,5-i-j-k)*5);

    return math.prod(events);
        
def probabilityC (i, j, k):
    events=[];
    events.append((1/6)**5);
    events.append(ncr(5,i));
    events.append(ncr(6,1));
    if i==1 or i==4 or i==0 or i==5:
        events.append(npr(5,5-i));
    if i==0:
        events.append(6);
    elif i==2:
        events.append(npr(5,5-i)+ncr(5,1)*ncr(4,1))
    elif i==3:
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    events.append((1/6)**(5-i));
    events.append(ncr(5-i,j));
    if i+j==1 or i+j==4 or i+j==0 or i+j==5:
        events.append(npr(5,5-i-j));
    if i+j==0:
        events.append(6);
    elif i+j==2:
        events.append(npr(5,5-i-j)+ncr(5,1)*ncr(4,1))
    elif i+j==3:
        events.append(npr(5,5-(i+j+1))*5);
    events.append((1/6)**(5-i-j));
    events.append(npr(5,5-i-j-k));
    events.append(ncr(5,5-i-j-k)*5);

    return math.prod(events);


def ExValA (x,y,z):
    baseProb=probabilityA(x,y,z);
    subVals=[];
    if x==4:
        for c in range (1,7):
            for a in range (1,7):
                if a!=c:
                    if a>5:
                        i=a;
                        subVals.append((c*4+i)*baseProb*(1/6)*((1/5)));
                    
                    elif a<=5:
                        for d in range (1,7):
                            if d!=c:
                                if d>=5:
                                    i=d;
                                    subVals.append((c*4+i)*baseProb*(1/6)*((1/5)**2));
                                elif d<5:
                                    for f in range (1,7):
                                        if f!=c:
                                            i=f;
                                            subVals.append((c*4+i)*baseProb*(1/6)*(1/5)*((1/5)**2));

    elif x+y==4:
        if x==1:
            for c in range (5,7):
                for a in range (1,7):
                    if a!=c:
                        if a>=5:
                            i=a
                            subVals.append(((c*4+(i))*baseProb*(1/5))/2);
                        elif a<5:
                            for d in range (1,7):
                                if d!=c:
                                    i=d
                                    subVals.append(((c*4+(i))*baseProb*(1/5)*(1/5))/2);
        else:
            for c in range (1,7):
                for a in range (1,7):
                    if a>=5:
                        i=a
                        subVals.append(((c*4+(i))*baseProb*(1/5))/6);
                    elif a<5:
                        for d in range (1,7):
                            if d!=c:
                                i=d
                                subVals.append(((c*4+(i))*baseProb*(1/5)*(1/5))/6);
                            
    elif x==1 and y==0:
        i=6;
        for a in range (1,7):
            if a!=i:
                subVals.append(((i*4+(a))*baseProb*(1/5)));
                     
    elif x+y==2:
        if x==1:
            for a in range (5,7):
                for b in range (1,7):
                    for h in range (1,7): 
                        if a!=b:
                            #dont switch
                            if a>b and a!=h:   
                                subVals.append(((a*4+h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/2)*(1/5)*(1/5)));
                            #switch
                            elif b>a and b!=h:
                                subVals.append(((b*4+h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/2)*(1/5)*(1/5)));
                    if a!=h:
                        subVals.append((a*4+h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2)))*(1/2)*(1/5));
                
        else:
            for a in range (1,7):
                for b in range (1,7):
                    for h in range (1,7): 
                        if a!=b:
                            #dont switch
                            if a>b and a!=h:   
                                subVals.append(((a*4+h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)*(1/5)));
                            #switch
                            elif b>a and b!=h:
                                subVals.append(((b*4+h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)*(1/5)));
                    if a!=h:
                        subVals.append((a*4+h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2)))*(1/6)*(1/5));
                    
    else:
        for a in range (1,7):
            for b in range (1,7):
                if a!=b:
                    subVals.append((((a*4)+b)*baseProb*(1/5))/6);
    return sum(subVals);
def ExValA1 (x,y,z, val):
    baseProb=probabilityA2(x,y)*probabilityA3(x,y,z);
    subVals=[];
    if x==4:
        for a in range (1,7):
            if a!=val:
                if a>5:
                    i=a;
                    subVals.append((val*4+i)*baseProb*((1/5)));
                
                elif a<=5:
                    for d in range (1,7):
                        if d!=val:
                            if d>=5:
                                i=d;
                                subVals.append((val*4+i)*baseProb*((1/5)**2));
                            elif d<5:
                                for f in range (1,7):
                                    if f!=val:
                                        i=f;
                                        subVals.append((val*4+i)*baseProb*(1/5)*(1/5)*((1/5)));

    elif x+y==4:
        for a in range (1,7):
            if a!=val:
                if a>=5:
                    i=a
                    subVals.append(((val*4+(i))*baseProb*(1/5)));
                elif a<5:
                    for d in range (1,7):
                        if d!=val:
                            i=d
                            subVals.append(((val*4+(i))*baseProb*(1/5)*(1/5)));
                                  
                     
    elif x+y==2:
        for b in range (1,7):
            for h in range (1,7): 
                if b!=val:
                    #dont switch
                    if val>b and val!=h:   
                        subVals.append(((val*4+h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/5)*(1/5)));
                    #switch
                    elif b>val and b!=h:
                        subVals.append(((b*4+h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/5)*(1/5)));
            if val!=h:
                subVals.append((val*4+h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2)))*(1/5));
                    
    elif x==1 and y==0:
        for a in range (1,7):
            for b in range (1,7):
                if a!=val and b!=val:
                    if a<val:
                        subVals.append(((4*val+(b))*baseProb*(1/5)**2));
                    elif val<a:
                        subVals.append(((4*a+(b))*baseProb*(1/5)**2));
    else:
        for b in range (1,7):
            if val!=b:
                subVals.append((((val*4)+b)*baseProb*(1/5)));
    return sum(subVals);

def ExValB1(x,y,z, val):
    baseProb=probabilityB2(x,y)*probabilityB3(x,y,z);
    subVals=[];
    if y==4:
        for c in range (1,7):
            if val!=c:
                if val>=5:
                    subVals.append(((c*4+(val))*baseProb*(1/5)));
                elif val<5:
                    for d in range (1,7):
                        if d!=c:
                            subVals.append(((c*4+(d))*baseProb*(1/5)*(1/5)));

    else:
        for a in range (1,7):
            for b in range (1,7):
                if a!=b and val!=a:
                    subVals.append((((a*4)+b)*baseProb*(1/5)*(1/5)));            
    return sum(subVals);

def ExValB(x,y,z):
    baseProb=probabilityB(x,y,z);
    subVals=[];
    if y==4:
        for c in range (1,7):
            for a in range (5,7):
                if a!=c:
                    subVals.append(((c*4+(a))*baseProb*(1/2))/6);

    else:
        for a in range (1,7):
            for b in range (1,7):
                if a!=b:
                    subVals.append((((a*4)+b)*baseProb*(1/5))/6);            
    return sum(subVals);

def ExValC1(x,y,z, val):
    baseProb=probabilityC2(x,y)*probabilityC3(x,y,z);
    subVals=[];
    if x==1:
        for i in range (1,7):
            for h in range (1,7):
                if i!=val:
                    if val>i and val!=h:
                        subVals.append((h*4+val)*baseProb*(1/5)*(1/5));
                    elif i>val and i!=h:
                        subVals.append((h*4+i)*baseProb*(1/5)*(1/5));
                    
        
    else:
        for a in range (1,7):
            for b in range (1,7):
                if a!=b and a!=val:
                    subVals.append(((a*4)+b)*baseProb*(1/5)*(1/5));            
    return sum(subVals);


def ExValC(x,y,z):
    baseProb=probabilityC(x,y,z);
    subVals=[];
    if x==1:
        i=6;
        for h in range (1,7):
            if h!=i:
                subVals.append((h*4+i)*baseProb*(1/5));
        
    else:
        for a in range (1,7):
            for b in range (1,7):
                if a!=b:
                    subVals.append(((a*4)+b)*baseProb*(1/6)*(1/5));            
    return sum(subVals);


if __name__ == '__main__':
    print (FourOfAKind());
    print (FourOfAKind1(4,6), FourOfAKind1(4,3))


        
