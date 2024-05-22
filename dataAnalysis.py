import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
data=pd.read_csv("CreditPrediction.csv")
# print(data.columns)





# creating box plot of features

boxplot = data.boxplot(column=["Avg_Utilization_Ratio"],grid=True, fontsize=15)
plt.savefig("./pic/Avg_Utilization_Ratio.png")
boxplot = data.boxplot(column=["Total_Ct_Chng_Q4_Q1"],grid=True, fontsize=15)
plt.savefig("./pic/Total_Ct_Chng_Q4_Q1.png")
boxplot = data.boxplot(column=["Total_Trans_Ct"],grid=True, fontsize=15)
plt.savefig("./pic/Total_Trans_Ct.png")
boxplot = data.boxplot(column=["Total_Trans_Amt"],grid=True, fontsize=15)
plt.savefig("./pic/Total_Trans_Amt.png")
boxplot = data.boxplot(column=["Total_Amt_Chng_Q4_Q1"],grid=True, fontsize=15)
plt.savefig("./pic/Total_Amt_Chng_Q4_Q1.png")
boxplot = data.boxplot(column=["Total_Revolving_Bal"],grid=True, fontsize=15)
plt.savefig("./pic/Total_Revolving_Bal.png")
boxplot = data.boxplot(column=["Contacts_Count_12_mon"],grid=True, fontsize=15)
plt.savefig("./pic/Contacts_Count_12_mon.png")
boxplot = data.boxplot(column=["Months_Inactive_12_mon"],grid=True, fontsize=15)
plt.savefig("./pic/Months_Inactive_12_mon.png")
boxplot = data.boxplot(column=["Total_Relationship_Count"],grid=True, fontsize=15)
plt.savefig("./pic/Total_Relationship_count.png")
boxplot = data.boxplot(column=["Months_on_book"],grid=True, fontsize=15)
plt.savefig("./pic/Months_on_book.png")
boxplot = data.boxplot(column=["Dependent_count"],grid=True, fontsize=15)
plt.savefig("./pic/Dependent_count.png")
boxplot = data.boxplot(column=["Customer_Age"],grid=True, fontsize=15)
plt.savefig("./pic/Customer_Age.png")


proportion_education = data['Education_Level'].value_counts()
proportion_education = pd.DataFrame(proportion_education)
proportion_education = proportion_education.rename(columns={'Education_Level':'Count'})
proportion_education = proportion_education.rename_axis('Education_Level').reset_index()
plt.figure(figsize = (15, 7))

percentage = []
for i in proportion_education['count']:
  pct = (i / proportion_education['count'].sum()) * 100
  percentage.append(round(pct, 2))
proportion_education['Percentage'] = percentage

## Show the plot
plots = sns.barplot(x = "Education_Level",
                    y = "Percentage",
                    data = proportion_education)

## Show the annotation
for p in plots.patches:
  plots.annotate('{} %'.format(p.get_height().astype('float')),
                 (p.get_x() + p.get_width() / 2, p.get_height()),
                 ha='center', va='center',
                 size=15, xytext=(0, 8),
                 textcoords='offset points')

# Setting the label for x-axis
plt.xlabel("Education Level", size=14)
# Setting the label for y-axis
plt.ylabel("Percentage", size=14)
# Setting the title for the graph
plt.title("Percentage of Education Level", size = 16, weight = 'semibold')
# Fianlly showing the plot
plt.savefig("./pic/Education_Level.png")



proportion_marital_status = data['Marital_Status'].value_counts()
proportion_marital_status = pd.DataFrame(proportion_marital_status)
proportion_marital_status = proportion_marital_status.rename(columns={'Marital_Status':'count'})
proportion_marital_status = proportion_marital_status.rename_axis('Marital_Status').reset_index()

# Show the proportion of education in bar chart
plt.figure(figsize = (15, 7))

percentage = []
for i in proportion_marital_status['count']:
  pct = (i / proportion_marital_status['count'].sum()) * 100
  percentage.append(round(pct, 2))
proportion_marital_status['Percentage'] = percentage

## Show the plot
plots = sns.barplot(x = "Marital_Status",
                    y = "Percentage",
                    data = proportion_marital_status)

## Show the annotation
for p in plots.patches:
  plots.annotate('{} %'.format(p.get_height().astype('float')),
                 (p.get_x() + p.get_width() / 2, p.get_height()),
                 ha='center', va='center',
                 size=15, xytext=(0, 8),
                 textcoords='offset points')

# Setting the label for x-axis
plt.xlabel("Marital Status", size=14)
# Setting the label for y-axis
plt.ylabel("Percentage", size=14)
# Setting the title for the graph
plt.title("Percentage of Marital Status", size = 16, weight = 'semibold')
# Fianlly showing the plot
plt.savefig("./pic/Marital Status")


proportion_income_category = data['Income_Category'].value_counts()
proportion_income_category = pd.DataFrame(proportion_income_category)
proportion_income_category = proportion_income_category.rename(columns={'Income_Category':'count'})
proportion_income_category = proportion_income_category.rename_axis('Income_Category').reset_index()

# Show the proportion of education in bar chart
plt.figure(figsize = (15, 7))

percentage = []
for i in proportion_income_category['count']:
  pct = (i / proportion_income_category['count'].sum()) * 100
  percentage.append(round(pct, 2))
proportion_income_category['Percentage'] = percentage

## Show the plot
plots = sns.barplot(x = "Income_Category",
                    y = "Percentage",
                    data = proportion_income_category)

## Show the annotation
for p in plots.patches:
  plots.annotate('{} %'.format(p.get_height().astype('float')),
                 (p.get_x() + p.get_width() / 2, p.get_height()),
                 ha='center', va='center',
                 size=15, xytext=(0, 8),
                 textcoords='offset points')

# Setting the label for x-axis
plt.xlabel("Income Category", size=14)
# Setting the label for y-axis
plt.ylabel("Percentage", size=14)
# Setting the title for the graph
plt.title("Percentage of Income Category", size = 16, weight = 'semibold')
# Fianlly showing the plot
plt.savefig("./pic/Income.png")


proportion_card_category = data['Card_Category'].value_counts()
proportion_card_category = pd.DataFrame(proportion_card_category)
proportion_card_category = proportion_card_category.rename(columns={'Card_Category':'count'})
proportion_card_category = proportion_card_category.rename_axis('Card_Category').reset_index()

# Show the proportion of education in bar chart
plt.figure(figsize = (15, 7))

percentage = []
for i in proportion_card_category['count']:
  pct = (i / proportion_card_category['count'].sum()) * 100
  percentage.append(round(pct, 2))
proportion_card_category['Percentage'] = percentage

## Show the plot
plots = sns.barplot(x = "Card_Category",
                    y = "Percentage",
                    data = proportion_card_category)

## Show the annotation
for p in plots.patches:
  plots.annotate('{} %'.format(p.get_height().astype('float')),
                 (p.get_x() + p.get_width() / 2, p.get_height()),
                 ha='center', va='center',
                 size=15, xytext=(0, 8),
                 textcoords='offset points')

# Setting the label for x-axis
plt.xlabel("Card Category", size=14)
# Setting the label for y-axis
plt.ylabel("Percentage", size=14)
# Setting the title for the graph
plt.title("Percentage of Card Category", size = 16, weight = 'semibold')
plt.savefig("./pic/Card_Category.png")


dfk = data.select_dtypes(include = ['int64', 'float64']) # memilih kolom numerik
k = len(dfk.columns)
cm = dfk.corr()
plt.figure(figsize = (14, 10))
sns.heatmap(cm, annot = True, cmap = 'viridis')
plt.savefig("./pic/correlation_matrix.png")


data=data.drop(columns=['CLIENTNUM'])

