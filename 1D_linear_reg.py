import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

for line in open('1D_data.csv'):
    x,y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

#plt.scatter(X,Y)
#plt.show()


denominator = X.dot(X) - X.mean()*X.sum()
a = (Y.dot(X) - Y.mean()*X.sum())/ denominator
b = (Y.mean()*X.dot(X) - X.mean()*Y.dot(X))/ denominator


Yhat = a*X + b

print(a)
print(b)

plt.scatter(X,Y)
plt.plot(X,Yhat)
plt.show()

d1 = Y - Yhat
d2 = Y - Y.mean()

R2 = 1 - d1.dot(d1)/d2.dot(d2)

print(R2)


