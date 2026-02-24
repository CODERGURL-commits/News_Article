import re
import string
from collections import Counter
from pathlib import Path



# Read Text From File
def read_text_file(file_name):
    try:
        # Get the directory where this script is located
        base_path = Path(__file__).parent
        file_path = base_path / file_name

        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    except FileNotFoundError:
        print(f"File not found at: {file_path}")
        return ""



# Count Specific Word

def count_specific_word(text, word):
    if not text or not word:
        return 0

    cleaned_text = text.lower().translate(
        str.maketrans('', '', string.punctuation)
    )
    words = cleaned_text.split()

    return words.count(word.lower())



# Identify Most Common word
def identify_most_common_word(text):
    if not text.strip():
        return None

    cleaned_text = text.lower().translate(
        str.maketrans('', '', string.punctuation)
    )
    words = cleaned_text.split()

    if not words:
        return None

    word_count = Counter(words)
    return word_count.most_common(1)[0][0]



# Calculate Average Word Length

def calculate_average_word_length(text):
    if not text.strip():
        return 0

    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.split()

    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)



# Count Paragraphs

def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    return len(paragraphs)



# Count Sentence
def count_sentences(text):
    if not text.strip():
        return 1

    sentences = re.findall(r'[.!?]', text)
    return len(sentences)


# Main Program

if __name__ == "__main__":
    article = read_text_file("news_article.txt")

    search_word = "python"

    print("Count of specific word:", count_specific_word(article, search_word))
    print("Most common word:", identify_most_common_word(article))
    print("Average word length:", calculate_average_word_length(article))
    print("Number of paragraphs:", count_paragraphs(article))
    print("Number of sentences:", count_sentences(article))