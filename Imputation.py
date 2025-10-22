import pandas as pd
import numpy as np
import random

data=pd.read_csv('______')

y=data.target

predictor = data.drop('target', axis=1)
x=predictor.select_dtypes(exclude=['object'])

# train_test_split ka sasta version
tratio = 0.2
random.seed(0)
random.shuffle(data)
test_size = int(len(data) * tratio)
tt_data = data[:test_size]
tr_data = data[test_size:]
x_tr= tr_data.drop('target',axis=1)
y_tr= tr_data['target']
x_val=tt_data.drop('target',axis=1)
y_val = tt_data['target']

def score(x_tr, x_val, y_tr, y_val):
    num_trees=100
    r_ratio= 0.69 #kitna percent of all rows tree dekhenge
    c_ratio=0.69  #kitna percent of all columns har tree dekhega
    random.seed(0)
    mean_tree=[]
    tree_c=[]
    for i in range(num_trees):
        rows=x.sample(frac=r_ratio, replace=True,random_state=0)
        y_sample= y.loc[rows.index]
        cols=random.sample(list(x.columns),int(len(x.columns)*c_ratio))
        tree_c.append(cols)
        mean_tree=y_sample.mean()
        mean_tree.append(mean_tree)
    prd=np.mean(mean_tree)
    return np.mean(np.abs(y_val, prd))

#Imputation
imp_tr=x_tr.copy()
col_mean={}
for col in imp_tr.columns:
    mean= imp_tr[col].mean(skipna=True)
    imp_tr[col].fillna(mean, inplace=True)
    col_mean[col]=mean
imp_x_tr = imp_tr.copy()

imp_val=x_val.copy()
col_mean={}
for col in imp_val.columns:
    mean= imp_val[col].mean(skipna=True)
    imp_val[col].fillna(mean, inplace=True)
    col_mean[col]=mean
imp_x_val=imp_val.copy()

imp_x_tr.columns=x_tr.columns
imp_x_val.columns=x_val.columns

print("MAE : ")
print(score(imp_x_tr,imp_x_val,y_tr, y_val))