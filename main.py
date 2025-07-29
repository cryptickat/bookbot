from stats import num_words, same_characters, sorted_list
import sys

# '/home/kat/bookbot/books/frankenstein.txt'

if len(sys.argv) < 2:
    print(f'Usage: python3 main.py <path_to_book>')
    sys.exit(1)

path = path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents

def main():
   v =  get_book_text(path).split()
   return v

# print(f'{num_words(main())} words found in the document')
# main()
number_of_words = num_words(main())
dict_of_all_the_values = (same_characters(get_book_text(path)))

print(
f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {number_of_words} total words
--------- Character Count -------
'''
)
sorted_list(dict_of_all_the_values)


