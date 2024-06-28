# src/word_counter.py
def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    sample_text = "Hello world! This is a simple word counting program."
    print(f"Number of words: {count_words(sample_text)}")
