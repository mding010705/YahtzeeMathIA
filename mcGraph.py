import matplotlib.pyplot as plt
import markovChain as mc

labels = list(range(1,31))
lab= ['1OK', '2OK', '3OK', '4OK', '5OK']

width = 0.5      

data=[0]*30
#jth element of data array is the vector produced from multiplying initial state vector by transition matrix j-1 times
for j in range (0, 30):
    data[j]=mc.trans(j,mc.vector(0),1)[0]

bars=[[0]*30,[0]*30,[0]*30,[0]*30,[0]*30]
fig, ax = plt.subplots()

#flipping indexes of values in data such that all of the kth value of the ith index of the bars array holds the probability of getting i matching dice in k rolls
for i in range (0,5):
    for k in range (0,30):
        bars[i][k]=data[k][i]

#shift up for the 3, 4, and 5OK bars respectively so graph shows probability that each number of matching dice takes up in relation to each other and the whole sample space
b2= [a + b for a, b in zip(bars[1], bars[0])]
b3= [a + b for a, b in zip(b2, bars[2])]
b4= [a + b for a, b in zip(b3, bars[3])]

#putting in the bars
ax.bar(labels, bars[0], width, label=lab[0])
ax.bar(labels, bars[1], width, bottom=bars[0], label=lab[1])
ax.bar(labels, bars[2], width, bottom=b2, label=lab[2])
ax.bar(labels, bars[3], width, bottom=b3, label=lab[3])
ax.bar(labels, bars[4], width, bottom=b4, label=lab[4])
  
#labels
ax.set_ylabel('Probability of Combination')
ax.set_xlabel('Number of Rolls')
ax.set_title('Probability of Achieving Matching Dice over Mulitple Rolls')
ax.legend()

plt.show()
