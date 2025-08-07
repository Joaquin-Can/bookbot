import sys
from stats import count_words
from stats import each_character_count
from stats import get_list_dics
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    counter = count_words(book_text)
    new_variable = each_character_count(book_text)

    result = get_list_dics(new_variable)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {counter} total words")
    print("--------- Character Count -------")
    for dic in result:
        if dic["char"].isalpha() == True:
            print(f"{dic["char"]}: {dic["count"]}")
    print("============= END ===============")

main()
