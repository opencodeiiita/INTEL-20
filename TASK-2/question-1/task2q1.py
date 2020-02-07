import numpy
data=numpy.genfromtxt(r'Salary_data.csv',delimeter=',')
data=numpy.delete(data,0,axis=0)
data=data[:,0]
data=data.T 
data=data.reshape(2,15)
print(numpy.linalg.pinv(data))