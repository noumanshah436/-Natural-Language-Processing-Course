Perplexity (PPL) is a common metric in NLP to measure how well a language model predicts a sequence of words.
**Lower perplexity = better model** (it is “less confused”).

---

# ✅ **Definition**

For a sequence of tokens ( w_1, w_2, ..., w_N ):

$$
\text{Perplexity} = e^{-\frac{1}{N}\sum_{i=1}^{N}\log P(w_i)}
$$

If you use log base 2:

$$
\text{Perplexity} = 2^{-\frac{1}{N}\sum_{i=1}^{N}\log_2 P(w_i)}
$$

---

# ✅ **Simple Example**

Suppose your language model produces the following probabilities for a sentence:

**Sentence:**
`I like apples`

Tokens and model probabilities:

| Token  | Probability (P(w_i)) |
| ------ | -------------------- |
| I      | 0.20                 |
| like   | 0.10                 |
| apples | 0.25                 |

Total tokens (N = 3).

---

## Step 1: Compute log probabilities

$$
\log P(I) = \log(0.20) = -1.609
$$
$$
\log P(like) = \log(0.10) = -2.302
$$
$$
\log P(apples) = \log(0.25) = -1.386
$$

---

## Step 2: Compute average negative log-likelihood

$$
-\frac{1}{3}(-1.609 -2.302 -1.386)
$$

$$
= \frac{1}{3}(1.609 + 2.302 + 1.386)
$$

$$
= \frac{5.297}{3} = 1.7657
$$

---

## Step 3: Exponentiate to get perplexity

$$
\text{PPL} = e^{1.7657} \approx 5.85
$$

---

# 🎉 **Final Answer**

**Perplexity = 5.85**

This means the model is "as confused as if it had to choose among ~6 equally likely options" at each step.

---

# 🧠 Quick intuition

* If probabilities are high → log probs are less negative → perplexity decreases → model is confident.
* If probabilities are low → perplexity increases → model is confused.

---

If you want, I can also give you a **Python example**, or show how perplexity is computed in **language models like GPT, LSTM, Transformer**.
