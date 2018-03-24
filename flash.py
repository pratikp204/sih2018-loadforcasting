from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import pandas as pd
import tensorflow as tf
import numpy as np

#from sklearn import cross_validation
#from sklearn.linear_model import LinearRegression
#from sklearn.feature_selection import mutual_info_regression
import pandas as pd
import numpy as np
#from sklearn import decomposition
#from sklearn import preprocessing
#from scipy.stats import pearsonr
tf.logging.set_verbosity(tf.logging.INFO)

df=pd.read_csv('datasetv3.csv')
test_set = df[int(len(df)*0.9):(len(df)-10)]
predict_set=df[(len(df)-10):]
training_set=df[:int(len(df)*0.9)]
features=['monthofyear','dayofmonth','weekday','Hour','T','lasthr','hour2','hour3','hour4','hour5','t2','weekday2','m2','m3','m4']
label='load'

feature_cols = [tf.feature_column.numeric_column(k) for k in features]

#train_x = preprocessing.scale(train_x)

regressor=tf.estimator.DNNRegressor(
    feature_columns=feature_cols,
    hidden_units=[],
    optimizer=tf.train.ProximalAdagradOptimizer(learning_rate=0.1)
)

def get_input_fn(data_set,num_epochs=None,shuffle=True):
    return tf.estimator.inputs.pandas_input_fn(
        x=pd.DataFrame({k: data_set[k].values for k in features}),
        y=pd.Series(data_set[label].values),
        num_epochs=num_epochs,
        shuffle=shuffle
    )

regressor.train(input_fn=get_input_fn(training_set))

ev=regressor.evaluate(input_fn=get_input_fn(test_set,num_epochs=1,shuffle=False))

loss_score = ev["loss"]
print('Loss : {0:f}'.format(loss_score))

y=regressor.predict(input_fn=get_input_fn(predict_set,num_epochs=1,shuffle=False))
print(y)

