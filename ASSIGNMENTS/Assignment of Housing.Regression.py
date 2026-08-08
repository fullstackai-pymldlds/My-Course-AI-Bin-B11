import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'ASSIGNMENTS/housing.csv')
print(df)

print("df.shape:      " , df.shape)

df.plot.scatter(x='median_income', y='median_house_value', title='Scatter plot of median income and median house value percentages');
plt.show()

print("df.corr():      " , df.corr())

print("df.describe():      " , df.describe())

print(" df['median_income']:      " , df['median_income'])
print(" df['median_house_value']:      " , df['median_house_value'])

x = df['median_income'].values.reshape(-1, 1)
y = df['median_house_value'].values.reshape(-1, 1)

print("x:      " , x)
print("y:      " , y)

print(df['median_house_value'].value)
print(df['median_house_value'].value_shape())

print(x.shape)
print(x)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state= SEED)

print(X_train)
print(y_train)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

print(regressor.intercept_)

print(regressor.coef_)

def calc(slope, intercept, median_house_value):
    return slope * median_house_value + intercept

median_income = calc(regressor.coef_, regressor.intercept_, 9.5)
print(median_income)

median_income = regressor.predict([[9.5]])
print(median_income)

y_pred = regressor.predict(X_test)

df_pred = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_pred)

from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 median_income: {r2:.2f}')