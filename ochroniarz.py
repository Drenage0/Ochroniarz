# == Import libraries ==
from openai import OpenAI, AuthenticationError
import spacy
import sys

from helpers import replace_entities_with_placeholders, replace_placeholders_with_entities, create_file_newText_dict

# == Global variables ==
END_MES = "====Program zakonczony===="
# * flags
detected_harassment_or_threats = False
detected_sensitive_data = False

# == First check if valid usage ==
if len(sys.argv) != 2:
    print("Złe użycie.\nAby uruchomić: python ochroniarz.py text/text1.txt")
    # ! exit program if wrong usage
    sys.exit(1)
# * check format of the file
if not sys.argv[1].endswith(".txt"):
    print("Wymagany plik .txt")
    sys.exit(1)

# == Try to open file and read it to text variable ==
# TODO: only txt files
try:
    text = open(sys.argv[1], "r").read().strip().strip("\n")
except FileNotFoundError:
    print(f"Nie znaleziono pliku: {sys.argv[1]}")
    sys.exit(2)
# print text if file found
print("========Tresc dokumentu============")
print(text)
print("=========End===========")

# == Initialize OpenAi library ==
# * read API key from file
API_KEY = open("API_KEY", "r").read()
# * create OpenAi client
client = OpenAI(
    api_key=API_KEY)
# * try to get a response from moderations endpoint
try:
    response = client.moderations.create(
        input=text)
except (AuthenticationError, NameError):
    response = ""
    while True:
        print("Error: Błędny klucz API, czy chcesz kontynuować bez sprawdzania mowy nienawiści?")
        users_input = input("Wpisz Y/N: ")
        if users_input.lower() == "y":
            break
        elif users_input.lower() == "n":
            sys.exit(END_MES)


# == Hate speech recognition - OpenAI moderations ==
# check response if there is one
if response:
    # * load all categories
    categories = response.results[0].categories
    categories_dict = vars(categories)  # * access attributes as dict
    # * load all categories scores
    category_scores = response.results[0].category_scores
    category_scores_dict = vars(category_scores)  # * access attributes as dict
    # print if hate speech detected
    for key in categories_dict:
        if categories_dict[key] == True:

            # * Set flag to True when something detected
            detected_harassment_or_threats = True
            # * print message
            print("❗\033[31mWykryto",
                  key, "==",
                  categories_dict[key],
                  "!", end=" ")
            print(f"\033[0mOkreślona wartość {
                  round(category_scores_dict[key], 2)} na 1.0")
        else:
            # * if False continue to the next key
            continue
    if not detected_harassment_or_threats:
        print(
            "✅\033[32m Nie znaleziono mowy nienawiści/gróźb/zastraszania/molestowania \033[0m")

else:
    print("====Kontynuacja bez sprawdzania mowy nienawiści====")


#  == Sensitive information recognition - spacy ==

# *initialize spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# *create dictionary for replacing words for placeholders {"Entity": "placeholder", ...}
dataTransform_dict = {}

# value index - for making values in dictionary UNIQUE
count = 0
for ent in doc.ents:
    if ent.text in dataTransform_dict:
        # *if key exists, just continue to the nest ent
        continue
    else:
        # * Set flag to True when something detected
        detected_sensitive_data = True
        # * add key/value pair dictionary with unique value count
        dataTransform_dict[ent.text] = ent.label_ + f"[{count}]"
        count += 1

if not detected_sensitive_data:
    print("✅\033[32m Nie znaleziono wrażliwych danych \033[0m")
else:
    print("❗\033[31mWykryto wrażliwe dane \033[0m")
    # print(dataTransform_dict)

    # changing text with placeholders

    changed_text, changed_text_highlited = replace_entities_with_placeholders(
        text, dataTransform_dict)
    print("========Oryginalny tekst============")
    print(text)
    print("=========Zmieniony tekst===========")
    print(changed_text_highlited + "\n" + "="*70)

    # == Sensitive information new file ==
    while True:
        print("Czy chcesz utworzyć plik \"result.txt\" z placeholderami na wrażliwe dane?")
        to_create = input("Wpisz Y/N: ")
        if to_create == "y":

            # create "result.txt" file with changed text and dataTransform dict
            create_file_newText_dict(changed_text, dataTransform_dict)
            print("✅\033[32m Utworzono plik \"result.txt\" \033[0m")
            break
        elif to_create.lower() == "n":
            print(END_MES)
            sys.exit(0)

    print(END_MES)
    sys.exit(0)
