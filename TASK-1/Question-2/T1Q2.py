import matplotlib.pyplot as plot
import pandas

x_train = pandas.read_csv("train.csv")
x_t = pandas.read_csv("test.csv")
x_trset = x_train.iloc[:, :-1].values
y_trset = x_train.iloc[:, -1].values
x_t = x_test.iloc[:, :-1].values
y_t = x_test.iloc[:, -1].values

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_trset, y_trset)

y_p = regressor.predict(x_t)

plot.scatter(x_t, y_t, color = 'blue')
plot.scatter(x_t, y_p, color = 'green')
plot.figtext(.2, .6, "Predicted result = green")
plot.figtext(.2, .7, "Test set result = blue")
plot.xlabel('Time invested')
plot.ylabel('Money(in lakh)')
plot.show