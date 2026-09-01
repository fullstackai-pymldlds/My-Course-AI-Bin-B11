import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'ASSIGNMENTS/insurance.csv')
print(df.head())

print("df.shape:      ", df.shape)

df.plot.scatter(x='bmi', y='charges', title='Scatter plot of bmi and charges')
plt.show()

print("df.corr():      ", df.corr(numeric_only=True))

print("df.describe():      ", df.describe())

print(" df['bmi']:      ", df['bmi'])
print(" df['charges']:      ", df['charges'])

x = df['bmi'].values.reshape(-1, 1)
y = df['charges'].values.reshape(-1, 1)

print("x:      ", x)
print("y:      ", y)

print(df['charges'].value_counts())
print(df['charges'].shape)

print(x.shape)
print(x)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(X_train)
print(y_train)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

print(regressor.intercept_)

print(regressor.coef_)

def calc(slope, intercept, bmi):
    return slope * bmi + intercept

charges = calc(regressor.coef_, regressor.intercept_, 30.0)
print(charges)

charges = regressor.predict([[30.0]])
print(charges)

y_pred = regressor.predict(X_test)

df_pred = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_pred)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 bmi: {r2:.2f}')