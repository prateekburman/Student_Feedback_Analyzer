import os
import re
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt

STOP_WORDS = {"and", "but", "the", "is", "a", "of", "too"}


def load_feedback(filename):
    """Read CSV with Pandas. Returns DataFrame or None if file is missing/bad."""
    if not os.path.exists(filename):
        print(f"Error: file '{filename}' not found.")
        return None
    try:
        # dtype=str so that bad ratings like 'abc' don't break reading
        df = pd.read_csv(filename, dtype=str, keep_default_na=False)
    except Exception as e:
        print(f"Error: could not read file ({e}).")
        return None

    df.columns = [c.strip() for c in df.columns]
    needed = ["StudentID", "Rating", "Comment"]
    if any(col not in df.columns for col in needed):
        print("Error: CSV must have columns StudentID, Rating, Comment.")
        return None
    return df


def validate_rating(value):
    """Return rating as int if it is a whole number from 1 to 5, else None."""
    try:
        num = float(str(value).strip())
    except ValueError:
        return None
    if num.is_integer() and 1 <= num <= 5:
        return int(num)
    return None


def clean_data(df):
    """Keep only valid rows, print a warning for each invalid row."""
    valid_rows = []
    for row_no, (_, row) in enumerate(df.iterrows(), start=1):
        rating = validate_rating(row["Rating"])
        if rating is None:
            print(f"Warning: Row {row_no} skipped - rating must be a whole number from 1 to 5.")
            continue
        valid_rows.append({"StudentID": row["StudentID"],
                           "Rating": rating,
                           "Comment": str(row["Comment"])})
    return pd.DataFrame(valid_rows, columns=["StudentID", "Rating", "Comment"])


def top_words(df, n=3):
    """Most frequent words in comments, stop words removed, ties alphabetical."""
    counter = Counter()
    for comment in df["Comment"]:
        words = re.findall(r"[a-z]+", comment.lower())
        counter.update(w for w in words if w not in STOP_WORDS)
    # sort by count (high -> low), then alphabetically
    return sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:n]


def show_summary(df):
    print(f"\nValid feedback: {len(df)}")
    if df.empty:
        print("No valid data to analyze.")
        return
    print(f"Average rating: {df['Rating'].mean():.2f}")

    counts = df["Rating"].value_counts()
    parts = [f"{r} -> {counts.get(r, 0)}" for r in range(5, 0, -1)]
    print("Ratings: " + ", ".join(parts))

    words = top_words(df)
    print("Top 3 words: " + ", ".join(f"{w} ({c})" for w, c in words))


def show_sentiment(df):
    total = len(df)
    if total == 0:
        print("No valid data to analyze.")
        return
    positive = int((df["Rating"] >= 4).sum())
    neutral = int((df["Rating"] == 3).sum())
    negative = int((df["Rating"] <= 2).sum())

    print()
    for name, val in [("Positive", positive), ("Neutral", neutral), ("Negative", negative)]:
        print(f"{name}: {val} ({val / total * 100:.2f}%)")

    # Bar chart
    plt.bar(["Positive", "Neutral", "Negative"], [positive, neutral, negative],
            color=["green", "gold", "red"])
    plt.title("Student Feedback Sentiment")
    plt.ylabel("Number of students")
    plt.savefig("sentiment_chart.png")
    print("(bar chart is displayed)")
    plt.show()


def main():
    filename = input("Enter CSV file name (press Enter for feedback.csv): ").strip()
    if not filename:
        filename = "feedback.csv"

    raw = load_feedback(filename)
    if raw is None:
        return
    df = clean_data(raw)

    while True:
        print("\n===== Student Feedback Analyzer =====")
        print("1. Summary and top 3 words")
        print("2. Sentiment")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            show_summary(df)
        elif choice == "2":
            show_sentiment(df)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()