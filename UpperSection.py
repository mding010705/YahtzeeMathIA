
import math

def upperSection():
    probs=[0,0,0,0,0,0];

                    
    for x in range (0,6):
        for y in range(0,6):
            for z in range (0,6):
                for a in range (0,6):
                    if y+z+a==x:
                        probs[x]+= p(y, z, a);

    return probs;
    
                
def ncr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def expected(value):
    exVals=[0,0,0,0,0,0]
    exV= [0,0,0,0,0,0]
    prob= upperSection();
    for y in range(0,6):
        exV[y]=prob[y]* value*y
    exVals[value-1]= exV;
    return exVals;

def totalEV(value):
    EV=0;
    distr=expected(value)[value-1];
    for y in range (0,6):
        EV+=distr[y]
    return EV;    

def p(i, j, k):
    events=[]
    events.append(ncr(5,i)*((1/6)**i)*((5/6)**(5-i)));
    if j<=5:
            events.append(ncr(5-i,j)*((1/6)**j)*((5/6)**(5-i-j)));          
    if k<=5:
        events.append(ncr(5-i-j,k)*((1/6)**k)*((5/6)**(5-i-j-k)));

    return math.prod(events);

def p12(i, j, k):
    events=[]
    if j<=5:
            events.append(ncr(5-i,j)*((1/6)**j)*((5/6)**(5-i-j)));          
    if k<=5:
        events.append(ncr(5-i-j,k)*((1/6)**k)*((5/6)**(5-i-j-k)));
    
    
    return math.prod(events);
def EV():
    categoryEV=0;
    for x in range (1,7):
        print (str(x)+'s:'+ str(expected(x)[x-1]));
        categoryEV+=totalEV(x);
        print (totalEV(x));

    print ('TOTAL: '+ str(categoryEV));
if __name__ == '__main__':
    print (upperSection());    



    


                   


