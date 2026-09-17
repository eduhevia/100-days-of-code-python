import pandas as pd

data = pd.read_csv("day-26-list-comprehension/data/nato_phonetic_alphabet.csv")

# Loop through rows of a data frame
phonetic_dict = {row["letter"]: row["code"] for _, row in data.iterrows()}
word = input("NATO phonetic alphabet convertor, insert a word: ").upper()

# Transform the word into a NATO phonetic alphabet
final_list = [phonetic_dict.get(letter, letter) for letter in word]
print(final_list)
