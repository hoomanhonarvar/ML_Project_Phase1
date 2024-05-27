import pandas as pd
import random
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
data=pd.read_csv("CreditPrediction.csv")
pd.set_option('display.max_columns', None)


print(data.columns)

# data_analysis
data=data.drop(columns=['Unnamed: 19'])
# print(data.describe())
#deleting duplicated row
data.drop_duplicates(inplace=True)
# finding repeated data

for i in data.itertuples():
    if i[2]<=0:
        data.iloc[i[0]][1]=10
        data.at[i[0], "Customer_Age"] = data.loc[:, "Customer_Age"].mean()
    if i[3]!='F' and i[3]!='M':
        data.at[i[0], "Gender"] = random.choice(['F','M'])
    if i[4]<0:
        data.at[i[0], "Card_Category"]=data.loc[:,"Dependent_count"].mean()
    if i[5]!="Graduate" and i[5]!="College"and i[5]!="High School"and i[5]!="Post-Graduate"and i[5]!="Uneducated"and i[5]!="Unknown"and i[5]!="Doctorate":
        data.at[i[0],"Education_Level"]="Unknown"
    if i[6]!="Single" and i[6]!="Married"and i[6]!="Unknown"and i[6]!="Divorced":
        data.at[i[0],"Marital_Status"]="Unknown"

    if i[8] != "Blue" and i[8] != "Silver" and i[6] != "Gold" and i[6] != "Plantium":
        Card_Category=["Blue","Silver","Gold","Plantium"]
        data.at[i[0],"Card_Category"] = random.choice(Card_Category) #RANDOM
    if i[9]<0:
        data.at[i[0], "Months_on_book"]=data.loc[:,"Months_on_book"].mean()
    if i[10]<0:
        data.at[i[0], "Total_Relationship_count"]=data.loc[:,"Total_Relationship_count"].mean()
    if i[11]<0:
        data.at[i[0], "Months_Inactive_12_mon"]=data.loc[:,"Months_Inactive_12_mon"].mean()
    if i[12]<0:
        data.at[i[0], "Contacts_Count_12_mon"]=data.loc[:,"Contacts_Count_12_mon"].mean()

    if i[14]<0:
        data.at[i[0], "Total_Revolving_Bal"]=data.loc[:,"Total_Revolving_Bal"].mean()
    if i[15]<0:
        data.at[i[0], "Total_Amt_Chng_Q4_Q1"]=data.loc[:,"Total_Amt_Chng_Q4_Q1"].mean()
    if i[16]<0:
        data.at[i[0], "Total_Trans_Amt"]=data.loc[:,"Total_Trans_Amt"].mean()
    if i[17]<0:
        data.at[i[0], "Total_Trans_Ct"]=data.loc[:,"Total_Trans_Ct"].mean()
    if i[18]<0:
        data.at[i[0], "Total_Ct_Chng_Q4_Q1"]=data.loc[:,"Total_Ct_Chng_Q4_Q1"].mean()
    if i[19]<0:
        data.at[i[0], "Avg_Utilization_Ratio"]=data.loc[:,"Avg_Utilization_Ratio"].mean()
# x = data.values #returns a numpy array
# min_max_scaler = preprocessing.MinMaxScaler()
# x_scaled = min_max_scaler.fit_transform(x)
# data = pd.DataFrame(x_scaled)
# print(data)



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


print(data)