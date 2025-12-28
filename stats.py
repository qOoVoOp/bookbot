def word_count(text):
  num_words = 0
  for word in text.split():
    num_words += 1
  return num_words

def count_characters(text):
  characters_dict = {

  }
  words = text.split()
  character_count = 0
  for word in words:
    lower_word = word.lower()
    for char in lower_word:
      count = 1
      if char not in characters_dict:
        characters_dict[char] = 1
      else:
        characters_dict[char] += 1

  return characters_dict



def sort_chars(characters_dict):
    character_list = []

    for char, num in characters_dict.items():
        character_list.append({"char": char, "num": num})

    def sort_on_num(d):
        return d["num"]

    character_list.sort(key=sort_on_num, reverse=True)

    return character_list




    

