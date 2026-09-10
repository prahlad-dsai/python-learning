import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.plot(df["Name"], df["Marks"], marker="o")

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()
