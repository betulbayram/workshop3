import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Salary_Data.csv")

# print(data.head())

x = data["YearsExperience"]
y = data["Salary"]

plt.scatter(x, y, c=data["Salary"], alpha=1)

plt.title("Maaş - Deneyim Grafiği")

plt.xlabel("Deneyim")
plt.ylabel("Maaş")

plt.show()