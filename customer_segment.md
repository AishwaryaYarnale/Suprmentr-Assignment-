## Customer Segmentation

**Problem Statement:**  
Segment customers into different groups using K-Means clustering based on their spending behavior.

---

**Dataset (Example):**

| Customer | Income (₹) | Spending Score |
|----------|-----------|----------------|
| 1        | 15,000    | 39             |
| 2        | 16,000    | 81             |
| 3        | 17,000    | 6              |
| 4        | 18,000    | 77             |
| 5        | 19,000    | 40             |

---

**Features:**  
- Annual Income  
- Spending Score  

---

**Model Used:**  
K-Means Clustering  

---

**Python Code:**
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dataset
data = np.array([
    [15000,39],
    [16000,81],
    [17000,6],
    [18000,77],
    [19000,40]
])

# Model
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Labels
labels = kmeans.labels_

# Plot
plt.scatter(data[:,0], data[:,1], c=labels)
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()
```

---

**Customer Groups (Example):**  
- Group 1: High income, high spending → Premium customers  
- Group 2: Low income, low spending → Budget customers  

---

**Conclusion:**  
K-Means clustering helps businesses understand different types of customers.  
This allows better marketing strategies and personalized offers.

---