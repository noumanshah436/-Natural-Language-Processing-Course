Here is the **simplest explanation** of how to calculate **n-gram probability** with clear examples (unigram + bigram + trigram).

---

# ✅ **1. Unigram Probability**

Unigram probability =
$$
P(w_i) = \frac{\text{count}(w_i)}{\text{total number of words}}
$$

### Example sentence (training data):

**"I love NLP I love AI"**

Tokenized:
$$"I", "love", "NLP", "I", "love", "AI"$$

Total words = **6**

Counts:

* count("I") = 2
* count("love") = 2
* count("NLP") = 1
* count("AI") = 1

### Probabilities:

* (P(I) = 2/6 = 0.333)
* (P(love) = 2/6 = 0.333)
* (P(NLP) = 1/6 = 0.166)
* (P(AI) = 1/6 = 0.166)

---

# ✅ **2. Bigram Probability**

Bigram probability =
$$
P(w_i \mid w_{i-1}) = \frac{\text{count}(w_{i-1}, w_i)}{\text{count}(w_{i-1})}
$$

### Using same training data:

**"I love NLP I love AI"**

### Step 1: Count bigrams

Bigrams:

* (I, love) = 2
* (love, NLP) = 1
* (NLP, I) = 1
* (love, AI) = 1

### Step 2: Take denominator = count(previous word)

* count("I") = 2
* count("love") = 2
* count("NLP") = 1

### Step 3: Compute probability

* (P(love \mid I) = \frac{2}{2} = 1.0)
* (P(NLP \mid love) = \frac{1}{2} = 0.5)
* (P(AI \mid love) = \frac{1}{2} = 0.5)
* (P(I \mid NLP) = \frac{1}{1} = 1.0)

---

# ✅ **3. Trigram Probability**

Trigram probability =
$$
P(w_i \mid w_{i-2}, w_{i-1})=
\frac{\text{count}(w_{i-2}, w_{i-1}, w_i)}
{\text{count}(w_{i-2}, w_{i-1})}
$$

### Example trigram counts:

Sentence: **"I love NLP I love AI"**

Trigrams:

* (I, love, NLP) = 1
* (love, NLP, I) = 1
* (NLP, I, love) = 1
* (I, love, AI) = 1

### Probabilities:

* (P(NLP \mid I, love) = 1 / 2 = 0.5)
  (because bigram (I, love) appears 2 times)

Similarly:

* (P(I \mid love, NLP) = 1 / 1 = 1)

---

# 🔥 Summary Table

| N-gram Type | Formula                        | Example |
| ----------- | ------------------------------ | ------- |
| **Unigram** | count(w) / total words         | 2/6     |
| **Bigram**  | count(w₁,w₂) / count(w₁)       | 2/2     |
| **Trigram** | count(w₁,w₂,w₃) / count(w₁,w₂) | 1/2     |

---

If you want, I can also show **how to compute perplexity using these n-gram probabilities**.
