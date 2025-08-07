import pandas as pd
from sentiment_analyzer.analyzer import analyze_sentiment
from sentiment_analyzer.visualizer import plot_sentiment_distribution

def main():
    df = pd.read_csv('data/tweets.csv')
    df['Sentiment'] = df['tweet'].apply(analyze_sentiment)
    print(df[['tweet', 'Sentiment']].head())

    plot_sentiment_distribution(df['Sentiment'])

if __name__ == "__main__":
    main()
