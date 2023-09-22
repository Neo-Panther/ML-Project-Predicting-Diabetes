import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('preprocessed.csv', index_col=0)
f, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(dataset.corr(), linewidths=0.5, ax=ax, annot=True)
plt.show()