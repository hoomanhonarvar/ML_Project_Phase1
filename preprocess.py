import pandas as pd
import random

data=pd.read_csv("CreditPrediction.csv")
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
        data.at[i[0], "Gender"] = random.choice(["F","M"])
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

    if i[3]=="F":
        data.at[i[0], "Gender"]=0
    if i[3]=="M":
        data.at[i[0], "Gender"]=1
    if i[5]=="Unknown":
        data.at[i[0], "Education_Level"]=0
    if i[5]=="Uneducated":
        data.at[i[0], "Education_Level"]=1
    if i[5]=="High School":
        data.at[i[0], "Education_Level"]=2
    if i[5]=="College":
        data.at[i[0], "Education_Level"]=3
    if i[5]=="Graduate":
        data.at[i[0], "Education_Level"]=4
    if i[5]=="Post-Graduate":
        data.at[i[0], "Education_Level"]=5
    if i[5]=="Doctorate":
        data.at[i[0], "Education_Level"]=6