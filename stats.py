# calculation to read and count the words in a book
from collections import Counter

def read_book_content(book_name):
    with open(book_name, 'r') as file:
        file_contents = file.read()
        
    split_list = file_contents.split()
    number_of_words = len(split_list)

    return number_of_words

def count_characters(book_name):

    with open(book_name, 'r') as file:
        content = file.read()

    content = content.replace(' ', '').lower()
 
    word_count = {}

    for char in content:
        if char == "\n":
            continue
        if char.isalpha() == False:
            continue
        if char not in word_count:
            word_count[char] = 0
        word_count[char] += 1

    return word_count
    


    
