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