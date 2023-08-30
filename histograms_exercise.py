import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv("Sales Data.csv")
sales_data['success_rate'] = sales_data['Orders_Taken'] / sales_data['Calls_Made']
print(sales_data)
# bin_edges = [0.65, 0.7, 0.75, 0.80, 0.85, 0.9, 0.95, 1.0]
# sales_data['bins'] = pd.cut(sales_data['success_rate'], bins=bin_edges)
# print(sales_data['bins'])
# sales_data['bins'].value_counts().plot(kind='bar')
plt.show()

grades = pd.read_csv("Grades Data.csv")
print(grades)
grades['average'] = grades[['Module 1 Grade', 'Module 2 Grade', 'Module 3 Grade', 'Module 4 Grade']].mean(axis=1)
print(grades)

def mean(row):
    "Take the mean of the columns in a row"
    return (row['Module 1 Grade'] + row['Module 2 Grade'] + row['Module 3 Grade'] + row['Module 4 Grade']) / 4

grades.drop('average', axis='columns', inplace=True)
grades['average'] = grades[['Module 1 Grade', 'Module 2 Grade', 'Module 3 Grade', 'Module 4 Grade']].apply(mean, axis=1)
print(grades)

# part three: calculating the gradients of a simple linear regression

advertising = pd.read_csv("advertising.csv")
x_bar = advertising['TV'].mean()
y_bar = advertising['Sales'].mean()
numerator = 0
for i in range(len(advertising['TV'])):
    numerator += (advertising['TV'].iloc[i] - x_bar) * (advertising['Sales'].iloc[i] - y_bar)
denominator = 0
for i in range(len(advertising['TV'])):
    denominator += (advertising['TV'].iloc[i] - x_bar)**2

m = numerator / denominator
print("m is ", m)
c = y_bar - m*x_bar
print("c is ", c)

def calculate_gradient_for_column(column_name: str):
    x_bar = advertising['TV'].mean()
    y_bar = advertising['Sales'].mean()
    numerator = 0
    for i in range(len(advertising[column_name])):
        numerator += (advertising[column_name].iloc[i] - x_bar) * (advertising['Sales'].iloc[i] - y_bar)
    denominator = 0
    for i in range(len(advertising[column_name])):
        denominator += (advertising[column_name].iloc[i] - x_bar) ** 2
    return numerator / denominator

print("Gradient of radio ", calculate_gradient_for_column('Radio'))
print("Gradient of newspaper ", calculate_gradient_for_column('Newspaper'))