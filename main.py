from stats import read_book_content
from stats import count_characters
import sys

def main():

    book = r"/home/tommygun2486/Workspace/bookbot/books/frankenstein.txt"

    number_of_words_in_book = read_book_content(book)
    number_of_characters_in_book = count_characters(book)
    print("========== BOOKBOT ===========")
    print(f"Analyzing book found at {book}")
    print("---------- Word Count ----------")
    print(f"Found {number_of_words_in_book} total words")
    print("-------- Character Count -------")
    for key, value in number_of_characters_in_book.items():
        print(f"{key}: {value}")
    print("========== END ==========")

    print(sys.argv[1])

if __name__ == '__main__':
    main()

    
