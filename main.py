def main():
    book_path = "books/frankenstein.txt"
    text = get_the_book(book_path)
    wordnum = book_word_num(text)
    letter_counts = letter_nums(text)
    letter_ls = []
    # convert dictionary into lists of dictionaries only added dictionaries if the keys are valid alphabetical values
    for letter in letter_counts: 
        testy=list(letter) 
        if testy[0].isalpha() == True: 
           letter_ls.append({"letter": letter, "num": letter_counts[letter]})
 
    letter_ls.sort(reverse=True, key=sort_ind)
    print_report(letter_ls,wordnum,book_path)

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

def sort_ind(dict):
    return dict["num"]

def print_report(sorted_dict,wordnum,book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordnum} words found in the document")
    print("")
    for entry in sorted_dict:
       let = entry["letter"]
       num = entry["num"]
       print(f"The {let} character was found {num} time")
    print("--- End report ---")


main()