import re
import string
from pathlib import Path

# Read Text From File

def read_text_file(file_name):
    try:
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

    count = 0
    for w in words: 
        if w == word.lower():  
            count += 1

    return count



# Identify Most Common Word

def identify_most_common_word(text):
    if not text.strip():
        return None

    cleaned_text = text.lower().translate(
        str.maketrans('', '', string.punctuation)
    )
    words = cleaned_text.split()

    if not words:
        return None

    word_count = {}

    # Count words manually (for loop + conditional)
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_common = None
    highest_count = 0

    # Find most frequent word
    for word in word_count:
        if word_count[word] > highest_count:
            highest_count = word_count[word]
            most_common = word

    return most_common


# Calculate Average Word Length

def calculate_average_word_length(text):
    if not text.strip():
        return 0

    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.split()

    if not words:
        return 0

    total_length = 0

    for word in words:  
        total_length += len(word)

    return total_length / len(words)



# Count Paragraphs

def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = text.split('\n\n')

    count = 0
    for p in paragraphs:
        if p.strip():  
            count += 1

    return count



# Count Sentences

def count_sentences(text):
    if not text.strip():
        return 1

    count = 0
    i = 0

    # Explicit while loop
    while i < len(text):
        if text[i] in ".!?":  
            count += 1
        i += 1

    return count


# Main Program

if __name__ == "__main__":
    article = read_text_file("news_article.txt")

    search_word = input("Enter a word to search for: ")

    print("Count of specific word:", count_specific_word(article, search_word))
    print("Most common word:", identify_most_common_word(article))
    print("Average word length:", calculate_average_word_length(article))
    print("Number of paragraphs:", count_paragraphs(article))
    print("Number of sentences:", count_sentences(article))