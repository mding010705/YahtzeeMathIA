import profitvprob as pvp
import matplotlib.pyplot as plt
import numpy as np

#gathering info on first roll to form graph
print('What is your roll? (ex. 13362)')
roll= list(input())
for i in range (len(roll)):
    roll[i]=int(roll[i])
print(roll)
print ('Have you already scored a Yahtzee? (y/n)')
yahtzee=input()

print(pvp.USScores(roll))
print(pvp.yahtzeeScore(yahtzee, roll))
print(pvp.TOKscore(roll))
print(pvp.FrOKscore(roll))

profit=[]
prob=[]
labels=[]
#sorts out the zero's from the data from profitvprob, condenses the separate lists into profit array (x values) and prob array (y values), and makes label for point
for i in range (len(pvp.USScores(roll)[0])):
    if pvp.USScores(roll)[0][i]!=0:
        profit.append(pvp.USScores(roll)[0][i])
        labels.append('US, '+str(i+1)+'s')
for i in range (len(pvp.USScores(roll)[1])):
    if pvp.USScores(roll)[1][i]!=0:
        prob.append(pvp.USScores(roll)[1][i])
for j in range (len(pvp.TOKscore(roll)[0])):
    if pvp.TOKscore(roll)[0][j]!=0:
        profit.append(pvp.TOKscore(roll)[0][j])
        labels.append('3OK, '+str(j+1)+'s')
for j in range (len(pvp.TOKscore(roll)[1])):
    if pvp.TOKscore(roll)[1][j]!=0:
        prob.append(pvp.TOKscore(roll)[1][j])
for k in range (len(pvp.FrOKscore(roll)[0])):
    if pvp.FrOKscore(roll)[0][k]!=0:
        profit.append(pvp.FrOKscore(roll)[0][k])
        labels.append('4OK, '+str(k+1)+'s')
for k in range (len(pvp.FrOKscore(roll)[1])):
    if pvp.FrOKscore(roll)[1][k]!=0:
        prob.append(pvp.FrOKscore(roll)[1][k])
profit.append(pvp.yahtzeeScore(yahtzee, roll)[0])
prob.append(pvp.yahtzeeScore(yahtzee, roll)[1])
labels.append('Yahtzee')

#possible plot point colours
colours=['red','orange','gold','lawngreen','forestgreen','turquoise','teal','cyan','dodgerblue','gray','navy','darkorchid','darkmagenta','magenta','deeppink','palevioletred']

#placing each plot point individually so they can have distinct labels
for l in range (len(labels)):
    plt.plot(profit[l], prob[l], 'o', color=colours[l],label=labels[l])
    
#gives and plots linear regression of all points
print(np.polyfit(profit, prob, 1).tolist())
m = np.polyfit(profit, prob, 1).tolist()[0]
b = np.polyfit(profit, prob, 1).tolist()[1]
reg=[]
for p in range (len(profit)):
    reg.append(profit[p]*m+b)
plt.plot(profit,reg, label='Baseline')

#taking Yahtzee off of data arrays since it is often an outlier that is not considered when trying to score so a new trendline can be made
profit0=list(profit[:-1])
print(profit0)
prob0=list(prob[:-1])
#gives and plots linear regression excluding Yahtzee
print(np.polyfit(profit0, prob0, 1).tolist())
m0 = np.polyfit(profit0, prob0, 1).tolist()[0]
b0 = np.polyfit(profit0, prob0, 1).tolist()[1]
reg0=[]
for p in range (len(profit0)):
    reg0.append(profit0[p]*m0+b0)
plt.plot(profit0,reg0, label='Baseline (without Yahtzee)')

# naming the x axis
plt.xlabel('Profit (Expected Potential Score)')
# naming the y axis
plt.ylabel('Probability')
  
# giving a title to my graph
plt.title('Comparison of Profit vs. Probability')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
