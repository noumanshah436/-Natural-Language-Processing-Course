import asyncio
import aiohttp
import json
import pandas as pd

MODEL = "llama3.2"
CSV_FILE = "IMDB_Dataset.csv"


async def classify(session, text):
    prompt = (
        "Classify the sentiment of this review as Positive or Negative:\n"
        f"{text}\n"
        "Answer with only one word (positive or negative)."
    )

    async with session.post(
        "http://localhost:11434/api/generate",
        json={"model": MODEL, "prompt": prompt},
    ) as resp:

        full_output = ""

        async for line in resp.content:
            line = line.decode("utf-8").strip()
            if not line:
                continue

            try:
                obj = json.loads(line)
                full_output += obj.get("response", "")
            except:
                pass

        return full_output.strip().replace(".", "").capitalize()


async def main():
    df = pd.read_csv(CSV_FILE)
    df["sentiment"] = df["sentiment"].astype(str).str.strip().str.capitalize()

    df = df.head(10)   # first 10 samples

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _, row in df.iterrows():
            tasks.append(classify(session, row["review"]))

        print("Running sentiment classification in parallel...\n")

        # Run all LLM calls concurrently
        predictions = await asyncio.gather(*tasks)

    # Add predictions to df
    df["pred"] = predictions

    # Print each review result
    for i, row in df.iterrows():
        print(f"Review {i+1}: {row['review']}")
        print(f"True Label: {row['sentiment']}")
        print(f"LLM Prediction: {row['pred']}")
        print("-" * 50)

    # Accuracy
    correct = sum(df["sentiment"] == df["pred"])
    accuracy = correct / len(df)

    print("\n===================================")
    print(f"Total Samples: {len(df)}")
    print(f"Correct Predictions: {correct}")
    print(f"Accuracy: {accuracy:.4f}")
    print("===================================")


# Run
asyncio.run(main())
