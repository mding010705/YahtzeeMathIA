import matplotlib.pyplot as plt
import numpy as np

probs2=[]
comp=[]
for x in range (1,7):
    probs2.append(((7-x)/6)+((x-1)*(7-x)/36))
    comp.append(((x-1)*(x-1)/36))
print (probs2)
print (comp)

probs1=[]
comp=[]
for x in range (1,7):
    probs1.append(((7-x)/6))
    comp.append((x-1)/6)
print (probs1)
print (comp)

barWidth = 0.25

y2 = probs2
y1 = probs1


  
# x axis values
x2 = np.arange(len(y2))
# corresponding y axis values


# plotting the points 
plt.bar(x2+0.25, y1, color= "green", width=barWidth, label= "In 1 Roll")
plt.bar(x2, y2, color= "red",width=barWidth, label= "In 2 Rolls" )
plt.xticks([r + barWidth for r in range(len(y2))], ['1', '2', '3', '4', '5','6'])
# naming the x axis
plt.xlabel('Die Value')
# naming the y axis
plt.ylabel('Probability of Rolling a Larger or Equal Number')
  
# giving a title to my graph
plt.title('Probabilities of Rolling a Larger or Equal Number per Die Value')

plt.legend()
# function to show the plot
plt.show()
