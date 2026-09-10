import numpy as np

marks = np.array([78, 65, 92, 55, 88, 73, 95, 60])

print("Mean:", marks.mean())
print("Median:", np.median(marks))
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Standard deviation:", marks.std())
print(marks[marks > 75])
print(marks[marks < 70])
print(len(marks[marks > 75]))
