def word_count(text):
    num_words = 0
    for word in text.split():
        num_words += 1
    return num_words


def count_characters(text):
    characters_dict = {}
    for char in text.lower():
        if char.isalpha():  # nur Buchstaben zählen (inkl. Umlaute/Accents wie æ â ê ë ô)
            characters_dict[char] = characters_dict.get(char, 0) + 1
    return characters_dict


def sort_chars(characters_dict):
    character_list = []

    for char, num in characters_dict.items():
        character_list.append({"char": char, "num": num})

    def sort_on_num(d):
        return d["num"]

    character_list.sort(key=sort_on_num, reverse=True)
    return character_list