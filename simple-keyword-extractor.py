# Simple Keyword Extraction
# Author: Hae-Ji Park (github.com/positive235)
# Date: Nov 4, 2020

from src import stopwords_english  # English stop words list
import re

def sentence_cleaner(sentence):
    """
    Returns a word list that URL, punctuation, and stop words are removed
    Input:
        sentence: the text that the user want to extract keywords

    Output:
        clean_words: a word list that URL, punctuation, and stop words are removed
    """

    # Remove URL
    sentence = re.sub(r'https?://\S+', '', sentence)

    # Remove every punctuation
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = re.sub(r'_', '', sentence)

    # Split the sentence to words (Tokenize)
    words_list = sentence.lower().split()
    clean_words = []

    for word in words_list:
        # Avoid including English stop words
        if word not in stopwords_english:
            clean_words.append(word)

    return clean_words

while True:
    print("\n\n******SIMPLE KEYWORD EXTRACTOR******\n")
    sentence = input("Enter text to extract keywords (To stop, enter 0):")
    if sentence == '0': break
    print("\nKeywords:", sentence_cleaner(sentence))

