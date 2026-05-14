import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tested.csv")

plt.hist(df['Age'].dropna(), bins=10, color='skyblue', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
df['Sex'].value_counts().plot(kind='bar', color=['pink','blue'])

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
