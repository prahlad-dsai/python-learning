import pandas as pd

df = pd.read_csv("students.csv")


df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("Average marks:", df["Marks"].mean())

print("Highest marks:", df["Marks"].max())

print("Lowest marks:", df["Marks"].min())

print("\nStudents by department:")
print(df["Department"].value_counts())

print("\nAverage marks by department:")
print(df.groupby("Department")["Marks"].mean())

print("\nStudents with marks above 80:")
print(df[df["Marks"] > 80])
