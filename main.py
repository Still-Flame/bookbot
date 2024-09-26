def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    print(f"{words} found in this document")


def count_words(text):
    count = 0
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()




main()