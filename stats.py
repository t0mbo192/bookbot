# calculation to read and count the words in a book
from collections import Counter

def read_book_content(book_name):
    with open(book_name) as file:
        file_contents = file.read()
        
    split_list = file_contents.split()
    number_of_words = len(split_list)

    return number_of_words

def count_characters(book_name):
    with open(book_name) as file:
        file_content = file.read()

    lower_characters = file_content.lower()

    frequent_character = Counter(lower_characters)

    return frequent_character