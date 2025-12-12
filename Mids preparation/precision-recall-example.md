Here is **the simplest possible example** to understand **Precision**, **Recall**, and **F1-score**.

---

# 🔹 Scenario

Suppose you built a classifier to detect **spam emails**.

You tested it on **10 emails**:

* **Actual spam emails:** 4
* **Actual non-spam emails:** 6

Your model predicted:

| Email | Actual   | Predicted |
| ----- | -------- | --------- |
| 1     | Spam     | Spam      |
| 2     | Spam     | Spam      |
| 3     | Spam     | Not Spam  |
| 4     | Spam     | Not Spam  |
| 5     | Not Spam | Spam      |
| 6     | Not Spam | Not Spam  |
| 7     | Not Spam | Not Spam  |
| 8     | Not Spam | Not Spam  |
| 9     | Not Spam | Not Spam  |
| 10    | Not Spam | Spam      |

Now count:

* **True Positives (TP)** = predicted Spam AND actual Spam → **2**
* **False Positives (FP)** = predicted Spam but actual Not Spam → **2**
* **False Negatives (FN)** = predicted Not Spam but actual Spam → **2**

---

# ✔️ **Precision**

**Out of all predicted Spam, how many were actually Spam?**

$$
\text{Precision} = \frac{TP}{TP + FP} = \frac{2}{2 + 2} = \frac{2}{4} = 0.5
$$

➡️ **Precision = 50%**

---

# ✔️ **Recall**

**Out of all actual Spam emails, how many did the model correctly find?**

$$
\text{Recall} = \frac{TP}{TP + FN} = \frac{2}{2 + 2} = \frac{2}{4} = 0.5
$$

➡️ **Recall = 50%**

---

# ✔️ **F1 Score**

F1 is the **harmonic mean** of precision and recall.

$$
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
$$

$$
F1 = 2 \times \frac{0.5 \times 0.5}{0.5 + 0.5}
$$

$$
F1 = 2 \times \frac{0.25}{1} = 0.5
$$

➡️ **F1 Score = 0.5**

---

# 📌 Summary

| Metric    | Value   |
| --------- | ------- |
| Precision | **0.5** |
| Recall    | **0.5** |
| F1-score  | **0.5** |

---

If you want, I can also give you:

✅ Confusion matrix diagram
✅ Another example with different TP/FP/FN values
✅ Python code to compute precision/recall/F1

Just tell me!
