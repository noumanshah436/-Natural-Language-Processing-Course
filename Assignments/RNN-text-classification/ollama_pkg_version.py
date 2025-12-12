import asyncio
import time
import pandas as pd
import ollama

MODEL = "llama3.2"
CSV_FILE = "IMDB_Dataset.csv"
LOG_FILE = "sentiment_logs.txt"

client = ollama.AsyncClient()


def truncate_review(review, max_words=200):
    """Truncate review to the first max_words words."""
    words = review.split()
    truncated = " ".join(words[:max_words])
    return truncated


async def main():
    df = pd.read_csv(CSV_FILE).head(100)
    df["sentiment"] = df["sentiment"].str.strip().str.lower()

    # Clear the log file at start
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("Sentiment Classification Logs\n")
        f.write("=====================================\n\n")

    print("Starting persistent Ollama session...")

    # Warm the model once
    await client.chat(
        model=MODEL,
        messages=[{"role": "system", "content": "Sentiment classifier ready."}],
        stream=False,
    )

    print("Model warmed. Starting classification...\n")

    predictions = []
    start = time.time()

    for i, row in df.iterrows():
        review_text = truncate_review(row["review"], max_words=200)
        actual_sentiment = row["sentiment"]

        prompt = (
            prompt
        ) = f"""
        Classify the sentiment of the following review as 'positive' or 'negative' (one word only). Do not explain.

        Example 1:
        Review: "I loved this movie, it was amazing!"
        Sentiment: positive

        Example 2:
        Review: "Terrible film, wasted my time."
        Sentiment: negative

        Now classify:
        Review: "{review_text}"
        Sentiment:
        """

        t0 = time.time()
        response = await client.chat(
            model=MODEL, messages=[{"role": "user", "content": prompt}], stream=False
        )
        t1 = time.time()

        pred = response["message"]["content"].strip().lower()
        predictions.append(pred)

        time_taken = round(t1 - t0, 2)

        print(f"[{i+1}/100] {pred} ({time_taken}s)")

        # Append logs to text file
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"--- Review #{i+1} ---\n")
            f.write(f"Review: {review_text}\n")
            f.write(f"Actual Sentiment: {actual_sentiment}\n")
            f.write(f"Model Prediction: {pred}\n")
            f.write(f"Time Taken: {time_taken} sec\n")
            f.write("\n")

    total = time.time() - start

    print(f"\nFinished all 100 reviews in: {total:.2f} sec")

    df["pred"] = predictions
    correct = (df["sentiment"] == df["pred"]).sum()

    print(f"Total correct = {correct}")

    print(f"Accuracy: {correct/100:.4f}")
    print(f"Logs saved to {LOG_FILE}")


asyncio.run(main())
