#transition matrix
T=[[120/1296,900/1296,250/1296,25/1296,1/1296],
               [0,120/216,80/216,15/216,1/216],
                        [0,0,25/36,10/36,1/36],
                               [0,0,0,5/6,1/6],
                                   [0,0,0,0,1]]

c=[0,0,0,0,0]
b=[0,0,0,0,0]
a=[0,0,0,0,0]

#gives iitial state vector based on a given number of matching dice
def vector (m):
    x=[0,0,0,0,0]
    if int(m)==0:
        x=[120/1296,900/1296,250/1296,25/1296,1/1296]
    elif int(m)<=5 and int(m)!=0:
        x[int(m)-1]=1
    return x

#takes number of repeated rolls, the initial state vector (from vector()), and the desired number of matching dice to give probability of such an event occurring
def trans(r, isv, num):
    prob=0
    b=list(isv)
    a=list(isv)
    for i in range (0, int(r)):
        b=list(a)
        #multiplying row of isv by columns of T and summing the products
        for j in range (0,len(T[0])):
            add=0
            for k in range (0, len(b)):
                add+=b[k]*T[k][j]
            a[j]=add
    for l in range (int(num)-1, len(a)):
        prob+=a[l]
    return [a, prob]


if __name__ == '__main__':
    again='y'
    while again=='y':
        print('How many rolls?')
        rolls= input()
        print ('Given how many matching?')
        match=input()
        print('How many of a kind?')
        ok=input()
        print(trans(rolls, vector(match), ok))
        print ('Again?')
        again=input()
