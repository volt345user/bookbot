from stats import get_num_words
from stats import get_num_char
from stats import sort_on
import sys

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    num_words = get_num_words(file_contents)
    char_dict_list = get_num_char(file_contents)
    char_dict_list.sort(reverse=True,key=sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in range(0, len(char_dict_list)): 
        entry_dict = char_dict_list[x]
        
        if entry_dict["char"].isalpha():
            print(f"{entry_dict["char"]}: {entry_dict["num"]}")

    print("============= END ===============")

main()