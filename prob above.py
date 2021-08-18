import matplotlib.pyplot as plt
import numpy as np

#probability of rolling same or higher number in max. 2 rolls
probs2=[]
for x in range (1,7):
    probs2.append(((7-x)/6)+((x-1)*(7-x)/36))

#probability of rolling same or higher number in 1 roll
probs1=[]
for x in range (1,7):
    probs1.append(((7-x)/6))

barWidth = 0.25
#y axis values
y2 = probs2
y1 = probs1
# x axis values
x2 = np.arange(len(y2))


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
