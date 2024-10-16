def main():
    book_path = "books/frankenstein.txt"
    text = get_the_book(book_path)
    print(text)

def get_the_book(path):
    with open(path) as b:
        return b.read()
    
main()