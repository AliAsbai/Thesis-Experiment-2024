from collections import Counter, deque

MAX_DAYS = 7
MAX_WORDS = 20


def solve():
  word_counts = deque(maxlen=MAX_DAYS)
  current_count = Counter()
  in_text = False  # Flag to track if we're currently processing text

  for line in iter(input, ''):
    line = line.strip()

    if in_text:  # Process lines only when inside a text block
      if not line:  # Handle empty lines within text block
        word_counts.append(current_count)
        current_count = Counter()
      else:  # Process words in the line
        for word in line.split():
          if len(word) > 3:
            current_count[word.lower()] += 1

    elif line.startswith('<text>'):
      in_text = True
    elif line.startswith('</text>'):
      in_text = False

    elif line.startswith('<top'):
      n = int(line.split()[1])
      merged_count = sum(word_counts, Counter())
      top_words = merged_count.most_common(n)
      print(f"<top {n}>")
      for word, count in top_words:
        print(f"{word} {count}")

  # Add the words from the last text block if it exists
  if in_text:
    word_counts.append(current_count)

  solve()
