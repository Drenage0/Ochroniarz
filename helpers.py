# Helpers functions for ochroniarz.py

def replace_entities_with_placeholders(text, dictionary):
    """
    returns text with sensitive data replaced with placeholders
    """
    # Get the dictionary keys
    dict_keys = dictionary.keys()

    # create 2 versions for replacing text
    text_not_highlited = text
    text_highlited = text
    # replace each key with placeholder
    for key in dict_keys:
        text_not_highlited = text_not_highlited.replace(
            key, f"{dictionary[key]}")
        text_highlited = text_highlited.replace(
            key, f"\033[32m{dictionary[key]}\033[0m")
    # return both not highlited and highlited text
    return text_not_highlited, text_highlited


def replace_placeholders_with_entities(text, dictionary):
    """
    returns text with placeholders replaced to oryginal text
    """
    # Reverse dictionary keys->values, values->keys using dictionary comprehension
    reverse_dict = {v: k for k, v in dictionary.items()}
    # Get the reversed_dictionary keys
    reverse_dict_keys = reverse_dict.keys()

    # replace each placeholder in text
    for key in reverse_dict_keys:
        text = text.replace(key, f"{reverse_dict[key]}")
    return text


def create_file_newText_dict(newText, dictionary):
    """
    creates file called "result.txt" and writes newText and dictionary in it
    """
    # open or create new file called result.txt
    with open("result.txt", "w") as file:
        # write text into the file
        file.write("="*25 + "Zmieniony tekst" + "="*25 + "\n")  # separator
        file.write(newText + "\n")
        # convert distionary to str and write into the file
        file.write("="*25 + "Slownik zamiany" + "="*25 + "\n")  # separator
        file.write(str(dictionary) + "\n")
        file.write("="*70 + "\n")  # separator
    return True
# test
