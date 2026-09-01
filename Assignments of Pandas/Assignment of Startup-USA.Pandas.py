import pandas as pd

df = pd.read_csv("ASSIGNMENTS/Startup-USA.csv", delimiter=",")
print(df)

print("df - datatypes", df.dtypes)
print("df.info():    ", df.info())

print('last three rows:')
print(df.tail(3))

print('first three rows:')
print(df.head(3))

print("summary of statistics of dataframe using describe() method:", df.describe())

print("continuing the rows and columns of the dataframe using shape method:", df.shape)
print()

industry = df['Industry']

print("access the Industry column: df : ")
print(industry)
print()

industry_country = df[['Industry', 'Country']]
print("access multiple columns: df : ")
print(industry_country)
print()

second_row = df.loc[1]
print("#selecting a single row using .loc")
print(second_row)
print()

second_row2 = df.loc[[1, 3]]
print("#selecting multiple rows using .loc")
print(second_row2)
print()

second_row3 = df.loc[[1, 5]]
print("#selecting a slice of rows using .loc")
print(second_row3)
print()

second_row4 = df.loc[df['Industry'] == 'HealthTech']
print("#conditional selection of rows using .loc")
print(second_row4)
print()

second_row5 = df.loc[:1, 'Industry']
print("#selecting a single column using .loc")
print(second_row5)
print()

second_row6 = df.loc[:, ['Industry', 'Country']]
print("#selecting multiple columns using .loc")
print(second_row6)
print()

second_row7 = df.loc[:1, 'Funding Rounds':'Valuation (USD)']
print("#selecting a slice of columns using .loc")
print(second_row7)
print()

second_row8 = df.loc[df['Industry'] == 'HealthTech', 'Funding Rounds':'Valuation (USD)']
print("#combined row and column selection using .loc")
print(second_row8)
print()

print("# case 2 : using .loc with index_col - starts here")
df_index_col = pd.read_csv('ASSIGNMENTS/Startup-USA.csv', delimiter=",", index_col='Year Founded')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

second_row = df_index_col.loc[2012]
print("#Selecting a single row using .loc")
print(second_row)
print()

second_row2 = df_index_col.loc[[2012, 2016]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

second_row3 = df_index_col.loc[2006:2016]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

second_row4 = df_index_col.loc[df_index_col['Industry'] == 'HealthTech']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

second_row5 = df_index_col.loc[:2016, 'Industry']
print("#Selecting a single column using .loc")
print(second_row5)
print()

second_row6 = df_index_col.loc[:2016, ['Industry', 'Country']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

second_row7 = df_index_col.loc[:2016, 'Funding Rounds':'Valuation (USD)']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

second_row8 = df_index_col.loc[df_index_col['Industry'] == 'HealthTech', 'Funding Rounds':'Valuation (USD)']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

print("# Case 3 : Using .iloc - starts here")

second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

second_row2 = df_index_col.iloc[[1, 3, 5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

second_row5 = df_index_col.iloc[:, 2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

second_row6 = df_index_col.iloc[:, [2, 4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

second_row7 = df_index_col.iloc[:, 2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

second_row8 = df_index_col.iloc[[1, 3, 5], 2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

print("Next Run")

df.loc[len(df.index)] = ['Startup_5001', 'FinTech', 5, 2500000000.0, 8000000000.0, 45, 'USA', 2020, 75.5]
print("Modified DataFrame - add a new row:")
print(df)
print()

df.drop(1, axis=0, inplace=True)

df.drop(index=2, inplace=True)

df.drop([3, 5], axis=0, inplace=True)

print("Modified DataFrame - Remove Rows:")
print(df)

df.drop('Startup Name', axis=1, inplace=True)

df.drop(columns='Growth Rate (%)', inplace=True)

df.drop(['Number of Investors', 'Year Founded'], axis=1, inplace=True)

print("Modified DataFrame - delete Startup Name, Growth Rate (%), Number of Investors, Year Founded column:")
print(df)

df.rename(columns={'Investment Amount (USD)': 'InvestmentChanged'}, inplace=True)

df.rename(mapper={'Valuation (USD)': 'ValuationChanged', 'Funding Rounds': 'FundingRoundsChanged'}, axis=1, inplace=True)

print("Modified DataFrame - Rename Labels:")
print(df)

df.rename(index={0: 7}, inplace=True)

df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)

print("Modified DataFrame - Rename Row - 0 >>> 7 , 1 >>> 10 , 2 >>> 100 Labels:")
print(df)

selected_rows = df.query("Industry == 'HealthTech' or ValuationChanged > 10000000000")

print(selected_rows.to_string())
print(len(selected_rows))

sorted_df = df.sort_values(by='ValuationChanged')
print(sorted_df.to_string(index=False))

df1 = df.sort_values(by=['ValuationChanged', 'InvestmentChanged'])

print("Sorting by 'ValuationChanged' (ascending) and then by 'InvestmentChanged' (ascending):\n")
print(df1.to_string(index=False))

grouped = df.groupby('Industry')['InvestmentChanged'].sum()

print(grouped.to_string())
print("grouped:", len(grouped))

df_cleaned = df.dropna()
print("Cleaned Data:\n", df_cleaned)

df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)

data = [2, 4, 6, 8]

array1 = pd.array(data)
print(array1)

int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()