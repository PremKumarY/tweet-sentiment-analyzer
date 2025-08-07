import matplotlib.pyplot as plt

def plot_sentiment_distribution(sentiments):
    sentiment_counts = sentiments.value_counts()
    sentiment_counts.plot(kind='bar', title="Sentiment Analysis")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
