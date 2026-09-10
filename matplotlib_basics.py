import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.bar(df["Name"], df["Marks"])

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.savefig("marks_chart.png")
print("Chart saved!")
