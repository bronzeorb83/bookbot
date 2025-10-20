import sys
from stats import count_words, char_count, sort_char_count

def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, num_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in num_chars:
        char = c["name"]
        if char.isalpha():
            print(f"{c["name"]}: {c["num"]}")
    print("============= END ===============")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = sort_char_count(char_count(text))
    print_report(book_path, num_words, num_chars)
    
   


main()