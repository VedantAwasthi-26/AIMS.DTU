import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer

data=pd.read_csv('______')

y=data.target

predictor = data.drop('target', axis=1)
x=predictor.select_dtypes(exclude=['object'])

x_tr, x_val, y_tr, y_val=train_test_split(x,y,tr_size=0.8, test_size=0.2,random_state=0)

def score(x_tr, x_val, y_tr, y_val):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(x_tr,y_tr)
    prd= model.predict(x_val)
    return mean_absolute_error(y_val, prd)

#Imputation
imputer=SimpleImputer()
imp_x_tr=pd.DataFrame(imputer.fit_transform(x_tr))
imp_x_val=pd.DataFrame(imputer.transform(x_val))

imp_x_tr.columns=x_tr.columns
imp_x_val.columns=x_val.columns

print("MAE : ")
print(score(imp_x_tr,imp_x_val,y_tr, y_val))
