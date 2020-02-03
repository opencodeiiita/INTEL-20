import matplotlib.pyplot as plot
import numpy as npy

from sklearn import ln
data=npy.genfromtxt(r'C:\Users\OneDrive\Desktop\INTEL-20\TASK-1\Question-1\Salary_Data.csv', delimiter=',')
data=npy.delete(data,0,axis=0)

x=dat[:,0]
y=dat[:,1]
x=x.reshape(-1,1)
regressn = ln.LinearRegression()
regressn.fit(x,y)
pred=regrssn.predict(x)

plot.scatter(x,y,color='red')
plot.plot(x,pred,color='blue')
plot.xlabel('Years Experience')
plot.ylabel('Salary')
plot.title('Linear Regression')

plot.show()
