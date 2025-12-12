import pandas as pd

# Load CSV
df = pd.read_csv("gutenberg_authors_dataset.csv")

# Filter only Shakespeare rows
shakespeare_df = df[df["author"].str.lower() == "shakespeare"]

# Combine all text into one string
all_text = "\n\n".join(shakespeare_df["text"].tolist())

# Save to txt file
with open("tiny.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("Saved tiny.txt with", len(shakespeare_df), "rows.")
