from sklearn import cross_validation
from sklearn.linear_model import LinearRegression
from FetchDataUnit import FetchData as fd
from sklearn.ensemble import GradientBoostingRegressor as GBR
from sklearn.ensemble import AdaBoostRegressor as ABR
from sklearn.feature_selection import mutual_info_regression
from sklearn import svm
import pandas as pd
import numpy as np
from sklearn import decomposition,svm
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor as mlpr
#from scipy.stats import pearsonr
from pickle import load,dumps

class Regression():

    def __init__(self):
        pass
        #self.default_hyprerparameter = default_hyprerparameter
        #self.epoch_loss = epoch_loss
        #self.batch_loss = batch_loss
        #self.epoch_accuracy = epoch_accuracy

    def read_dataset(self,input_set,n_components):
        if(n_components>15):
            n_components=15
        df=pd.DataFrame(input_set)
        # df = df[24:]
        # df['prevhr']=df.load.shift(+24)
        # df['lasthr'] = df.load.shift(+1)
        df = df[1:]
        df['hour2'] = pow(df['hour'],2)
        df['hour3'] = pow(df['hour'],3)
        df['hour4'] = pow(df['hour'],4)
        df['hour5'] = pow(df['hour'],5)
        df['t2'] = pow(df['temp'],2)
        df['weekday2'] = pow(df['weekday'],2)
        df['m2'] = pow(df['month'],2)
        df['m3'] = pow(df['month'],3)
        df['m4'] = pow(df['month'],4)
        train_y=np.asarray(input_set['load'])
        train_x=np.asarray(df.drop(['load','date']))
        scaler=MinMaxScaler()
        scaler.fit(train_x)
        train_x=scaler.transform(train_x)
        pca = decomposition.PCA(n_components=n_components)
        pca.fit(train_x)
        train_x = pca.transform(train_x)
        x_train, x_test, y_train, y_test = cross_validation.train_test_split(train_x, train_y, test_size=0.2)
        return x_train,x_test,y_train,y_test,scaler,pca
    def create_model(self):
        pass

    def train(self,zone,num,hidden_layer_size=(4),n_jobs=1,kernel='rbf',n_components=15,n_estimators=50,loss='linear',learning_rate=1.0):
        f=fd()
        input_set=f.getTrainData(zone)
        x_train, x_test, y_train, y_test,scaler,pca =self.read_dataset(input_set,n_components)
        if num==1:
            #Linear Regression
            clf=LinearRegression(n_jobs=n_jobs)
            clf.fit(x_train,y_train)
            # storeObj(clf,zone,clf.score(x_test,y_test),'Linear Regression')
            return clf,clf.score(x_test,y_test),'Linear Regression',scaler,pca
        elif num==2:
            # SVR sigmoid
            clf=svm.SVR(kernel=kernel)
            clf.fit(x_train,y_train)
            # storeObj(clf, zone, clf.score(x_test, y_test), 'SVR'+','+kernel)
            return clf,clf.score(x_test,y_test),'SVR'+kernel,scaler,pca
        elif num==3:
            #Neural Net
            clf=mlpr(hidden_layer_size=hidden_layer_size)
            clf.fit(x_train,y_train)
            str=''
            for i in hidden_layer_size:
                str+='-> {}'.format(i)
            # storeObj(clf, zone, clf.score(x_test, y_test), 'NeuralNet'+' hidden layer size'+hidden_layer_size)
            return clf,clf.score(x_test,y_test),'NeuralNet hidden_size'+str,scaler,pca
        elif num==4:
            #Gradient Boosting Regressor
            clf=GBR(loss=loss,n_estimators=n_estimators,learning_rate=learning_rate)
            clf.fit(x_train,y_train)
            # storeObj(clf, zone, clf.score(x_test, y_test), 'Gradient Boosting Regressor')
            return clf,clf.score(x_test,y_test),'Gradient Boosted Regressor',scaler,pca
        elif num==5:
            clf=ABR()
            clf.fit(x_train,y_train)
            # storeObj(clf, zone, clf.score(x_test, y_test), 'AdaBoost Regressor')
            return clf,clf.score(x_test,y_test),'AdaBoost Regressor',scaler,pca

    def test(self,model):
        pass

    @staticmethod
    def save_model(self,obj,zone,score,preobj,pca,name):
        du=dumps(obj)
        f=fd()
        f.storeObj(pickleobj=du,zone=zone,acc=score,preobj=preobj,pca=pca,name=name)

    @staticmethod
    def predict(self,input_x,name,zone):
        df=pd.DataFrame(input_x)
        df['hour2'] = pow(df['hour'],2)
        df['hour3'] = pow(df['hour'],3)
        df['hour4'] = pow(df['hour'],4)
        df['hour5'] = pow(df['hour'],5)
        df['t2'] = pow(df['temp'],2)
        df['weekday2'] = pow(df['weekday'],2)
        df['m2'] = pow(df['month'],2)
        df['m3'] = pow(df['month'],3)
        df['m4'] = pow(df['month'],4)
        f=fd()
        obj,preobj,pca=f.get_obj(name,zone)
        input_x=preobj.transform(input_x)
        input_x=pca.transform(input_x)
        return obj.predict(input_x)


if __name__=='__main__':
    r=Regression()
    clf,score,algo,scaler,pca=r.train(zone=1,num=1)
    print(score)
    Regression.save_model(clf,1,score,scaler,pca,'first test')