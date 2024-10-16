def main():
    book_path = "books/frankenstein.txt"
    text = get_the_book(book_path)
    wordnum = book_word_num(text)
    print(wordnum)
    letter_counts = letter_nums(text)
    print(letter_counts)

def get_the_book(path):
    with open(path) as b:
        return b.read()
    
def book_word_num(text):
    words = text.split()
    wordnum = len(words)
    return wordnum

def letter_nums(text):
    letter_counts = {}
    words = text.split()
    for word in words:
        word = word.lower()
        word1 = list(word)
        for letter in word1:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts

        

main()