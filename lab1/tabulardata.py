import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name":["A","B","C","D","E"],
    "Marks": [65,72,81,55,98]
}

df = pd.DataFrame(data)
print(df)
print(df["Marks"].mean())

plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

plt.hist(df["Marks"])
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Marks")
