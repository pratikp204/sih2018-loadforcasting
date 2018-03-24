import tensorflow as tf
from sklearn.datasets import load_iris


def input_evaluation_fn():
    features={'column1':np.array([]),
              'column2':np.array([]),
              'column3':np.array([]),
              'column4':np.array([])}
    labels=np.array([])
    return features,labels

def train_input_fn(features,labels,batch_size):
    '''An input function for training'''
    #convert the inputs to a dataset
    dataset=tf.data.Dataset.from_tensor_slices((dict(features),labels))

    #shuffle,repeat and batch the examples

    return dataset.shuffle(1000).repeat().batch(batch_size)

# define the feature columns

my_feature_columns=[]
for key in train_x.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))


#instantiate an estimator

#build a DNN with 2 hidden layers and 10 nodes in each hidden layer

classifier=tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    #two hidden layers of 10 nodes each
    hidden_units=[10,10],
    n_classes=3
)

#train,Evaluate, predict
#train
classifier.train(input_fn=lambda : iris_data.train_input_fn(train_x,train_y,args.batch_size),
                 steps=args.train_steps)
#evaluate
eval_result=classifier.evaluate(
    input_fn=lambda :iris_data.eval_input_fn(test_x,test_y,args.batch_size)
)
#make predictions

expected=['setosa','class2','class3']
predict_x={
    'column1':np.array([]),
    'column2':np.array([]),
    'column3':np.array([])
}

predictions=classifier.predict(
    input_fn=lambda:iris_data.eval_input_fn(predict_x,batch_size=args.batch_size)
    
)

