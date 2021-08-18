import math

def ThreeOfAKind():
    prob=0;
    exVal=0;
    for y in range(0,4):
        for z in range (0,4):
            for a in range (0,4):
                if y+z+a==3:
                    prob+= probabilityA (y,z,a);
                    exVal+= ExValA(y,z,a);
                    
                if y+z+a>3 and z>y and z<=5-y and z+a==3 and y!=0:
                    prob+=probabilityB (y,z,a);
                    exVal+= ExValB(y,z,a);
                    
                if a+y+z<=5 and y+z+a>3 and a==3 and y+z<=5:
                    prob+=probabilityC (y,z,a);
                    exVal+= ExValC(y,z,a);
                    
                if y+z+a>3 and a<=5-z and a==3 and y+z<=5 and z>y and y!=0:
                    prob+=probabilityBC (y,z,a);
                    exVal+=ExValBC(y,z,a);
                    
    return (prob,exVal/prob, exVal);

def ThreeOfAKind1(n, val):
    prob=0;
    exVal=0;
    y=n
    for z in range (0,4):
        for a in range (0,4):
            if y+z+a==3:
                prob+=probabilityA2 (y, z)*probabilityA3(y,z,a);
                exVal+=ExValA1(y,z,a,val)
            if y+z+a>3 and z>y and z<=5-y and z+a==3 and y!=0:
                prob+=probabilityB2 (y, z)*probabilityB3(y,z,a)
                exVal+=ExValB1(y,z,a,val)
            if a+y+z<=5 and y+z+a>3 and a==3 and y+z<=5:
                prob+=probabilityC2 (y, z)*probabilityC3(y,z,a)
                exVal+=ExValC1(y,z,a,val)
            if y+z+a>3 and a<=5-z and a==3 and y+z<=5 and z>y and y!=0:
                prob+=probabilityBC2 (y, z)*probabilityBC3(y,z,a)
                exVal+=ExValBC1(y,z,a,val)
                    
    return (prob,exVal/prob, exVal);


def ncr(n,r):
    f = math.factorial;
    return f(n) // f(r) // f(n-r);

def npr(n,r):
    f = math.factorial
    return f(n) / f(n-r);

def probability(y,z,x):
    if y+z+x==3:
        a=probabilityA (y, z, x);
    if y+z+x>3 and z>y and z<=5-y and z+x==3 and y!=0:
        b=probabilityB (y, z, x)
    if x+y+z<=5 and y+z+x>3 and x==3 and y+z<=5:
        c=probabilityC (y,z,x);
    if y+z+x>3 and x<=5-z and x==3 and y+z<=5 and z>y and y!=0:
        bc=probabilityBC (y,z,x);
    return (a, b, c, bc, a+b+c+bc);

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
    if i<3:
        events.append((1/6)**(5-i));
        events.append(ncr(5-i,j));
        if i==0 and j!=0:
            events.append(6);
        if i+j==1 or i+j==4 or i+j==0 or i+j==5:
            events.append(npr(5,5-i-j));
        if i+j==0:
            events.append(6);
        elif i+j==2:
            events.append(npr(5,5-i-j)+ncr(5,1)*ncr(4,1))
        elif i+j==3:
            events.append(ncr(5,5-i-j-1)+npr(5,5-i-j));
    elif i==3:
        events.append((1/6)**(5-i));
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    return math.prod(events);

def probabilityA3 (i, j, k):
    events=[];
    if i+j<3:
        events.append((1/6)**(5-i-j));
        events.append(ncr(5-i-j,k));
        events.append(ncr(5,5-i-j-k-1)+npr(5,5-i-j-k));
        if i+j==0:
            events.append(6);
    elif i==3: 
        events.append((1/6)**(5-i));
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    elif i+j==3:
        events.append((1/6)**(5-i-j));
        events.append(ncr(5,5-i-j-1)+npr(5,5-i-j));
  
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
    if i<3:
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
           
    elif i==3:
        events.append((1/6)**(5-i));
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    if i+j<3:
        events.append((1/6)**(5-i-j));
        events.append(ncr(5-i-j,k));
        events.append(ncr(5,5-i-j-k-1)+npr(5,5-i-j-k));
    elif i==3: 
        events.append((1/6)**(5-i));
        events.append(ncr(5,5-i-1)+npr(5,5-i));
    elif i+j==3:
        events.append((1/6)**(5-i-j));
        events.append(ncr(5,5-i-j-1)+npr(5,5-i-j));
 
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
    if 5-i-j>=2:
        if j==2:
            events.append(npr(4,5-i-j)+ncr(3,1)*ncr(4,1));
        elif j==3:
            events.append(ncr(4,5-i-j-1)+npr(4,5-i-j));
    else:
        events.append(npr(4,5-i-j));
    return math.prod(events);

def probabilityB3 (i, j, k):
    events=[];
    if j<3:
        events.append((1/6)**(5-j));
        events.append(ncr(5-j,k));
        events.append(ncr(5,5-j-k-1)+npr(5,5-j-k));
    elif j==3:
        events.append((1/6)**(5-j));
        events.append(ncr(5,5-j-1)+npr(5,5-j));

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
    if 5-i-j>=2:
        if j==2:
            events.append(npr(4,5-i-j)+ncr(3,1)*ncr(4,1));
        elif j==3:
            events.append(ncr(4,5-i-j-1)+npr(4,5-i-j));
    else:
        events.append(npr(4,5-i-j));
    if j<3:
        events.append((1/6)**(5-j));
        events.append(ncr(5-j,k));
        events.append(ncr(5,5-j-k-1)+npr(5,5-j-k));
    elif j==3:
        events.append((1/6)**(5-j));
        events.append(ncr(5,5-j-1)+npr(5,5-j));

    return math.prod(events);
       
def probabilityC1 (i):
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

def probabilityC2 (i, j):
    events=[];
    events.append((1/6)**(5-i));
    events.append(ncr(5-i,j));
    if i==0 and j!=0:
        events.append(6);
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
    events.append(ncr(5,5-i-j-k)+npr(5,5-i-j-k));
    events.append(ncr(5,5-i-j-k)*5);

    return math.prod(events);

def probabilityC (i, j, k):
    f=math.factorial;
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
    events.append(ncr(5,5-i-j-k)+npr(5,5-i-j-k));
    events.append(ncr(5,5-i-j-k)*5);

    return math.prod(events);

def probabilityBC1 (i):
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

def probabilityBC2 (i, j):
    events=[];
    events.append((1/6)**(5-i));
    events.append(ncr(5-i,j)*5);
    if 5-i-j>=2:
        if j==2:
            events.append(npr(4,5-i-j)+ncr(3,1)*ncr(4,1));
        elif j==3:
            events.append(ncr(4,5-i-j-1)+npr(4,5-i-j));
    else:
        events.append(npr(4,5-i-j));
    return math.prod(events);

def probabilityBC3 (i, j, k):
    events=[];
    events.append((1/6)**(5-j));
    events.append(ncr(5,5-j-k)+npr(5,5-j-k));
    events.append(ncr(5,5-(j+k))*5);

    return math.prod(events);

def probabilityBC (i, j, k):
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
        events.append(6);
    elif i+j==2:
        events.append(npr(4,5-i-j)+ncr(3,1)*ncr(4,1))
    elif i+j==3:
        events.append(ncr(4,5-i-j-1)+npr(4,5-i-j));
    
    events.append((1/6)**(5-j));
    events.append(ncr(5,5-j-k)+npr(5,5-j-k));
    events.append(ncr(5,5-(j+k))*5);
    return math.prod(events);
    


def ExValA (x,y,z):
    baseProb=probabilityA(x,y,z);
    subVals=[];
    if x==3:
        for c in range (1,7):
            for a in range (1,7):
                for b in range(1,7):
                    if a!=c and b!=c:
                        if a>5 and b>5:
                            i=a;
                            j=b;
                            subVals.append((c*3+i+j)*baseProb*(1/6)*((1/5)**2));
                        elif a>5 and b<=5:
                            i=a;
                            for d in range (1,7):
                                if d!=c:
                                    if d>=5:
                                        j=d;
                                        subVals.append((c*3+i+j)*baseProb*(1/6)*(1/5)*((1/5)**2));
                                    else:
                                        for e in range (1,7):
                                            if e!=c:
                                                j=e;
                                                subVals.append((c*3+i+j)*baseProb*(1/6)*(1/5)*(1/5)*((1/5)**2));
                        elif b>5 and a<=5:
                            i=b;
                            for d in range (1,7):
                                if d!=c:
                                    if d>=5:
                                        j=d;
                                        subVals.append((c*3+i+j)*baseProb*(1/6)*(1/5)*((1/5)**2));
                                    else:
                                        for e in range (1,7):
                                            if e!=c:
                                                j=e;
                                                subVals.append((c*3+i+j)*baseProb*(1/6)*(1/5)*(1/5)*((1/5)**2));
                        elif a<=5 and b<=5:
                            for d in range (1,7):
                                for e in range (1,7):
                                    if d!=c and e!=c:
                                        if d>=5 and e>=5:
                                            j=d;
                                            i=e;
                                            subVals.append((c*3+i+j)*baseProb*(1/6)*(1/5)*(1/5)*((1/5)**2));
                                        elif d>=5 and e<5:
                                            j=d;
                                            for f in range (1,7):
                                                if f!=c:
                                                    i=f;
                                                    subVals.append((c*3+i+j)*baseProb*(1/6)*(1/5)*(1/5)*(1/5)*((1/5)**2))
                                        elif d<=5 and e>5:
                                            i=e;
                                            for f in range (1,7):
                                                if f!=c:
                                                    j=f;
                                                    subVals.append((c*3+i+j)*baseProb*(1/6)*(1/5)*(1/5)*(1/5)*((1/5)**2));
                                        elif d<5 and e<5:
                                            for f in range (1,7):
                                                for g in range (1,7):
                                                    if f!=c and g!=c:
                                                        i=g;
                                                        j=f;
                                                        subVals.append((c*3+i+j)*baseProb*(1/6)*(1/5)*(1/5)*(1/5)*(1/5)*((1/5)**2));

    elif x+y==3:
        if x==1:
            for c in range (5,7):
                i=0;
                j=0;
                for a in range (1,7):
                    for b in range (1,7):
                        if a!=c and b!=c:
                            if a>=5 and b>=5:
                                i=a
                                j=b
                                subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5))/2);
                            elif a<5 and b>=5:
                                j=b;
                                for d in range (1,7):
                                    if d!=c:
                                        i=d
                                        subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5))/2);
                            elif a>=5 and b<5:
                                i=a;
                                for d in range (1,7):
                                    if d!=c:
                                        j=d
                                        subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5))/2);
                            elif a<5 and b<5:
                                for d in range (1,7):
                                    for e in range (1,7):
                                        if d!=c and e!=c:
                                            i=d;
                                            j=e;
                                            subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5)*(1/5))/2);
        else:
            for c in range (1,7):
                i=0;
                j=0;
                for a in range (1,7):
                    for b in range (1,7):
                        if a!=c and b!=c:
                            if a>=5 and b>=5:
                                i=a
                                j=b
                                subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5))/6);
                            elif a<5 and b>=5:
                                j=b;
                                for d in range (1,7):
                                    if d!=c:
                                        i=d
                                        subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5))/6);
                            elif a>=5 and b<5:
                                i=a;
                                for d in range (1,7):
                                    if d!=c:
                                        j=d
                                        subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5))/6);
                            elif a<5 and b<5:
                                for d in range (1,7):
                                    for e in range (1,7):
                                        if d!=c and e!=c:
                                            i=d;
                                            j=e;
                                            subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5)*(1/5))/6);
                            
        
    elif x==1 and y==0:
        for a in range (1,7):
            for b in range (1,7):
                if a!=6 and b!=6:
                    subVals.append(((3*6+(a)+(b))*baseProb*(1/5)**2));
                     
    elif x+y==2:
        if x==1:
            for a in range (1,7):
                for b in range (1,7):
                    for h in range (5,7):
                        for i in range (1,7):  
                            if h!=i:
                                #dont switch
                                if h>i and a!=h and b!=h:   
                                    subVals.append(((h*3+a+b)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/2)*(1/5)*(1/5)**2));
                                #switch
                                elif i>h and a!=i and b!=i:
                                    subVals.append(((i*3+a+b)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/2)*(1/5)*(1/5)**2));
                        if a!=h and b!=h:
                            subVals.append((h*3+a+b)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2)))*(1/2)*(1/5)*(1/5));
        else:
            for a in range (1,7):
                for b in range (1,7):
                    for h in range (1,7):
                        for i in range (1,7):  
                            if h!=i:
                                #dont switch
                                if h>i and a!=h and b!=h:   
                                    subVals.append(((h*3+a+b)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)*(1/5)**2));
                                #switch
                                elif i>h and a!=i and b!=i:
                                    subVals.append(((i*3+a+b)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)*(1/5)**2));
                        if a!=h and b!=h:
                            subVals.append((h*3+a+b)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2)))*(1/6)*(1/5)*(1/5));
                    
    else:
        for a in range (1,7):
            for b in range (1,7):
                for c in range (1,7):
                    if a!=b and a!=c:
                        subVals.append((((a*3)+b+c)*baseProb*(1/5)**2)/6);
    return sum(subVals);
    
def ExValB(x,y,z):
    baseProb=probabilityB(x,y,z);
    subVals=[];
    if y==3:
        if x==1:
            for a in range (5,7):
                for h in range (1,7):
                    for i in range (1,7):  
                        if a!=h and i!=h:
                            if i>=5:
                                subVals.append(((h*3+(i)+(a))*baseProb*(1/5)*(1/5))/2);
                            elif i<5:
                                for d in range (1,7):
                                    if d!=h:
                                        subVals.append(((h*3+(i)+(a))*baseProb*(1/5)*(1/5))/2);
                                
                                
                                
        else:
            for c in range (1,7):
                i=0;
                j=0;
                for a in range (1,7):
                    for b in range (1,7):
                        if a!=c and b!=c:
                            if a>=5 and b>=5:
                                i=a
                                j=b
                                subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5))/6);
                            elif a<5 and b>=5:
                                j=b;
                                for d in range (1,7):
                                    if d!=c:
                                        i=d
                                        subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5))/6);
                            elif a>=5 and b<5:
                                i=a;
                                for d in range (1,7):
                                    if d!=c:
                                        j=d
                                        subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5))/6);
                            elif a<5 and b<5:
                                for d in range (1,7):
                                     for e in range (1,7):
                                        if d!=c and e!=c:
                                            i=d;
                                            j=e;
                                            subVals.append(((c*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5)*(1/5))/6);
    else:
        for a in range (1,7):
            for b in range (1,7):
                for c in range (1,7):
                    if a!=b and a!=c:
                        subVals.append((((a*3)+b+c)*baseProb*(1/5)**2)/6);            
    return sum(subVals);
        
def ExValC(x,y,z):
    baseProb=probabilityC(x,y,z);
    subVals=[];
    if x+y==2:
        if x==1:
            for k in range (5,7):
                for h in range (1,7):
                    for i in range (1,7):
                        if h>k and h!=i:
                            subVals.append((i*3+2*h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)*(1/5));
                        if h<k and k!=i:
                            subVals.append((i*3+2*k)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)*(1/5));
                    if h!=k:
                        subVals.append((k*3+2*h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2)))*(1/6)*(1/5));
                   
        if x==2:
            for k in range (1,7):
                for h in range (1,7):
                    for i in range (1,7):
                        if h>k and h!=i:
                            subVals.append((i*3+2*h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)*(1/5));
                        if h<k and k!=i:
                            subVals.append((i*3+2*k)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/6)*(1/5)*(1/5));
                    if h!=k:
                        subVals.append((k*3+2*h)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2)))*(1/6)*(1/5));
        if y==2:
            for k in range (1,7):
                for h in range (1,7):
                    if h!=k:
                        subVals.append((k*3+2*h)*baseProb*(1/6)*(1/5));
            
        
    else:
        for a in range (1,7):
            for b in range (1,7):
                for c in range (1,7):
                    if a!=b and a!=c:
                        subVals.append(((a*3)+b+c)*baseProb*(1/6)*(1/5)**2);            
    return sum(subVals);
def ExValBC(x,y,z):
    baseProb=probabilityBC(x,y,z);
    subVals=[];
    for c in range (5,7):
        for a in range (1,7):
            for b in range (1,7):
                if a!=b and b!=c:
                    subVals.append((((a*3)+b*2)*baseProb*(1/6)*(1/5)*(1/2)));            
    return sum(subVals);

def ExValA1 (x,y,z, val):
    baseProb=probabilityA2(x,y)*probabilityA3(x,y,z);
    subVals=[];
    if x==3:
        for a in range (1,7):
            for b in range(1,7):
                if a!=val and b!=val:
                    if a>5 and b>5:
                        i=a;
                        j=b;
                        subVals.append((val*3+i+j)*baseProb*((1/5)**2));
                    elif a>5 and b<=5:
                        i=a;
                        for d in range (1,7):
                            if d!=val:
                                if d>=5:
                                    j=d;
                                    subVals.append((val*3+i+j)*baseProb*(1/5)*((1/5)**2));
                                else:
                                    for e in range (1,7):
                                        if e!=val:
                                            j=e;
                                            subVals.append((val*3+i+j)*baseProb*(1/5)*(1/5)*((1/5)**2));
                    elif b>5 and a<=5:
                        i=b;
                        for d in range (1,7):
                            if d!=val:
                                if d>=5:
                                    j=d;
                                    subVals.append((val*3+i+j)*baseProb*(1/5)*((1/5)**2));
                                else:
                                    for e in range (1,7):
                                        if e!=val:
                                            j=e;
                                            subVals.append((val*3+i+j)*baseProb*(1/5)*(1/5)*((1/5)**2));
                    elif a<=5 and b<=5:
                        for d in range (1,7):
                            for e in range (1,7):
                                if d!=val and e!=val:
                                    if d>=5 and e>=5:
                                        j=d;
                                        i=e;
                                        subVals.append((val*3+i+j)*baseProb*(1/5)*(1/5)*((1/5)**2));
                                    elif d>=5 and e<5:
                                        j=d;
                                        for f in range (1,7):
                                            if f!=val:
                                                i=f;
                                                subVals.append((val*3+i+j)*baseProb*(1/5)*(1/5)*(1/5)*((1/5)**2))
                                    elif d<=5 and e>5:
                                        i=e;
                                        for f in range (1,7):
                                            if f!=val:
                                                j=f;
                                                subVals.append((val*3+i+j)*baseProb*(1/5)*(1/5)*(1/5)*((1/5)**2));
                                    elif d<5 and e<5:
                                        for f in range (1,7):
                                            for g in range (1,7):
                                                if f!=val and g!=val:
                                                    i=g;
                                                    j=f;
                                                    subVals.append((val*3+i+j)*baseProb*(1/5)*(1/5)*(1/5)*(1/5)*((1/5)**2));

    elif x+y==3:
        for a in range (1,7):
            for b in range (1,7):
                if a!=val and b!=val:
                    if a>=5 and b>=5:
                        i=a
                        j=b
                        subVals.append(((val*3+(i)+(j))*baseProb*(1/5)*(1/5)));
                    elif a<5 and b>=5:
                        j=b;
                        for d in range (1,7):
                            if d!=val:
                                i=d
                                subVals.append(((val*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5)));
                    elif a>=5 and b<5:
                        i=a;
                        for d in range (1,7):
                            if d!=val:
                                j=d
                                subVals.append(((val*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5)));
                    elif a<5 and b<5:
                        for d in range (1,7):
                            for e in range (1,7):
                                if d!=val and e!=val:
                                    i=d;
                                    j=e;
                                    subVals.append(((val*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5)*(1/5)));
                        
                     
    elif x+y==2:
        for a in range (1,7):
            for b in range (1,7):
                for i in range (1,7):  
                    if val!=i:
                        #dont switch
                        if val>i and a!=val and b!=val:   
                            subVals.append(((val*3+a+b)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1)))*ncr(5,1)*ncr(4,1))*(1/5)*(1/5)**2));
                        #switch
                        elif i>val and a!=i and b!=i:
                            subVals.append(((i*3+a+b)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1)))*ncr(5,1)*ncr(4,1))*(1/5)*(1/5)**2));
                if a!=val and b!=val:
                    subVals.append((val*3+a+b)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1)))*npr(5,5-2))*(1/5)*(1/5));
    elif x==1 and y==0:
        for a in range (1,7):
            for b in range (1,7):
                for c in range (1,7):
                    if a!=val and b!=val and c!=val:
                        if a<val:
                            subVals.append(((3*val+(c)+(b))*baseProb*(1/5)**3));
                        elif val<a:
                            subVals.append(((3*a+(c)+(b))*baseProb*(1/5)**3));
                    
    else:
        for b in range (1,7):
            for c in range (1,7):
                if val!=b and val!=c:
                    subVals.append((((val*3)+b+c)*baseProb*(1/5)**2));
    return sum(subVals);


def ExValB1(x,y,z, val):
    baseProb=probabilityB2(x,y)*probabilityB3(x,y,z);
    subVals=[];
    if y==3:
        for a in range (1,7):
            for b in range (1,7):
                if a!=val and b!=a:
                    if val>=5 and b>=5:
                        i=val
                        j=b
                        subVals.append(((a*3+(i)+(j))*baseProb*(1/5)*(1/5)));
                    elif val<5 and b>=5:
                        j=b;
                        for d in range (1,7):
                            if d!=a:
                                i=d
                                subVals.append(((a*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5)));
                    elif val>=5 and b<5:
                        i=val;
                        for d in range (1,7):
                            if d!=a:
                                j=d
                                subVals.append(((a*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5)));
                    elif val<5 and b<5:
                        for d in range (1,7):
                             for e in range (1,7):
                                if d!=a and e!=a:
                                    i=d;
                                    j=e;
                                    subVals.append(((a*3+(i)+(j))*baseProb*(1/5)*(1/5)*(1/5)*(1/5)));
    else:
        for a in range (1,7):
            for b in range (1,7):
                for c in range (1,7):
                    if a!=b and a!=c and a!=val:
                        subVals.append((((a*3)+b+c)*baseProb*(1/6)*(1/5)**2));            
    return sum(subVals);
        
def ExValC1(x,y,z, val):
    baseProb=probabilityC2(x,y)*probabilityC3(x,y,z);
    subVals=[];
    if x+y==2:
        if y==2:
            for k in range (1,7):
                for i in range (1,7):
                    if i!=k:
                        subVals.append((k*3+2*i)*baseProb*(1/5)*(1/6));
        else:
            for k in range (1,7):
                for i in range (1,7):
                    if val>k and val!=i:
                        subVals.append((i*3+2*val)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/5)*(1/5));
                    if val<k and k!=i:
                        subVals.append((i*3+2*k)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*ncr(5,1)*ncr(4,1)))*(1/5)*(1/5));
                if val!=k:
                    subVals.append((k*3+2*val)*((baseProb/(npr(5,5-2)+ncr(5,1)*ncr(4,1))*npr(5,5-2)))*(1/5));
         
    else:
        for a in range (1,7):
            for b in range (1,7):
                if a!=b and a!=val:
                    subVals.append(((a*3)+b+val)*baseProb*(1/5)**2);            
    return sum(subVals);


def ExValBC1(x,y,z, val):
    baseProb=probabilityBC2(x,y)*probabilityBC3(x,y,z);
    subVals=[];
    for a in range (1,7):
        for b in range (1,7):
            if a!=b and b!=val:
                subVals.append((((a*3)+b*2)*baseProb*(1/5)*(1/5)));            
    return sum(subVals);


if __name__ == '__main__':
    print (ThreeOfAKind());
    print (ThreeOfAKind1(2,6), ThreeOfAKind1(3,1))

