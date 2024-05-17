from collections import Counter
import re

def process_text(text):
    words = re.findall(r'\b\w{4,}\b', text.lower())
    return Counter(words)

def update_frequency(curr_freq, new_freq):
    for word, count in new_freq.items():
        curr_freq[word] += count
    return curr_freq

def get_top_words(frequency, n):
    sorted_freq = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    top_words = [f"{word} {count}" for word, count in sorted_freq[:n]]
    return top_words

def main():
    frequency = Counter()
    text = ""
    while True:
        try:
            line = input().strip()
            if line.startswith("<text>"):
                while not line.endswith("</text>"):
                    text += line.replace("<text>", "").strip() + " "
                    line = input().strip()
                text += line.replace("</text>", "").strip()
                daily_frequency = process_text(text)
                frequency = update_frequency(frequency, daily_frequency)
                text = ""
            elif line.startswith("<top"):
                n = int(re.search(r'\d+', line).group())
                top_words = get_top_words(frequency, n)
                print(f"<top {n}>")
                for word in top_words:
                    print(word)
                print("</top>")
        except EOFError:
            break

if __name__ == "__main__":
    main()
