def main():
    book_path = "books/frankenstein.txt"
    text = get_the_book(book_path)
    wordnum = book_word_num(text)
    print(wordnum)

def get_the_book(path):
    with open(path) as b:
        return b.read()
    
def book_word_num(text):
    words = text.split()
    wordnum = len(words)
    return wordnum

main()