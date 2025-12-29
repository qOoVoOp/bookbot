from stats import word_count, count_characters, sort_chars
import sys


def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    try: 

        filepath = sys.argv[1]
        text = get_book_text(filepath)
        num_words = word_count(text)
        print(f"Found {num_words} total words")

        characters_dict = count_characters(text)
        sorted_chars = sort_chars(characters_dict)

        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
            
    except: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    

main()