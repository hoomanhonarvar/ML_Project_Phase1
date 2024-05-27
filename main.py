import numpy as np
import pandas as pd
import random
from numpy import arange
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.model_selection import train_test_split, RepeatedKFold, GridSearchCV
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder,PolynomialFeatures

data=pd.read_csv("CreditPrediction.csv",na_values="Unknown")
pd.set_option('display.max_columns', None)



data=data.drop(columns=['Unnamed: 19','Gender'])

#deleting duplicated row
# finding repeated data
data=data.drop([0])
data=data.fillna({'Card_Category':data['Income_Category'].mode(),'Income_Category':data['Income_Category'].mode()
                  ,'Marital_Status':data['Marital_Status'].mode(),'Education_Level':data['Education_Level'].mode()})

data=data.dropna()
data.drop_duplicates(inplace=True)

# Ordinal Encoding
LE = LabelEncoder()
for cat in list([  'Income_Category', 'Card_Category','Marital_Status','Education_Level']):
    data[cat] = LE.fit_transform(data[cat])

#Scalling
for norm in data.columns:
    data[norm] = MinMaxScaler().fit_transform(data[norm].values.reshape(len(data), 1))

X = data.drop(['Credit_Limit'], axis = 1).astype(float).values
y = data['Credit_Limit'].astype(float).values

#Train test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 30)

ridge=Ridge(0.99)
ridge.fit(X_train,y_train)
y_ridge_predict=ridge.predict(X_test)
# define model evaluation method
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
# define grid
grid = dict()
grid['alpha'] = arange(0, 1, 0.01)
# define search
search = GridSearchCV(ridge, grid, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
# perform the search
results = search.fit(X_train, y_train)
# summarize
print('MAE: %.3f' % results.best_score_)
print('Config: %s' % results.best_params_)






lin_reg_1=LinearRegression()
lin_reg_1.fit(X_train,y_train)
poly_reg2 = PolynomialFeatures(degree=2)
X_poly = poly_reg2.fit_transform(X_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y_train)


poly_reg3 = PolynomialFeatures(degree=3)
X_poly3 = poly_reg3.fit_transform(X_train)
lin_reg_3 = LinearRegression()
lin_reg_3.fit(X_poly3, y_train)

Linear_y_test_pred=lin_reg_1.predict(X_test)
poly_reg2_y_test_pred=lin_reg_2.predict(poly_reg2.fit_transform(X_test))
poly_reg3_y_test_pred=lin_reg_3.predict(poly_reg3.fit_transform(X_test))
# poly_reg4_y_test_pred=lin_reg_4.predict(poly_reg4.fit_transform(X_test))



regressor = RandomForestRegressor(n_estimators=10, random_state=0, oob_score=True)
regressor.fit(X_train,y_train)
predict=regressor.predict(X_test)


# Performance
print("linear Regression:")
print(mean_squared_error(y_test, Linear_y_test_pred))
print(r2_score(y_test, Linear_y_test_pred))

print("p2 Regression:")
print(mean_squared_error(y_test, poly_reg2_y_test_pred))
print(r2_score(y_test, poly_reg2_y_test_pred))

print("p3 Regression:")
print(mean_squared_error(y_test, poly_reg3_y_test_pred))
print(r2_score(y_test, poly_reg3_y_test_pred))


print("Random Forest Regression:")
print(mean_squared_error(y_test, predict))
print(r2_score(y_test, predict))

print("ridge Regression:")
print(mean_squared_error(y_test, y_ridge_predict))
print(r2_score(y_test, y_ridge_predict))

