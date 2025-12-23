from stats import read_book_content
from stats import count_characters

def main():

    book = r"/home/tommygun2486/Workspace/bookbot/books/frankenstein.txt"

    number_of_words_in_book = read_book_content(book)
    number_of_characters_in_book = count_characters(book)

    print(f"Found {number_of_words_in_book} total words")
    print(number_of_characters_in_book)

if __name__ == '__main__':
    main()

    
