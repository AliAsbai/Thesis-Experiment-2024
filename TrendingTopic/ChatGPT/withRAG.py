from collections import Counter, defaultdict
import heapq
import sys

class TrendingTopics:
    def __init__(self):
        self.word_count = defaultdict(Counter)
        self.current_day = 0

    def process_text(self, text):
        words = text.split()
        for word in words:
            if len(word) >= 4:
                self.word_count[self.current_day][word] += 1

    def process_query(self, top_n):
        merged_counter = Counter()
        for day in range(max(0, self.current_day - 6), self.current_day + 1):
            merged_counter += self.word_count[day]

        top_words = heapq.nlargest(top_n, merged_counter.items(), key=lambda x: (-x[1], x[0]))
        for word, count in top_words:
            print(f"{word} {count}")

    def run(self):
        in_text = False
        for line in sys.stdin:
            line = line.strip()
            if line.startswith("<text>"):
                in_text = True
            elif line.startswith("</text>"):
                self.current_day += 1
                in_text = False
            elif line.startswith("<top"):
                if in_text:
                    self.current_day += 1
                    in_text = False
                top_n = int(line.split()[1].strip("/>"))
                print(f"<top {top_n}>")
                self.process_query(top_n)
                print("</top>")
            elif in_text:
                self.process_text(line)

if __name__ == "__main__":
    trending_topics = TrendingTopics()
    trending_topics.run()
