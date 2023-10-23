import numpy as np
import math
#DATA SET
X=np.array([[35,35,3],[22,50,2],[63,200,1],[59,170,1],[25,40,4]])
Y=np.array([[0,1,0,0,1]])

age=int(input("AGE : "))
income=int(input("INCOME : "))
no_credit_cards=int(input("NUMBER OF CREDIT CARDS : "))
ip=np.array([[age,income,no_credit_cards]])

def euclide(x,y):
    dis_list=[]
    for i in range(x.shape[0]):
        result=0
        for j in range(x.shape[1]):
            result+=(x[i][j]-y[0][j])**2
        dis_list.append(math.sqrt(result))
    return dis_list

def voting(index,y):
    count_0=0
    count_1=0
    for i in index:
        if y[0][i] == 0:
            count_0+=1
        else:
            count_1+=1
        if(count_1>count_0):
            return "YES"
        else:
            return "NO"
        
class KNN_classifier:
    def __init__(self,k):
        self.k=k

    def fit(self,X,y):
        self.X=X
        self.y=y

    def predict(self,X_predict):
        self.X_predict=X_predict
        dis_list=euclide(self.X,self.X_predict)
        index=np.argsort(dis_list)[:self.k]
        return voting(index,self.y)
    
knn_model=KNN_classifier(k=3)
knn_model.fit(X,Y)
predict=knn_model.predict(ip)
print(predict)



        
        
        




        
    

