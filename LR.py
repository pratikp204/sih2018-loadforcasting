from sklearn import cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import mutual_info_regression
import pandas as pd
import numpy as np

df = pd.read_csv('data/mergedData.csv')
df = df[24:]
train_y = np.asarray(df['load'])
train_x = np.array(df.drop(['date','hour','day','month','load'],1))
test_x = train_x[int(len(train_x)*0.9):]
test_y = train_y[int(len(train_x)*0.9):]
train_x = train_x[:int(len(train_x)*0.9)]
train_y = train_y[:int(len(train_y)*0.9)]
print mutual_info_regression(train_x, train_y)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(train_x,train_y,test_size=0.2)
clf = LinearRegression()
clf.fit(x_train, y_train)
print clf.coef_
print clf.score(test_x, test_y)*100
print clf.predict(test_x), test_y