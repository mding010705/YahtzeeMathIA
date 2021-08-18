import matplotlib.pyplot as plt
import UpperSection as US
import numpy as np

#possible scores of US categories
aces= [0,1,2,3,4,5];
twos= [0,2,4,6,8,10];
threes= [0,3,6,9,12,15];
fours= [0,4,8,12,16,20];
fives= [0,5,10,15,20,25];
sixes= [0,6,12,18,24,30];
#arrays with an element per possible score in US
probabilityScores=[0]*106;
categoryPercent=[0]*106;
#iterating through every possible score
for score in range (0,106):
    combo=0;
    pb=0;
    numCategories=[0,0,0,0,0,0];
    #iterating through every possible way to get score (pls don't curse me for my inefficient code, I love my for loops)
    for a in range (0,6):
        for b in range (0,6):
            for c in range (0,6):
                for d in range (0,6):
                    for e in range (0,6):
                        for f in range (0,6):
                            if aces[a]+twos[b]+threes[c]+fours[d]+fives[e]+sixes[f]==score:
                                combo+=1;
                                pb+=(US.upperSection()[a]*US.upperSection()[b]*US.upperSection()[c]*US.upperSection()[d]*US.upperSection()[e]*US.upperSection()[f]);
                                if score>0:
                                    #adding the percent contribution of the US category, n, to the nth element of the numCategories array 
                                    numCategories[0]+=((a*1)/score);
                                    numCategories[1]+=((b*2)/score);
                                    numCategories[2]+=((c*3)/score);
                                    numCategories[3]+=((d*4)/score);
                                    numCategories[4]+=((e*5)/score);
                                    numCategories[5]+=((f*6)/score);
    #normalizing the culmulated percents
    for i in range(0,6):
        numCategories[i]/=combo;
    #storing results before resetting variable for next score
    categoryPercent[score]=numCategories;                              
    probabilityScores[score]=pb;


bonusProb=0;
per1=[];
per2=[];
per3=[];
per4=[];
per5=[];
per6=[];
#storing only the results from above that have scores that earn the US bonus
for x in range (63,106):
    bonusProb+=probabilityScores[x];
    per1.append(categoryPercent[x][0]);
    per2.append(categoryPercent[x][1]);
    per3.append(categoryPercent[x][2]);
    per4.append(categoryPercent[x][3]);
    per5.append(categoryPercent[x][4]);
    per6.append(categoryPercent[x][5]);
#adding up results per category    
catDistr= [sum(per1), sum(per2), sum(per3), sum(per4),sum(per5),sum(per6)];    

print (bonusProb);

print (catDistr);
#normalizing
percentCatDistr=[0]*6;
for x in range (0,6):
    percentCatDistr[x]=catDistr[x]/43;

print (percentCatDistr);
print(sum(percentCatDistr))

#same stuff as above, except with all scores, not just the ones high enough to get the bonus
per1=[];
per2=[];
per3=[];
per4=[];
per5=[];
per6=[];
for x in range (0,106):
    per1.append(categoryPercent[x][0]);
    per2.append(categoryPercent[x][1]);
    per3.append(categoryPercent[x][2]);
    per4.append(categoryPercent[x][3]);
    per5.append(categoryPercent[x][4]);
    per6.append(categoryPercent[x][5]);
overallCatDistr= [sum(per1), sum(per2), sum(per3), sum(per4),sum(per5),sum(per6)];
for x in range (0,6):
    overallCatDistr[x]/=105;


#setting up the graph
#bar graph, since I am only dealing with discreet natural numbers
barWidth = 0.25
# y axis values
y2 = overallCatDistr
y1 = percentCatDistr
  
# x axis values
x2 = np.arange(len(y2))

# plotting the points 
plt.bar(x2+0.25, y1, color= "green", width=barWidth, label= "Percent of Scores > 62")
plt.bar(x2, y2, color= "red",width=barWidth, label= "Percent of Overall Scores" )

# naming the x axis
plt.xlabel('Category')
plt.xticks([r + barWidth for r in range(len(y2))], ['1', '2', '3', '4', '5','6'])
# naming the y axis
plt.ylabel('Average Percent of Scores')
  
# giving a title to my graph
plt.title('Category Weights')

plt.legend()
# function to show the plot
plt.show()
