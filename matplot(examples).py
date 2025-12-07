import numpy as np
import matplotlib.pyplot as plt 
#sample data
x=np.arange(1,11)
y=np.random.randint(10,101,size=10)
#LINE Plot
plt.figure(figsize=(6,4))
plt.plot(x,y,marker='>',color='g',linestyle=':',label='line plot') 
plt.title('Line plot example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='lower right')
plt.show()
#bar plot
plt.figure(figsize=(6,4))
plt.bar(x,y,label='Bar plot') 
plt.title('Bar plot example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='lower right')
plt.show()
#scatter plot
plt.figure(figsize=(6,4))
plt.scatter(x,y,label='Bar plot') 
plt.title('Bar plot example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='lower right')
plt.show()
 
