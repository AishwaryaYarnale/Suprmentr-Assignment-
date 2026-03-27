## KNN in Real Life

**Problem Statement:**  
Explain how K-Nearest Neighbors (KNN) works in real life using Netflix-like recommendations.

---

**What is KNN?**  
KNN (K-Nearest Neighbors) is a Machine Learning algorithm that finds similar items or users based on distance or similarity.

---

**Real-Life Example (Netflix Recommendation):**  
Netflix recommends movies based on users with similar tastes.

- If two users like similar movies  
- Then Netflix suggests movies liked by one user to the other  

👉 KNN finds "nearest neighbors" (similar users)

---

**How it Works:**  
1. Take a user  
2. Find other users with similar watching history  
3. Recommend movies those similar users liked  

---

**Small Similarity Example:**

| User | Action | Comedy | Drama |
|------|--------|--------|-------|
| A    | 5      | 3      | 2     |
| B    | 4      | 3      | 2     |
| C    | 1      | 5      | 4     |

- User A is more similar to User B  
- User A is less similar to User C  

👉 So, recommend movies liked by User B to User A

---

**Conclusion:**  
KNN helps find similar users or items and gives recommendations based on similarity.  
It is widely used in apps like Netflix, Amazon, and Spotify.

---