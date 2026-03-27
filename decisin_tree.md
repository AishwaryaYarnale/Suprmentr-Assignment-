## Decision Tree on Paper

**Problem Statement:**  
Draw a decision tree to predict whether you should play outside based on weather conditions.

---

**Features (Input):**  
- Weather (Sunny / Rainy / Cloudy)  
- Temperature (Hot / Mild / Cool)  
- Humidity (High / Normal)  

---

**Output:**  
- Play Outside (Yes / No)  

---

**Decision Tree:**

```
            Weather
           /   |    \
       Sunny Rainy  Cloudy
        /              \
   Humidity           Yes
   /      \
High      Normal
 No         Yes
```

---

**Explanation:**  
- If weather is **Rainy** → Do not play  
- If weather is **Cloudy** → Play  
- If weather is **Sunny**:
  - High humidity → Do not play  
  - Normal humidity → Play  

---

**Conclusion:**  
Decision Trees help in making decisions based on conditions.  
They are easy to understand and used in many real-life problems.

---