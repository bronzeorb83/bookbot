from stats import count_words, char_count

def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    #print(text)
    num_words = count_words(text)
    num_chars = char_count(text) 
    print(f"Found {num_words} total words")
    print(num_chars)

main()