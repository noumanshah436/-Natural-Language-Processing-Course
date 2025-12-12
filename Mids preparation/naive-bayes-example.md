Here is **the simplest possible Naive Bayes example** using small numbers, so you can understand the full calculation.

---

# ✅ **Naive Bayes Example (Very Simple)**

We will classify a message as **Spam** or **Not Spam** using the word **“buy”**.

---

## **Training Data**

| Message             | Label    |
| ------------------- | -------- |
| “buy now”           | Spam     |
| “limited offer buy” | Spam     |
| “meeting tomorrow”  | Not Spam |
| “project meeting”   | Not Spam |

---

## **Step 1: Count word frequencies**

### For **Spam (S)**:

Messages: “buy now”, “limited offer buy”

Words in spam:

* buy → 2
* now → 1
* limited → 1
* offer → 1

Total spam words = **5**

### For **Not Spam (NS)**:

Messages: “meeting tomorrow”, “project meeting”

Words in not spam:

* meeting → 2
* tomorrow → 1
* project → 1

Total not-spam words = **4**

---

## **Step 2: Compute prior probabilities**

Total messages = 4

* P(Spam) = 2/4 = **0.5**
* P(Not Spam) = 2/4 = **0.5**

---

## **Step 3: Classify new message**

### **New message: “buy project”**

We compute:

### **1. P("buy project" | Spam)**

* P(buy | Spam) = 2/5
* P(project | Spam) = 0/5 → **0 (problem)**

To avoid 0, we use **Laplace smoothing**:
Formula: (count + 1) / (total words + vocabulary size)

Vocabulary size = 7 unique words
(buy, now, limited, offer, meeting, tomorrow, project)

#### Compute with smoothing:

* P(buy|Spam)     = (2+1)/(5+7) = 3/12
* P(project|Spam) = (0+1)/(5+7) = 1/12

So:

P(sentence | Spam)
= (3/12) × (1/12)
= **3/144**

---

### **2. P("buy project" | Not Spam)**

Counts:

* buy → 0
* project → 1

Total words = 4

Apply smoothing:

* P(buy|NS)     = (0+1)/(4+7) = 1/11
* P(project|NS) = (1+1)/(4+7) = 2/11

P(sentence | NS)
= (1/11) × (2/11)
= **2/121**

---

## **Step 4: Multiply by priors**

* Spam score = P(S) × likelihood
  = 0.5 × (3/144)
  = **3/288**

* Not-Spam score = 0.5 × (2/121)
  = **2/242**

Convert to decimal:

* Spam score ≈ 0.0104
* Not-Spam score ≈ 0.0083

---

## ✅ **Final Prediction: SPAM**

Because:

**0.0104 > 0.0083**

---

# 🎉 Final Summary

Your message **“buy project”** is classified as **Spam** using Naive Bayes.

---

If you want, I can give:
✔ even simpler example
✔ without Laplace smoothing
✔ code in Python
✔ bigram Naive Bayes version

Just tell me!
