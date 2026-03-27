import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "Marks": [85, 78, 90, 65, 70, 88, 92],
    "Gender": ["Female", "Male", "Male", "Male", "Female", "Male", "Female"]
}

df = pd.DataFrame(data)

# Bar Chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("bar_chart.png")   # ✅ saves image
plt.show()

# Pie Chart
gender_count = df["Gender"].value_counts()

plt.figure()
plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.savefig("pie_chart.png")   # ✅ saves image
plt.show()

# Histogram
plt.figure()
plt.hist(df["Marks"])
plt.title("Distribution of Marks")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")
plt.savefig("histogram.png")   # ✅ saves image
plt.show()