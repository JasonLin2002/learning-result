import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_set = pd.read_csv("iris.csv")
df = pd.DataFrame(data_set)

sns.boxplot(x="species", y="petal_length", data=df)
plt.show()