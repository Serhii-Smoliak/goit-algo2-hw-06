import requests
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt

def download_text(url):
    response = requests.get(url)
    return response.text

def clean_text(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words

def map_reduce(words):
    word_counts = Counter(words)
    return word_counts

def visualize_top_words(word_counts, top_n=10):
    most_common = word_counts.most_common(top_n)
    words, counts = zip(*most_common)

    plt.barh(words, counts)
    plt.ylabel('Words')
    plt.xlabel('Frequency')
    plt.title(f'Top {top_n} Words by Frequency')
    plt.show()

if __name__ == '__main__':
    url = 'https://www.gutenberg.org/cache/epub/75121/pg75121.txt'
    text = download_text(url)

    with ThreadPoolExecutor() as executor:
        words = executor.submit(clean_text, text)
        word_counts = executor.submit(map_reduce, words.result())

    visualize_top_words(word_counts.result())
