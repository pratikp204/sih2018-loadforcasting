from sklearn import cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import mutual_info_regression
from sklearn.
import pandas as pd
import numpy as np
from sklearn import decomposition,svm
from sklearn import preprocessing
from sklearn.neural_network import MLPRegressor as mlpr
from scipy.stats import pearsonr
from pickle import load,dump


df = pd.read_csv('Constructed datasetV2.csv')
df = df[24:]
df['lasthr'] = df.load.shift(+1)
df = df[1:]
df['hour2']=df['Hour']**2
df['hour3']=df['Hour']**3
df['hour4']=df['Hour']**4
df['hour5']=df['Hour']**5
df['t2']=df['T']**2
df['weekday2']=df['weekday']**2
df['m2']=df['monthofyear']**2
df['m3']=df['monthofyear']**3
df['m4']=df['monthofyear']**4
df.to_csv('datasetv3.csv')
train_y = np.asarray(df['load'])
train_x = np.array(df.drop(['Date','load'],1))

test_y = train_y[int(len(train_x)*0.9):]
train_y = train_y[:int(len(train_y)*0.9)]
train_x = preprocessing.scale(train_x)
pca = decomposition.PCA(n_components=15)
pca.fit(train_x)
train_x = pca.transform(train_x)
test_x = train_x[int(len(train_x)*0.9):]
train_x = train_x[:int(len(train_x)*0.9)]
print mutual_info_regression(train_x, train_y)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(train_x,train_y,test_size=0.2)

clf2=svm.SVR(kernel='rbf')
clf2.fit(x_train,y_train)
print(clf2.score(test_x,test_y)*100)
print(clf2.predict(test_x),test_y[:10])
clf = LinearRegression()
clf.fit(x_train, y_train)
print clf.score(test_x, test_y)*100
print clf.predict(test_x), mutual_info_regression(train_x, train_y)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(train_x,train_y,test_size=0.2)

clf = LinearRegression()
clf.fit(x_train, y_train)
print(clf.score(test_x, test_y)*100)
print(clf.predict(test_x), test_y[:10])
