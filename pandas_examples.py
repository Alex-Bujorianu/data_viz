import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# df = pd.read_excel('AdventureWorks2016Subset.xlsx')
# example_data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
# print(example_data['col1'].sum())
# print(example_data['col1'].iloc[0])
#
# df.groupby(['FullName']).apply(print)
# print(df.groupby(['FullName'])['SubTotal'].aggregate('sum'))
# df.groupby(['FullName'])['SubTotal'].aggregate('sum').to_csv('grouped_AdventureWorks')

budget = pd.read_excel('Budget.xlsx')
budget = budget = budget.tail(-2)
print(budget)