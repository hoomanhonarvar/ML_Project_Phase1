import numpy as np
import pandas as pd
import random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder,PolynomialFeatures
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE




data=pd.read_csv("CreditPrediction.csv")
pd.set_option('display.max_columns', None)


print(data.columns)

# data_analysis
data=data.drop(columns=['Unnamed: 19'])
# print(data.describe())
#deleting duplicated row
data.drop_duplicates(inplace=True)
# finding repeated data

data=data.fillna(method='bfill')
data=data.drop(data.index[data["Credit_Limit"]=="x.0"][0])
#Scalling
stand_var = ['Customer_Age', 'Months_on_book', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1']
norm_var = ['Dependent_count', 'Total_Relationship_Count', 'Months_Inactive_12_mon', 'Contacts_Count_12_mon',
            'Total_Revolving_Bal', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Avg_Utilization_Ratio']

for stand in data[stand_var]:
    data[stand] = StandardScaler().fit_transform(data[stand].values.reshape(len(data), 1))
for norm in data[norm_var]:
    data[norm] = MinMaxScaler().fit_transform(data[norm].values.reshape(len(data), 1))


# Ordinal Encoding
LE = LabelEncoder()
for cat in list([ 'Education_Level', 'Income_Category', 'Card_Category']):
    data[cat] = LE.fit_transform(data[cat])

# Nominal Encoding
nominal_cats = ['Gender', 'Marital_Status']
for cat in nominal_cats:
    onehot = pd.get_dummies(data[cat], prefix = cat)
    data = data.join(onehot)

data = data.drop(['Gender', 'Marital_Status'], axis = 1)


X = data.drop(['Credit_Limit'], axis = 1).astype(float).values
y = data['Credit_Limit'].astype(float).values
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')

#Train test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 30)

# #balancing data
# smote = SMOTE(random_state = 0)
# X_resampled, y_resampled = smote.fit_resample(X_train, y_train)



lin_reg=LinearRegression()
lin_reg.fit(X_train,y_train)

poly_reg2 = PolynomialFeatures(degree=2)
X_poly = poly_reg2.fit_transform(X_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y_train)

poly_reg3 = PolynomialFeatures(degree=3)
X_poly3 = poly_reg3.fit_transform(X_train)
lin_reg_3 = LinearRegression()
lin_reg_3.fit(X_poly3, y_train)



Linear_y_test_pred=lin_reg.predict(X_test)
poly_reg2_y_test_pred=lin_reg_2.predict(X_test)
poly_reg3_y_test_pred=lin_reg_3.predict(X_test)

