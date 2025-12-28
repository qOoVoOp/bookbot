from stats import word_count,count_characters, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
  bookfile = "books/frankenstein.txt"
  text = get_book_text(bookfile)
  num_words = word_count(text)
  print(f"Found {num_words} total words")

  characters_dict = count_characters(text)
  sorted_chars = sort_chars(characters_dict)
  for i in sorted_chars:
    print(i)


main()