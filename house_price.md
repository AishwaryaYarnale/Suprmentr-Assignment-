# ML Assignments

---

### House Price Predictor

**Problem Statement:**  
Predict house prices using Machine Learning based on area.

**Dataset:**

| Area (sq ft) | Price (₹ lakhs) |
|-------------|----------------|
| 500         | 20             |
| 800         | 30             |
| 1000        | 40             |
| 1200        | 50             |
| 1500        | 65             |

**Features & Label:**  
- Feature (Input): Area (sq ft)  
- Label (Output): Price  

**Model Used:**  
Linear Regression  

**Python Code:**
```python
import numpy as np
from sklearn.linear_model import LinearRegression

area = np.array([500,800,1000,1200,1500]).reshape(-1,1)
price = np.array([20,30,40,50,65])

model = LinearRegression()
model.fit(area, price)

print("Price for 1300 sq ft:", model.predict([[1300]]))
```

**Prediction:**  
For 1300 sq ft → approx ₹55–60 lakhs  

**Conclusion:**  
As area increases, price increases.

---

### Spam Classifier Thinking

**Problem Statement:**  
Detect spam messages.

**Features:**
- Message text  
- Keywords (win, free, offer)  
- Links  
- Sender  

**Data Needed:**
- Messages labeled as Spam / Not Spam  

**Output:**  
Spam or Not Spam  

**Mistakes:**
- False Positive  
- False Negative  

**Examples:**
- "Win ₹1000 now!!!" → Spam  
- "Meeting at 5 PM" → Not Spam  

**Conclusion:**  
Helps filter unwanted messages.