Below is a **clear, step-by-step explanation** of **Lab Exercise 3 – Build a Simple RAG System (Retrieval + LLaMA)**, written in an **academic + practical style** suitable for labs, reports, or interviews.

I’ll explain **what**, **why**, and **how** for each step, and connect it to real-world RAG systems.

---

# 📘 Lab Exercise 3

## Build a Simple RAG System (Retrieval + LLaMA)

---

## 🎯 Goal

The goal of this lab is to build a **Question–Answer (QA) system** that can:

* Answer questions **based on your own documents**
* Reduce **hallucinations** in LLaMA
* Improve **accuracy and relevance** using **retrieval + generation**

This approach is known as **Retrieval-Augmented Generation (RAG)**.

---

## 🧠 What is RAG (High-Level)?

RAG combines two components:

1. **Retriever** → Finds relevant document chunks
2. **Generator (LLaMA)** → Generates answers using retrieved context

Instead of relying only on LLaMA’s internal knowledge, we **inject relevant context** at inference time.

---

## 🧪 Step 1 – Prepare Your Documents

### 📌 What You Do

* Collect **3–5 text documents**

  * Examples:

    * Lecture notes
    * Research summaries
    * PDFs converted to `.txt`
* Split documents into **small chunks** (200–300 words)

---

### ❓ Why Chunking Is Important

LLMs:

* Have **context length limits**
* Perform better with **focused, relevant information**

Chunking helps:

* Improve retrieval accuracy
* Avoid passing irrelevant text to the model
* Scale to large documents

---

### 🛠 Example Chunking Logic (Conceptual)

```text
Document → Split into paragraphs → Group into 200–300 word chunks
```

Each chunk becomes a **retrievable knowledge unit**.

---

### 🧪 Output of Step 1

You should have:

```python
chunks = [
    "Text chunk 1...",
    "Text chunk 2...",
    "Text chunk 3..."
]
```

---

## 🧪 Step 2 – Create Embeddings

### 📌 What You Do

Convert each text chunk into a **numerical vector (embedding)** using a pretrained model.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks, convert_to_numpy=True)
```

---

### 🧠 What Are Embeddings?

Embeddings:

* Represent text meaning in vector space
* Similar meanings → closer vectors
* Enable **semantic search**, not keyword search

Example:

> “What is backpropagation?”
> “Explain gradient descent”

These will be **closer** in embedding space than unrelated sentences.

---

### 📌 Why `all-MiniLM-L6-v2`?

* Lightweight
* Fast on CPU
* High-quality sentence embeddings
* Commonly used in RAG pipelines

---

### 🧪 Output of Step 2

```python
embeddings.shape == (num_chunks, embedding_dim)
```

Each chunk now has a vector representation.

---

## 🧪 Step 3 – Build a Simple Similarity Search

### 📌 What You Do

For a user question:

1. Convert the **question** into an embedding
2. Compute similarity with **all chunk embeddings**
3. Retrieve **top 3 most relevant chunks**

---

### 🧠 Why Similarity Search?

LLMs don’t know:

* Which document is relevant
* Where the answer exists

Similarity search:

* Filters knowledge
* Reduces noise
* Improves answer quality

---

### 🛠 Common Similarity Method

**Cosine similarity**

```python
cosine_similarity(question_embedding, chunk_embeddings)
```

Higher score → more relevant chunk.

---

### 🧪 Output of Step 3

You now have:

```text
Top 3 relevant document chunks
```

These will be passed to LLaMA.

---

## 🧪 Step 4 – Build the RAG Prompt

### 📌 What You Do

Construct a **controlled prompt** for LLaMA:

```text
Use only the following context to answer the question:

<context from top 3 chunks>

Question: <user question>
Answer:
```

---

### 🧠 Why Prompt Control Matters

This prompt:

* Forces LLaMA to **ground its answer**
* Prevents hallucination
* Makes output traceable to documents

This is the **core idea of RAG**.

---

### 🔍 Difference from Normal Prompting

| Without RAG             | With RAG            |
| ----------------------- | ------------------- |
| Uses internal knowledge | Uses your documents |
| Can hallucinate         | More factual        |
| Generic answers         | Context-specific    |

---

## 🧪 Step 5 – Test RAG vs No-RAG

### 📌 What You Do

1. Create **10 questions** based on your documents
2. Answer them using:

   * **LLaMA alone**
   * **LLaMA + RAG**
3. Compare results

---

### 📊 Evaluation Table

| Method      | Correct? | Notes                    |
| ----------- | -------- | ------------------------ |
| LLaMA alone | ❌ / ✅    | May hallucinate or guess |
| LLaMA + RAG | ✅        | Grounded in documents    |

---

### 🧠 What You Should Observe

* **LLaMA alone**:

  * Confident but sometimes wrong
  * May invent details

* **LLaMA + RAG**:

  * More accurate
  * Answers directly reference document content
  * Fewer hallucinations

---

## ✅ Final Learning Outcomes

By completing this lab, you will understand:

* How **RAG works internally**
* Why **retrieval improves LLM reliability**
* How embeddings enable **semantic search**
* Practical limitations of standalone LLMs
* How real-world systems (ChatGPT, Copilot) use RAG

---

## 🔥 Bonus (Optional Improvements)

If you want to go further:

* Use **FAISS** for faster search
* Add **source citations**
* Increase chunk overlap
* Use **re-ranking models**
* Store embeddings in a vector database

---

If you want, I can:

* Provide **full runnable Python code**
* Help you **write the lab report**
* Create **diagrams for RAG architecture**
* Help you **explain this in an interview**

Just tell me 👍
