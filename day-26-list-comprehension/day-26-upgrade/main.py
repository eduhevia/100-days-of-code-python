import pandas as pd

data = pd.read_csv("day-26-list-comprehension/data/nato_phonetic_alphabet.csv")

phonetic_dict = {row["letter"]: row["code"] for _, row in data.iterrows()}


def generate_phonetic():
    word = input("NATO phonetic alphabet convertor, insert a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
