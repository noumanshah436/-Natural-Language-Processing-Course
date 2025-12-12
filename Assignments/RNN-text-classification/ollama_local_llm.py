import requests
import json
import pandas as pd

MODEL = "llama3.2"   # any installed Ollama model
CSV_FILE = "IMDB_Dataset.csv"   # <-- update filename

def classify(text):
    prompt = (
        "Classify the sentiment of this review as Positive or Negative:\n"
        f"{text}\n"
        "Answer with only one word (positive or negative)."
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": MODEL, "prompt": prompt},
        stream=True
    )

    full_output = ""

    for line in response.iter_lines():
        if not line:
            continue
        try:
            obj = json.loads(line.decode("utf-8"))
            full_output += obj.get("response", "")
        except:
            pass

    return full_output.strip().replace(".", "").capitalize()


# -----------------------------
# Load CSV file
# -----------------------------
df = pd.read_csv(CSV_FILE)

# Normalize labels
df["sentiment"] = df["sentiment"].astype(str).str.strip().str.capitalize()

y_true = df["sentiment"].tolist()
y_pred = []

print("Testing LLM on CSV reviews...\n")

df = df.head(10)
for i, row in df.iterrows():
    review = row["review"]
    true_label = row["sentiment"]

    prediction = classify(review)

    y_pred.append(prediction)

    print(f"Review {i+1}: {review}")
    print(f"True Label: {true_label}")
    print(f"LLM Prediction: {prediction}")
    print("-" * 50)


# -----------------------------
# Compute accuracy
# -----------------------------
correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
accuracy = correct / len(df)

print("\n===================================")
print(f"Total Samples: {len(df)}")
print(f"Correct Predictions: {correct}")
print(f"Accuracy: {accuracy:.4f}")
print("===================================")
