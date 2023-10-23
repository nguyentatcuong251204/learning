import numpy as np
import random

#CREATE DATASET
x=np.random.uniform(0,10,100)
noise=np.random.uniform(-1,1,100)
y=2*x+1+noise
n=len(x)
#BUILD MODEL LINEAR REGRESSION
class linear_regression():
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y

    
    def fit(self,X,Y):
        epochs=1000
        a=0
        b=0
        def gradient_descent(a,b):
            lr=0.01
            a_gradient=0
            b_gradient=0
            for i in range(n):
                a_gradient+=(-2/100)*(self.X[i])*(self.Y[i]-(a*self.X[i]+b))
                b_gradient+=(-2/100)*(self.Y[i]-(a*self.X[i]+b))
            a=a-lr*a_gradient
            b=b-lr*b_gradient
            return a,b
        for i in range(epochs):
            a,b=gradient_descent(0,0)
        return a,b
    
    
    def predict(self,x):
        a,b=self.fit(self.X,self.Y)
        print(a) 

li_reg=linear_regression(x,y)

a,b=li_reg.fit(x,y)
value=int(input("NHAP X CAN DU DOAN : "))
print(a*value+b)

        

