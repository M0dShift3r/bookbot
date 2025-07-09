import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import get_num_character
from stats import sort_data

def main():
    # book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_character(text)
    sort_characters = sort_data(num_characters)
    # print(f"{num_words} words found in the document")
    # print(num_characters)
    # print(sort_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")       
    for char in sort_characters:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()




main()

"""
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
"""
