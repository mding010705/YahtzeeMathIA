import matplotlib.pyplot as plt
import UpperSection as US  
# x axis values
x = [0,1,2,3,4,5]
# corresponding y axis values
y = US.upperSection()

label= x
# plotting the points 
plt.bar(x, y, tick_label= label, width=0.8, color= "green")
  
# naming the x axis
plt.xlabel('# Matching Dice')
# naming the y axis
plt.ylabel('Probability')
  
# giving a title to my graph
plt.title('Binomial Distribution of 3rd Roll')

plt.legend()
# function to show the plot
plt.show()
