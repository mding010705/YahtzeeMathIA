import chooseComp as cc
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

fig = plt.figure()
barWidth = 0.2

zdata31=[]
for i in range (0, len(cc.results3),3): 
    zdata31.append(cc.results3[i][2])
print('31', zdata31)
zdata32=[]
for i in range (1, len(cc.results3),3): 
    zdata32.append(cc.results3[i][2])
print('32',zdata32)
zdata33=[]
for i in range (2, len(cc.results3),3): 
    zdata33.append(cc.results3[i][2])
print('33',zdata33)
xdata3=[]
for i in range (0, len(cc.results3),3): 
    xdata3.append(cc.results3[i][0]) 
ydata3=[]
for i in range (0, len(cc.results3),3): 
    ydata3.append(cc.results3[i][1])
zdata41=[]
for i in range (0, len(cc.results4),4): 
    zdata41.append(cc.results4[i][2])
print('41',zdata41)
zdata42=[]
for i in range (1, len(cc.results4),4): 
    zdata42.append(cc.results4[i][2])
print('42',zdata42)
zdata43=[]
for i in range (2, len(cc.results4),4): 
    zdata43.append(cc.results4[i][2])
print('43',zdata43)
zdata44=[]
for i in range (3, len(cc.results4),4): 
    zdata44.append(cc.results4[i][2])
print('44',zdata44)
xdata4=[]
for i in range (0, len(cc.results4),4): 
    xdata4.append(cc.results4[i][0]) 
ydata4=[]
for i in range (0, len(cc.results4),4): 
    ydata4.append(cc.results4[i][1])
x3 = np.arange(len(zdata31))
x4 = np.arange(len(zdata41))

def autolabel(height, shift ):
    for index,data in enumerate(height):
        plt.text(x=index+shift/18 , y =data+1 , s=f"{round(data, 2)}" , fontdict=dict(fontsize=7), rotation='vertical')

    
# plotting the points
plt.subplot(2, 1, 1)
plt.bar(x3+0.4, zdata33, color= "green", width=barWidth, label= "3 Matching")
autolabel(zdata33, 6)
plt.bar(x3+0.2, zdata32, color= "blue",width=barWidth, label= "2 Matching" )
autolabel(zdata32, 2.5)
plt.bar(x3, zdata31, color= "red",width=barWidth, label= "1 Matching" )
autolabel(zdata31, -1)
ax = plt.gca()

ax.axes.xaxis.set_ticklabels([])
#plt.xticks([r + barWidth for r in range(len(zdata31))], ['|','|','|','|','|','|'])

# naming the y axis
plt.ylabel('Unweighted EV of 3OK')
plt.legend()

plt.subplot(2, 1, 2)
plt.bar(x4+0.6, zdata44, color= "orange", width=barWidth, label= "4 Matching")
autolabel(zdata44, 10)
plt.bar(x4+0.4, zdata43, color= "green",width=barWidth, label= "3 Matching" )
autolabel(zdata43, 6)
plt.bar(x4+0.2, zdata42, color= "blue",width=barWidth, label= "2 Matching" )
autolabel(zdata42, 3)
plt.bar(x4, zdata41, color= "red",width=barWidth, label= "1 Matching" )
autolabel(zdata41, -1)
plt.xticks([r + barWidth for r in range(len(zdata41))], ['1', '2', '3','4','5','6'])
# naming the x axis
plt.xlabel('Value of Matching Dice')
# naming the y axis
plt.ylabel('Unweighted EV of 4OK')
plt.legend()
  
# giving a title to my graph
plt.suptitle('EV of 3OK and 4OK Given a Specific Number of Matching Dice')


# function to show the plot
plt.show()

