import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book> --> requires a filepath to a book")
    sys.exit(1)
    

def get_book_text(filepath):
    text_string = filepath.read()
    return text_string
        
def main():
    with open(sys.argv[1]) as book:
        return get_book_text(book)

from stats import num_of_words
from stats import letters_of_book
from stats import dict_sorted

#num_of_words(main())
#letters_of_book(main())
sorted_dictionary = dict_sorted(letters_of_book(main()))




print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(num_of_words(main()))
print("--------- Character Count -------")
for i in sorted_dictionary:
    if i["char"].isalpha():
        print(f"{i["char"]}: {i["num"]}")
print("============= END ===============")