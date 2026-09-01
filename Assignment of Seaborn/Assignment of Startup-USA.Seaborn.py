import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

sns.set_theme(style="darkgrid")

sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style="whitegrid")
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style="dark")
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style="white")
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style="ticks")
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'red', 'grid.color': 'black'})
sns.lineplot(x='x', y='y', data=data)
plt.show()

df = pd.read_csv('ASSIGNMENTS/Startup-USA.csv')

print(df.dtypes)
dffilter = df.head(40)
dffilter100 = df.head(100)

sns.set(style="whitegrid")

g = sns.displot(data=dffilter, x="Investment Amount (USD)", y="Valuation (USD)", hue="Industry", kind='hist')
g.figure.suptitle("sns.displot(data=dffilter, x='Investment Amount (USD)', y='Valuation (USD)', hue='Industry', kind='hist')")
g.figure.show()

g = input("wait for me....")

g = sns.displot(data=dffilter, x="Investment Amount (USD)", y="Valuation (USD)", kind='kde')
g.figure.show()
read = input("wait for me....")

g = sns.kdeplot(data=dffilter, x="Investment Amount (USD)")
g.figure.suptitle("sns.kdeplot(data=dffilter, x='Investment Amount (USD)')")
g.figure.show()
read = input("wait for me....")

g = sns.histplot(data=dffilter, x="Investment Amount (USD)", y="Valuation (USD)", hue="Industry", multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='Investment Amount (USD)', y='Valuation (USD)', hue='Industry', multiple='stack')")
g.figure.show()
read = input("wait for me....")

g = sns.scatterplot(x="Investment Amount (USD)", y="Valuation (USD)", data=dffilter)
g.figure.suptitle("sns.scatterplot(x='Investment Amount (USD)', y='Valuation (USD)', data=dffilter)")
g.figure.show()
read = input("wait for me....")

g = sns.lineplot(data=dffilter, x="Investment Amount (USD)", y="Valuation (USD)")
g.figure.suptitle("sns.lineplot(data=dffilter, x='Investment Amount (USD)', y='Valuation (USD)')")
g.figure.show()
read = input("wait for me....")

g = sns.barplot(data=dffilter, x="Industry", y="Valuation (USD)", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x='Industry', y='Valuation (USD)', legend=False)")
g.figure.show()
read = input("wait for me....")

g = sns.catplot(data=dffilter, x="Industry", y="Valuation (USD)")
g.figure.suptitle("sns.catplot(data=dffilter, x='Industry', y='Valuation (USD)')")
g.figure.show()
read = input("wait for me....")

glue = dffilter.pivot(columns='Industry', values='Valuation (USD)')
g = sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) - glue = dffilter.pivot(columns='Industry', values='Valuation (USD)')")
g.figure.show()
read = input("wait for me....")