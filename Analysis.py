import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

nums = {}
for i in range(2013,2021+1):
    if i != 2014:
        nums[i]=[]

with open("valence.csv", "r") as f:
    for line in f:            
        yr = int(line.split(",")[0])
        valence = int(line.split("\n")[0].split(",")[1])
        #print(yr, valence)
        nums[yr].append(valence/100)

'''
plt.boxplot([nums[i] for i in nums.keys()])

plt.xticks([i+1 for i in range(8)], [i for i in nums.keys()])

plt.title("Boxplot of Valence Values of Top 10 Songs By Year")
plt.ylabel("Valence")

plt.show()
'''


happy = {2013:7.08,
         2015:7.12,
         2016:7.1,
         2017:6.99,
         2018:6.89,
         2019:6.89,
         2020:6.95,
         2021:6.98
         }
x = [happy[i]/10 for i in happy.keys()]
y = [sum(nums[i])/len(nums[i]) for i in nums.keys()]
plt.scatter(x, y)

bfl = stats.linregress(x,y)

plt.plot(x, [i*bfl.slope+bfl.intercept for i in x], color="black")

#with open("scatter.csv", "w") as f:
#    for i in range(len(x)):
#        f.write(str(x[i])+","+str(y[i])+"\n")

plt.ylabel("Mean Valence")
plt.xlabel("Happiness Index")
plt.title("Scatterplot of Mean Valence Against Happiness Index")

plt.show()

print(bfl)

