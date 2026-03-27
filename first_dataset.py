import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
study_hours = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
marks = np.array([35,40,50,60,65,70,80,85])

# Model
model = LinearRegression()
model.fit(study_hours, marks)

# Prediction
predicted_marks = model.predict(study_hours)

# Graph
plt.scatter(study_hours, marks, label="Actual Data")
plt.plot(study_hours, predicted_marks, label="Prediction Line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()

plt.show()

# Example prediction
print("Marks for 9 hours study:", model.predict([[9]]))