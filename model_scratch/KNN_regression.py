import numpy as np
import math
#DATA SET
X=np.array([1000,1500,2000,2500])
Y=np.array([50000,75000,100000,125000])
ip=int(input("NHẬP DIỆN TÍCH NHÀ CẦN DỰ ĐOÁN : "))

def average(index,value):
    value_with_index=[]
    for i in index:
        value_with_index.append(value[i])
    return sum(value_with_index)/len(value_with_index)

def euclide(X,x):
    dis_list=[]
    for i in X:
        dis_list.append(abs(i-x))
    return dis_list

# index=[2,1,3]

# print(average(index,Y))
class KNN_regress:
    def __init__(self,k):
        self.k=k
    def fit(self,X,y):
        self.X=X
        self.y=y
        
    def predict(self,input):
        item_list=[]
        self.input=input
        dis_list=euclide(self.X,self.input)
        index=np.argsort(dis_list)[:self.k]
        return(average(index,self.y))

knn_regression=KNN_regress(k=3)
knn_regression.fit(X,Y)
predict=knn_regression.predict(ip)
print(predict)