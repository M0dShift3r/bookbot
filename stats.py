def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_character(text):
    lower_case = text.lower()
    all_characters = {}
    for character in lower_case:
        if character in all_characters:
            all_characters[character] += 1
        else: 
            all_characters[character] = 1
    return all_characters    



def sort_data(character_count):
    char_list = []
    for key, value in character_count.items():
        single_char = {"char": key, "num": value}
        char_list.append(single_char)
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)    

    return char_list    

"""
def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
"""