import pandas as pd
from collections import Counter
import re

def extract_Keyword(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = text.split()
    return words

if __name__ == "__main__":
    df = pd.read_csv("Milestone2_Sentiment_Results_new.csv")
    all_words = []
    df["clean_feedback"].apply(lambda x: all_words.extend(extract_Keyword(x)))
    keyword_freq = Counter(all_words)
    keyword_df = pd.DataFrame(keyword_freq.items(), columns=["keyword", "frequency"]).sort_values(by="frequency", ascending=False)
    keyword_df.to_csv("Milestone3_keyword_Insights.csv", index=False)
    print("Milestone 3 completed successfully!")
    print(keyword_df.head(10))