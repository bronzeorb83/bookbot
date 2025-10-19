from stats import count_words, char_count, sort_char_count

def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    text = get_book_text("books/frankenstein.txt")
    print("Analyzing book found at books/frankenstein.txt...")
    num_words = count_words(text)
    num_chars = sort_char_count(char_count(text))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in num_chars:
        char = c["name"]
        if char.isalpha():
            print(f"{c["name"]}: {c["num"]}")
    print("============= END ===============")


main()