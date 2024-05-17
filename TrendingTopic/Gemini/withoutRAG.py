from collections import defaultdict, Counter

class TrendingTopics:
  def __init__(self):
    self.word_counts = Counter()  # Use Counter for efficient merging
    self.day_queue = collections.deque(maxlen=7)  # Keep track of daily word counts

  def add_text(self, text):
    # Preprocess text: lowercase and remove words less than 4 characters
    words = [word.lower() for word in text.split() if len(word) >= 4]
    self.word_counts.update(words)  # Update Counter efficiently

    # Add daily word count to the queue (converted to Counter for efficiency)
    self.day_queue.append(Counter(self.word_counts))

  def get_top_n(self, n):
    # Merge word counts from last 7 days (efficiently with Counter)
    merged_counts = sum(self.day_queue, start=Counter())

    # Get top N words and their frequencies
    top_n_words = merged_counts.most_common(n)

    # Handle potential edge cases (no words or ties)
    if not top_n_words:
      return []  # Return empty list if no words meet the criteria
    top_n_freq = min(count for _, count in top_n_words)

    # Return words with frequency equal to top_n_freq (using Counter methods)
    return [word for word, count in merged_counts.items() if count == top_n_freq]

# Usage example
topics = TrendingTopics()
topics.add_text("This is a sample text please please")
topics.add_text("Another day, another text please")

print("<top 3>")
print(topics.get_top_n(3))

topics.add_text("Blah blah blah please")

print("<top 2>")
print(topics.get_top_n(2))
